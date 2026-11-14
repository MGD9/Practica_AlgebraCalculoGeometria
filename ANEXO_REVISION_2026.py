"""Revisión posterior, 14/11/2026. El notebook de formación permanece intacto.
Ejecutar pruebas: python3 ANEXO_REVISION_2026.py --comprobar
"""
from collections import Counter
from numbers import Integral
import argparse
import unittest
import numpy as np


def _normalizar(mc):
    if any(isinstance(n, bool) or not isinstance(n, Integral) or n < 0 for n in mc.values()):
        raise ValueError("Las multiplicidades deben ser enteros no negativos")
    return {k: int(v) for k, v in mc.items() if v > 0}


def multiconjunto(elementos):
    return dict(Counter(elementos))


def cardinalidad(mc):
    return sum(_normalizar(mc).values())


def pertenece(mc, elemento):
    return _normalizar(mc).get(elemento, 0) > 0


def inserta(mc, elemento):
    resultado = _normalizar(mc)
    resultado[elemento] = resultado.get(elemento, 0) + 1
    return resultado


def elimina(mc, elemento):
    resultado = _normalizar(mc)
    if resultado.get(elemento, 0) > 1:
        resultado[elemento] -= 1
    else:
        resultado.pop(elemento, None)
    return resultado


def subconjunto(a, b):
    a, b = _normalizar(a), _normalizar(b)
    return all(n <= b.get(k, 0) for k, n in a.items())


def iguales(a, b):
    return _normalizar(a) == _normalizar(b)


def union(a, b):
    # Convención de la práctica: sumar multiplicidades, no usar el máximo.
    a, b = _normalizar(a), _normalizar(b)
    return {k: a.get(k, 0) + b.get(k, 0) for k in a.keys() | b.keys()}


def interseccion(a, b):
    a, b = _normalizar(a), _normalizar(b)
    return {k: min(a[k], b[k]) for k in a.keys() & b.keys()}


def diferencia(a, b):
    a, b = _normalizar(a), _normalizar(b)
    return {k: n - b.get(k, 0) for k, n in a.items() if n > b.get(k, 0)}


def _matriz(x):
    x = np.asarray(x, dtype=float)
    if x.ndim != 2 or min(x.shape) == 0 or not np.isfinite(x).all():
        raise ValueError("Se necesita una matriz no vacía y con valores finitos")
    return x


def aproximacion_svd(x, rango):
    x = _matriz(x)
    if isinstance(rango, bool) or not isinstance(rango, Integral) or not 1 <= rango <= min(x.shape):
        raise ValueError("Rango fuera de los límites de la matriz")
    u, s, vt = np.linalg.svd(x, full_matrices=False)
    return (u[:, :rango] * s[:rango]) @ vt[:rango, :]


def _regresion_datos(x, y):
    x = _matriz(x)
    y = np.asarray(y, dtype=float)
    if y.shape != (len(x),) or not np.isfinite(y).all():
        raise ValueError("El objetivo debe tener una observación finita por fila")
    return np.column_stack([np.ones(len(x)), x]), y


def minimos_cuadrados(x, y):
    # lstsq evita invertir X.T @ X y admite columnas linealmente dependientes.
    diseno, y = _regresion_datos(x, y)
    return np.linalg.lstsq(diseno, y, rcond=None)[0]


def descenso_gradiente(x, y, tolerancia=1e-9, iteraciones=100000):
    diseno, y = _regresion_datos(x, y)
    if tolerancia <= 0 or iteraciones < 1:
        raise ValueError("La tolerancia y las iteraciones deben ser positivas")
    paso = 0.9 / (np.linalg.norm(diseno, ord=2) ** 2 / len(y))
    beta = np.zeros(diseno.shape[1])
    for _ in range(iteraciones):
        gradiente = diseno.T @ (diseno @ beta - y) / len(y)
        if np.linalg.norm(gradiente, ord=np.inf) <= tolerancia:
            return beta
        beta -= paso * gradiente
    raise RuntimeError("No se alcanzó la tolerancia; revisar escala y límite de iteraciones")


def similitud_coseno(a, b):
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    if a.ndim != 1 or a.shape != b.shape or len(a) == 0 or not np.isfinite(a).all() or not np.isfinite(b).all():
        raise ValueError("Se necesitan dos vectores finitos de la misma dimensión")
    norma = np.linalg.norm(a) * np.linalg.norm(b)
    return 0.0 if norma == 0 else float(np.clip(np.dot(a, b) / norma, -1, 1))


class PruebasRevision(unittest.TestCase):
    def test_elemento_ausente(self):
        self.assertFalse(pertenece({1: 2}, 9))
    def test_igualdad(self):
        self.assertTrue(iguales({1: 2}, {1: 2, 2: 0}))
    def test_subconjunto_vacio(self):
        self.assertTrue(subconjunto({}, {1: 2}))
    def test_subconjunto_segundo_elemento(self):
        self.assertFalse(subconjunto({1: 1, 2: 1}, {1: 2}))
    def test_multiplicidades(self):
        self.assertFalse(subconjunto({1: 3}, {1: 2}))
    def test_diferencia_resta(self):
        self.assertEqual(diferencia({1: 4, 2: 1}, {1: 2, 2: 4}), {1: 2})
    def test_union_suma(self):
        self.assertEqual(union({1: 2}, {1: 3, 2: 1}), {1: 5, 2: 1})
    def test_interseccion(self):
        self.assertEqual(interseccion({1: 2, 2: 1}, {1: 3}), {1: 2})
    def test_sin_mutar_entrada(self):
        a = {1: 1}
        self.assertEqual(inserta(a, 1), {1: 2})
        self.assertEqual(elimina(a, 1), {})
        self.assertEqual(a, {1: 1})
    def test_conteo(self):
        self.assertEqual(cardinalidad(multiconjunto([1, 1, 2])), 3)
    def test_multiplicidad_invalida(self):
        with self.assertRaises(ValueError): cardinalidad({1: -1})
    def test_svd(self):
        x = np.array([[3., 0.], [0., 1.]])
        np.testing.assert_allclose(aproximacion_svd(x, 1), [[3, 0], [0, 0]])
        np.testing.assert_allclose(aproximacion_svd(x, 2), x)
    def test_regresion_y_colinealidad(self):
        x = np.arange(10.).reshape(-1, 1)
        np.testing.assert_allclose(minimos_cuadrados(x, 2 + 3*x[:, 0]), [2, 3], atol=1e-8)
        beta = minimos_cuadrados(np.c_[x, 2*x], 2 + 3*x[:, 0])
        np.testing.assert_allclose(np.c_[np.ones(10), x, 2*x] @ beta, 2+3*x[:, 0], atol=1e-8)
    def test_gradiente(self):
        x = np.linspace(-1, 1, 30).reshape(-1, 1)
        np.testing.assert_allclose(descenso_gradiente(x, 2+3*x[:, 0]), [2, 3], atol=1e-6)
    def test_coseno(self):
        self.assertAlmostEqual(similitud_coseno([1,0], [1,0]), 1)
        self.assertAlmostEqual(similitud_coseno([1,0], [0,1]), 0)
        self.assertEqual(similitud_coseno([0,0], [1,1]), 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comprobar", action="store_true")
    args = parser.parse_args()
    if args.comprobar:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(PruebasRevision)
        raise SystemExit(not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful())
    parser.print_help()
