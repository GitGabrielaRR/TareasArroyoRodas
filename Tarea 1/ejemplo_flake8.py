# -*- coding: utf-8 -*-

"""Archivo de ejemplo con 3 errores intencionales detectables por flake8."""


def sumar(a, b):
    resultado = a + b
    mensaje = "El resultado de la suma es: " + str(resultado)
    print(mensaje)
    return resultado
