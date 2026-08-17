# -*- coding: utf-8 -*-

"""Archivo de ejemplo con 3 errores intencionales detectables por flake8."""


def sumar(a, b):
    resultado=a + b
    mensaje = "este comentario hace que la linea sea demasiado larga a proposito para superar el limite"
    return resultado
