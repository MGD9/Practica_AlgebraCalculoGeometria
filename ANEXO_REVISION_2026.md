# Revisión posterior: Matemáticas con Python: volver a los fundamentos

**Fecha: 14/11/2026. Anexo separado de la entrega original.**

Después de retomar esta práctica con más perspectiva y herramientas, he vuelto a revisar cómo la resolví al empezar. Mantengo aquella entrega como parte de mi aprendizaje y recojo aquí una versión posterior que corrige los puntos identificados. Esta revisión se ha preparado con apoyo de IA y con las comprobaciones indicadas al final.

Es una revisión actual. No se atribuye su uso a una fecha anterior ni se presenta como un despliegue o un resultado de trabajo que no se haya comprobado.

## Archivos de esta versión

- [ANEXO_REVISION_2026.py](ANEXO_REVISION_2026.py)

## Qué cambia y por qué

Se revisan las operaciones de multiconjuntos: pertenencia, igualdad, subconjunto con multiplicidades, unión por suma, intersección por mínimo y diferencia por resta. Las funciones devuelven diccionarios nuevos y validan las multiplicidades. Esa decisión evita cambios inesperados sobre la entrada y se explica como parte de esta versión.

Se añaden funciones independientes para aproximación SVD, mínimos cuadrados sin invertir la matriz normal, descenso del gradiente con criterio de convergencia y similitud coseno. Son versiones de referencia de esos bloques, con datos de prueba pequeños. El anexo no descarga páginas ni reconstruye las imágenes o los datasets ausentes del curso.

## Cómo usarla

```sh
python3 -m pip install numpy
python3 ANEXO_REVISION_2026.py --comprobar
```

Las funciones pueden importarse desde el archivo. La unión sigue la convención del enunciado original: sumar las multiplicidades. La similitud de un vector nulo se define como 0 y se declara como convención de esta utilidad.

## Qué se ha comprobado

15 pruebas ejecutadas con Python y NumPy 2.3.5. Incluyen vacíos, elemento ausente, segundo elemento incompatible, distintas multiplicidades, diferencia parcial, conservación de entradas, matrices SVD, regresión con colinealidad, descenso del gradiente y coseno.

**Pendiente:** cualquier extensión que quiera reproducir los gráficos, datos y ejemplos externos del notebook original. Las pruebas del anexo no certifican todas las celdas de la entrega histórica.

## La entrega inicial sigue aquí

Los scripts, notebooks y archivos originales conservan su nombre y contenido. El README y REVISION.md explican sus límites; este anexo ofrece la alternativa. Se puede estudiar la evolución sin borrar el punto de partida.
