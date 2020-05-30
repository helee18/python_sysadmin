#!/usr/bin/env python

import os

# Funcion ejecutar comandos Linux

def terminal(entrada):
    salida = ''
    # Ejecutamos el comando en el terminal
    f = os.popen(entrada)

    # Leemos caracter a caracter y lo guardamos en la variable a devolver
    for i in f.readlines():
        salida += i 
    # Eliminamos el salto de linea
    salida = salida[:-1]
 
    # Devolvemos la variable con la respuesta al comando
    return salida 