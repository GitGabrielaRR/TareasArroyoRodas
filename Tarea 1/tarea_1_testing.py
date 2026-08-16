# -*- coding: utf-8 -*-
"""
Pruebas de pytest para el metodo 'filtrar_vocales' definido en tarea_1.py.

Sigue el mismo formato del archivo de ejemplo entregado por el curso e
incorpora aleatorizacion con las librerias 'random' y 'string' para probar
el metodo con muchas entradas distintas y no solo con valores fijos.
El archivo con el codigo (tarea_1.py) debe estar en la misma carpeta.
"""

import tarea_1
import random
import string

# ---------------------------------------------------------------------------
# Codigos de retorno esperados (definidos en tarea_1.py)
#   Exito ................................. 0
#   cadena no es un string ................ 1
#   cadena es un string vacio ............. 2
#   cadena contiene caracteres no-letra ... 3
#   cadena con mas de 30 caracteres ....... 4
#   bandera no es un booleano ............. 5
# ---------------------------------------------------------------------------

# Conjunto de vocales usado para calcular el resultado esperado.
VOCALES = "aeiouAEIOU"


def cadena_aleatoria(largo):
    """Genera una cadena aleatoria formada solo por letras del abecedario."""
    return "".join(random.choice(string.ascii_letters) for _ in range(largo))


# Prueba 1
# Verifica todos los casos de error del metodo filtrar_vocales.
def test_casos_error_filtrar_vocales():
    # cadena no es un string: se prueba con un numero aleatorio -> codigo 1
    numero = random.randint(1, 1000)
    estado, res = tarea_1.filtrar_vocales(numero, True)
    assert estado == 1
    assert res is None

    # cadena es un string vacio -> codigo 2
    estado, res = tarea_1.filtrar_vocales("", True)
    assert estado == 2
    assert res is None

    # cadena con un caracter que no es letra (un digito aleatorio) -> codigo 3
    digito = random.choice(string.digits)
    estado, res = tarea_1.filtrar_vocales(cadena_aleatoria(5) + digito, True)
    assert estado == 3
    assert res is None

    # cadena con mas de 30 caracteres (largo aleatorio 31..50) -> codigo 4
    estado, res = tarea_1.filtrar_vocales(
        cadena_aleatoria(random.randint(31, 50)), True)
    assert estado == 4
    assert res is None

    # bandera que no es booleano (valor no-bool aleatorio) -> codigo 5
    bandera_invalida = random.choice(["True", 1, 0, None, 3.5])
    estado, res = tarea_1.filtrar_vocales(
        cadena_aleatoria(5), bandera_invalida)
    assert estado == 5
    assert res is None


# Prueba 2
# Verifica los casos de exito del metodo filtrar_vocales usando una
# cadena aleatoria valida y comparando contra el resultado esperado.
def test_casos_exito_filtrar_vocales():
    # cadena valida: solo letras y con un largo aleatorio entre 1 y 30.
    cadena = cadena_aleatoria(random.randint(1, 30))

    # bandera True -> debe devolver solo las vocales, en el mismo orden.
    esperado_vocales = "".join(c for c in cadena if c in VOCALES)
    estado, res = tarea_1.filtrar_vocales(cadena, True)
    assert estado == 0
    assert res == esperado_vocales

    # bandera False -> debe devolver solo las consonantes, en el mismo orden.
    esperado_consonantes = "".join(c for c in cadena if c not in VOCALES)
    estado, res = tarea_1.filtrar_vocales(cadena, False)
    assert estado == 0
    assert res == esperado_consonantes
