# -*- coding: utf-8 -*-
"""
Pruebas de pytest para los metodos 'filtrar_vocales' y 'encontrar_extremos'
definidos en tarea_1.py.

Sigue el mismo formato del archivo de ejemplo entregado por el curso e
incorpora aleatorizacion con las librerias 'random' y 'string' para probar
los metodos con muchas entradas distintas y no solo con valores fijos.
El archivo con el codigo (tarea_1.py) debe estar en la misma carpeta.
"""

import tarea_1_solution as tarea_1
import random
import string

# ---------------------------------------------------------------------------
# Codigos de retorno esperados de filtrar_vocales (definidos en tarea_1.py)
#   Exito ................................. 0
#   cadena no es un string ................ 1
#   cadena es un string vacio ............. 2
#   cadena contiene caracteres no-letra ... 3
#   cadena con mas de 30 caracteres ....... 4
#   bandera no es un booleano ............. 5
#
# Codigos de retorno esperados de encontrar_extremos (definidos en tarea_1.py)
#   Exito ................................... 0
#   la entrada no es una lista ............. -10
#   un elemento no es int/float ........... -20
#   la lista esta vacia ................... -30
#   la lista tiene mas de 15 elementos .... -40
# ---------------------------------------------------------------------------

# Conjunto de vocales usado para calcular el resultado esperado.
VOCALES = "aeiouAEIOU"


def cadena_aleatoria(largo):
    """Genera una cadena aleatoria formada solo por letras del abecedario."""
    return "".join(random.choice(string.ascii_letters) for _ in range(largo))


def lista_aleatoria(largo):
    """Genera una lista de numeros aleatorios (int o float mezclados)."""
    lista = []
    for _ in range(largo):
        if random.choice([True, False]):
            lista.append(random.randint(-1000, 1000))
        else:
            lista.append(random.uniform(-1000, 1000))
    return lista


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


# Prueba 3
# Verifica todos los casos de error del metodo encontrar_extremos.
def test_casos_error_encontrar_extremos():

    # la entrada no es una lista: se prueba con un valor no-lista -> codigo -10
    no_lista = random.choice([random.randint(1, 1000), "abc", 3.5, (1, 2)])
    estado, minimo, maximo = tarea_1.encontrar_extremos(no_lista)
    assert estado == -10
    assert minimo is None
    assert maximo is None

    # un elemento no es int/float: se inserta un elemento invalido -> codigo -20
    lista_invalida = lista_aleatoria(random.randint(1, 5))
    elemento_invalido = random.choice(["x", None, True, [1]])
    lista_invalida.insert(
        random.randint(0, len(lista_invalida)), elemento_invalido)
    estado, minimo, maximo = tarea_1.encontrar_extremos(lista_invalida)
    assert estado == -20
    assert minimo is None
    assert maximo is None

    # la lista esta vacia -> codigo -30
    estado, minimo, maximo = tarea_1.encontrar_extremos([])
    assert estado == -30
    assert minimo is None
    assert maximo is None

    # la lista tiene mas de 15 elementos (largo aleatorio 16..30) -> codigo -40
    estado, minimo, maximo = tarea_1.encontrar_extremos(
        lista_aleatoria(random.randint(16, 30)))
    assert estado == -40
    assert minimo is None
    assert maximo is None


# Prueba 4
# Verifica los casos de exito del metodo encontrar_extremos usando una
# lista aleatoria valida y comparando contra el minimo y maximo esperados.
def test_casos_exito_encontrar_extremos():
    # lista valida: solo numeros y con un largo aleatorio entre 1 y 15.
    lista = lista_aleatoria(random.randint(1, 15))

    estado, minimo, maximo = tarea_1.encontrar_extremos(lista)
    assert estado == 0
    assert minimo == min(lista)
    assert maximo == max(lista)
