#!/usr/bin/env python

# Importamos los modulos y submodulos necesarios
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from auth.auth import token
import os

# Habilitamos el registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

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

# Función para errores

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Función de repetición 

def echo(update, context):
    update.message.reply_text(update.message.text)

# Funciones para comandos

def start(update, context):
    # Confirmamos que se ha iniciado bien con un mensaje de bienvenida
    update.message.reply_text(
        'Welcome to PythonSysadminBot ' + update.message.from_user.first_name
    )

def help(update,context):
    # Listamos todos los comandos
    update.message.reply_text(
        '*Lista de comandos* \n'
        '/start - inicio del bot \n' 
        '/ip - ip del servidor \n', 
        parse_mode= 'Markdown'
    )

def nombre(update,context):
     # Llamamos a la funcion terminal, que ejecuta el comando pasado
    nombre = terminal('hostname')
    # Respondemos al comando con el mensaje
    update.message.reply_text(
        'El nombre del servidor es: \n' + nombre
    ) 

def ip(update,context):
    # Nombre del servidor
    nombre = terminal('hostname')
    # Llamamos a la funcion terminal, que ejecuta el comando pasado
    ip = terminal('hostname -I')
    # Eliminamos el ultimo caracter
    ip = ip[:-1] 
    # Respondemos al comando con el mensaje
    update.message.reply_text(
        'La ip del servidor ' + nombre + ' es: \n' + ip
    ) 

def red(update,context):
    # Nombre del servidor
    nombre = terminal('hostname')
    # Llamamos a la funcion terminal, que ejecuta el comando pasado
    red = terminal('iwgetid')
    # Respondemos al comando con el mensaje
    update.message.reply_text(
        'La red a la que está conectado el servidor ' + nombre + ' es: \n' + red
    )

def particiones(update,context):
    # Nombre del servidor
    nombre = terminal('hostname')
    # Llamamos a la funcion terminal, que ejecuta el comando pasado
    _fdisk = terminal('sudo fdisk -l | grep "Disco"')
    # Respondemos al comando con el mensaje
    update.message.reply_text(
        'Las particiones del servidor ' + nombre + ' son: \n' + _fdisk
    )

def arquitectura(update,context):
    # Nombre del servidor
    nombre = terminal('hostname')
    # Llamamos a la funcion terminal, que ejecuta el comando pasado
    arquitectura = terminal('arch')
    # Respondemos al comando con el mensaje
    update.message.reply_text(
        'La arquitectura del sistema del servidor ' + nombre + ' es: \n' + arquitectura
    )
 
# Funcion principal

def main():
    # Introducimos nuestro Token
    updater = Updater(token, use_context=True)

    # Definimos los comandos y las funciones a ejecutar
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('nombre', nombre))
    updater.dispatcher.add_handler(CommandHandler('ip', ip))
    updater.dispatcher.add_handler(CommandHandler('red', red))
    updater.dispatcher.add_handler(CommandHandler('particiones', particiones))
    updater.dispatcher.add_handler(CommandHandler('arquitectura', arquitectura))

    # Log para errores
    updater.dispatcher.add_error_handler(error)

    # Cuando no entiende el comando de entrada
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Iniciamos el bot y configuramos que esté pendiente y a la espera
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
