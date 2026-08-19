# -*- coding: utf-8 -*-
"""
Tarea 1 - MT-7003 Microprocesadores y microcontroladores
Metodo 1: filtrar_vocales
Metodo 2: encontrar_extremos

Este archivo contiene la implementacion del primer y segundo metodo solicitado
en la seccion practica de la tarea.
"""

# ---------------------------------------------------------------------------
# Codigos de error / exito (cada uno es unico)
#
# NOTA:
#   Los valores coinciden con los que espera el archivo de pruebas oficial
#   "tarea_1_testing.py" entregado por el curso. Se dejan centralizados aqui
#   para facilitar su mantenimiento.
# ---------------------------------------------------------------------------
# Codigos de retorno generales
EXITO = 0               # La funcion se ejecuto correctamente

# Codigos de error de filtrar_vocales
ERR_NO_STRING = -100    # 'cadena' no es un string
ERR_NO_LETRAS = -200    # 'cadena' contiene caracteres que no son letras
ERR_VACIO = -300        # 'cadena' es un string vacio
ERR_MUY_LARGO = -400    # 'cadena' tiene mas de 30 caracteres
ERR_BANDERA = -500      # 'bandera' no es un booleano (True/False)

# Codigos de error de encontrar_extremos
ERROR_NO_LISTA = -600            # La entrada recibida no es una lista.
ERROR_ELEMENTO_NO_NUMERO = -700  # Al menos un elemento que no es int o float.
ERROR_LISTA_VACIA = -800         # La lista recibida no contiene elementos.
ERROR_MAS_DE_15 = -900           # Contiene más de los 15 elementos permitidos.


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

    # a. Verificar que 'cadena' sea un string.
    if not isinstance(cadena, str):
        return ERR_NO_STRING, None

    # c. Verificar que 'cadena' no sea un string vacio.
    #    (Se revisa antes que "solo letras" porque "" no tiene letras.)
    if cadena == "":
        return ERR_VACIO, None

    # b. Verificar que 'cadena' solo contenga letras del abecedario.
    if not cadena.isalpha():
        return ERR_NO_LETRAS, None

    # d. Verificar que 'cadena' no sea mayor a 30 caracteres.
    if len(cadena) > 30:
        return ERR_MUY_LARGO, None

    # e. Verificar que 'bandera' sea un booleano (True o False).
    if not isinstance(bandera, bool):
        return ERR_BANDERA, None

    # Conjunto de vocales (minusculas y mayusculas) usado para el filtrado.
    vocales = "aeiouAEIOU"

    # f. Si la bandera es True -> devolver solo las vocales.
    # g. Si la bandera es False -> devolver solo las consonantes.
    #    En ambos casos se conserva el orden original de aparicion.
    if bandera:
        filtrado = "".join(letra for letra in cadena if letra in vocales)
    else:
        filtrado = "".join(letra for letra in cadena if letra not in vocales)

    # h/i. Ejecucion correcta: se devuelve el codigo de exito y la cadena.
    return EXITO, filtrado


def encontrar_extremos(lista_numeros):
    """Obtiene el valor minimo y maximo de una lista numerica.

    Parametros:
        lista_numeros: Lista de numeros enteros o flotantes con
        un maximo de 15 elementos.

    Retorna:
        Una tupla formada por el codigo de estado, valor minimo
        y valor maximo. En caso de error, los dos ultimos valores
        son None.
    """

    # Verifica que el parametro recibido sea una lista.
    if not isinstance(lista_numeros, list):
        return ERROR_NO_LISTA, None, None

    # Verifica que todos los elementos sean numeros.
    for numero in lista_numeros:
        if isinstance(numero, bool):
            return ERROR_ELEMENTO_NO_NUMERO, None, None

        if not isinstance(numero, (int, float)):
            return ERROR_ELEMENTO_NO_NUMERO, None, None

    # Verifica que la lista no este vacia.
    if len(lista_numeros) == 0:
        return ERROR_LISTA_VACIA, None, None

    # Verifica que la lista tenga como maximo 15 elementos.

    if len(lista_numeros) > 15:
        return ERROR_MAS_DE_15, None, None

    # Una vez superadas todas las validaciones,
    # se obtienen los extremos de la lista.
    valor_minimo = min(lista_numeros)
    valor_maximo = max(lista_numeros)

    return EXITO, valor_minimo, valor_maximo
