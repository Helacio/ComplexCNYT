# Librería de Números Complejos.
Se realizan las operaciones básicas sobre números complejos.
1. Suma.
2. Producto.
3. Resta.
4. División.
5. Módulo.
6. Conjugado.
7. Conversión entre coordenadas polar y cartesiana.
8. Retornar la fase de un número complejo.

Tenga en cuenta que algunas de las funciones mencionadas depende de la liberia math para facilitar operaciones.


## Libreria:
Tenga en cuenta que el funcionamiento del código depende de las tuplas "c1" y "c2" de la forma (a, b), dónde **a** representa la parte real y **b** la parte imaginaria.
Adicionalmente, hay funciones dentro de la libreria "complejos" las cuales tiene como entrada un solo parametro, tal como es el caso de modulo:
```python
def modulo(c1):
    d = ((c1[0] ** 2) + (c1[1] ** 2))** 0.5
    return d
```

## Prueba:
Este archivo toma como tuplas c1 = (3, -8) y c2 = (4, 6).

Tenga en cuenta que se tomaron algunos valores con más de 5 cifras decimales.
```python
resp4 = lib.modulo(c1)
if resp4 == 8.54400374531753:
    passed += 1
else:
    failed += 1
```