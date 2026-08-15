# -*- coding: utf-8 -*-
"""
Pruebas de pytest para el metodo 'filtrar_vocales' definido en tarea_1.py.

Sigue el mismo formato del archivo de ejemplo entregado por el curso:
una prueba que verifica todos los casos de error y otra que verifica
los casos de exito. El archivo con el codigo (tarea_1.py) debe estar en
la misma carpeta que este archivo de pruebas.
"""

import tarea_1

# ---------------------------------------------------------------------------
# Codigos de retorno esperados (definidos en tarea_1.py)
#   Exito ................................. 0
#   cadena no es un string ................ 1
#   cadena es un string vacio ............. 2
#   cadena contiene caracteres no-letra ... 3
#   cadena con mas de 30 caracteres ....... 4
#   bandera no es un booleano ............. 5
# ---------------------------------------------------------------------------


# Prueba 1
# Verifica todos los casos de error del metodo filtrar_vocales.
def test_casos_error_filtrar_vocales():
    # cadena no es un string (se pasa un entero) -> codigo 1
    estado, res = tarea_1.filtrar_vocales(123, True)
    assert estado == 1
    assert res is None

    # cadena es un string vacio -> codigo 2
    estado, res = tarea_1.filtrar_vocales("", True)
    assert estado == 2
    assert res is None

    # cadena con caracteres que no son letras (numeros) -> codigo 3
    estado, res = tarea_1.filtrar_vocales("Hola123", True)
    assert estado == 3
    assert res is None

    # cadena con mas de 30 caracteres -> codigo 4
    estado, res = tarea_1.filtrar_vocales("a" * 31, True)
    assert estado == 4
    assert res is None

    # bandera que no es un booleano (se pasa un string) -> codigo 5
    estado, res = tarea_1.filtrar_vocales("Hola", "True")
    assert estado == 5
    assert res is None


# Prueba 2
# Verifica los casos de exito del metodo filtrar_vocales.
def test_casos_exito_filtrar_vocales():
    # bandera True -> devuelve solo las vocales, en el mismo orden
    estado, res = tarea_1.filtrar_vocales("Murcielago", True)
    assert estado == 0
    assert res == "uieao"

    # bandera False -> devuelve solo las consonantes, en el mismo orden
    estado, res = tarea_1.filtrar_vocales("Murcielago", False)
    assert estado == 0
    assert res == "Mrclg"
