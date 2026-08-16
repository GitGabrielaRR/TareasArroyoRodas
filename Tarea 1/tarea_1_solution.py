# -*- coding: utf-8 -*-
"""
Tarea 1 - MT-7003 Microprocesadores y microcontroladores
Metodo 1: filtrar_vocales

Este archivo contiene la implementacion del primer metodo solicitado.
"""

# ---------------------------------------------------------------------------
# Codigos de error / exito (cada uno es unico)
#
# NOTA IMPORTANTE:
#   El archivo de pruebas "tarea_1_testing.py" define los valores exactos
#   que se esperan para cada codigo de error. Como no se dispuso de ese
#   archivo al escribir este codigo, se eligieron valores unicos y se
#   dejaron centralizados aqui para que sea facil ajustarlos y hacerlos
#   coincidir con los que espere la prueba.
# ---------------------------------------------------------------------------
EXITO = 0               # La funcion se ejecuto correctamente
ERR_NO_STRING = 1       # 'cadena' no es un string
ERR_VACIO = 2           # 'cadena' es un string vacio
ERR_NO_LETRAS = 3       # 'cadena' contiene caracteres que no son letras
ERR_MUY_LARGO = 4       # 'cadena' tiene mas de 30 caracteres
ERR_BANDERA = 5         # 'bandera' no es un booleano (True/False)


def filtrar_vocales(cadena, bandera):
    """
    Filtra las vocales o las consonantes de una cadena de texto.

    Parametros de entrada:
        cadena  (str)  : texto a filtrar. Solo debe contener letras del
                         abecedario, no puede estar vacio y no puede tener
                         mas de 30 caracteres.
        bandera (bool) : si es True se devuelven solo las vocales;
                         si es False se devuelven solo las consonantes.

    Valores de salida (siempre se devuelven DOS valores en este orden):
        codigo (int)   : codigo de error o de exito segun el resultado.
        filtrado (str) : cadena con las vocales o consonantes filtradas.
                         En caso de error este valor es None.
    """

    # Verificar que 'cadena' sea un string.
    if not isinstance(cadena, str):
        return ERR_NO_STRING, None

    # Verificar que 'cadena' no sea un string vacio.
    # (Se revisa antes que "solo letras" porque "" no tiene letras.)
    if cadena == "":
        return ERR_VACIO, None

    # Verificar que 'cadena' solo contenga letras del abecedario.
    if not cadena.isalpha():
        return ERR_NO_LETRAS, None

    # Verificar que 'cadena' no sea mayor a 30 caracteres.
    if len(cadena) > 30:
        return ERR_MUY_LARGO, None

    # Verificar que 'bandera' sea un booleano (True o False).
    if not isinstance(bandera, bool):
        return ERR_BANDERA, None

    # Conjunto de vocales (minusculas y mayusculas) usado para el filtrado.
    vocales = "aeiouAEIOU"

    # Si la bandera es True -> devolver solo las vocales.
    # Si la bandera es False -> devolver solo las consonantes.
    # En ambos casos se conserva el orden original de aparicion.
    if bandera:
        filtrado = "".join(letra for letra in cadena if letra in vocales)
    else:
        filtrado = "".join(letra for letra in cadena if letra not in vocales)

    # Ejecucion correcta: se devuelve el codigo de exito y la cadena.
    return EXITO, filtrado
