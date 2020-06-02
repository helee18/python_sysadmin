#!/usr/bin/env python

import os

# Funcion ejecutar comandos Linux y devolver texto

def terminal_texto(entrada):
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

# Funcion ejecutar comandos Linux y devolver imagen

def terminal_imagen(entrada):
    # Borramos la imagen si existe
    if os.path.exists('./images/image.png'): 
        os.popen('./images/image.png')

    # Añadimos el conversor a imagen al comando
    entrada = entrada + ' | convert -font Courier -pointsize 50 -fill white -background black label:@- ./images/image.png'
    
    # Ejecutamos el comando en el terminal
    os.popen(entrada)