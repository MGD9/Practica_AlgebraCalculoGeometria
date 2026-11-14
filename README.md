# Álgebra, cálculo y geometría con Python

Esta práctica de KeepCoding me sirvió para bajar las matemáticas al código: representar conjuntos con repeticiones, descomponer matrices y entender cómo se ajusta una regresión.

**Estado:** cuaderno de formación conservado. Incluye código propio, enunciados y ejemplos de clase. Tiene recursos externos y errores pendientes; no se presenta como una librería matemática validada.

## Recorrido del cuaderno

| Bloque | Qué se trabaja |
| --- | --- |
| Multiconjuntos | Contar elementos repetidos y operar con sus multiplicidades. |
| Descomposición SVD | Entender una matriz a través de otras matrices más sencillas y sus aproximaciones. |
| Regresión y mínimos cuadrados | Ajustar una relación entre variables y compararla con scikit-learn. |
| Descenso del gradiente | Acercarse paso a paso a una solución del ajuste. |
| Similitud entre páginas, opcional | Preparar texto y explorar similitud coseno. |

## Cómo abrirlo

Abre [ALG00-Practica.ipynb](ALG00-Practica.ipynb) en GitHub para leerlo o con Jupyter en una copia local. Los bloques importan `numpy`, `pandas`, `matplotlib`, `scipy`, `scikit-learn`, `beautifulsoup4` y `lxml`, además de herramientas de Python e IPython.

La regresión lee un `train.csv` desde una ruta absoluta de la máquina original. También hay referencias a imágenes y otros recursos que no están en el repositorio. Antes de ejecutar todo, adapta las rutas y consigue los materiales del curso. La parte opcional consulta páginas externas; no se ha vuelto a comprobar su disponibilidad.

El repositorio no fija versiones de dependencias. Las salidas guardadas corresponden a la entrega de aprendizaje; no se han vuelto a producir en esta revisión.

## Qué revisaría hoy

La [revisión técnica](REVISION.md) señala fallos concretos en pertenencia, igualdad y subconjuntos. Son buenos ejemplos de por qué una función que parece sencilla también necesita casos de prueba.

Conservo el cuaderno para que se vea mi proceso. Esta limpieza ordena y explica el trabajo; no atribuye correcciones ni resultados que todavía no se han validado.

[Volver a mi perfil](https://github.com/MGD9).
