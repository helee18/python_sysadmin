#!/usr/bin/env python

# Importamos del modulo telegram.ext dos submodulos
from telegram.ext import Updater, CommandHandler
# Importamos el modulo os
import os

# Definimos las funciones
def hello(update, context):
    update.message.reply.text(
        'Hello{}',format(update.message.from_user.first_name)
    )

# Introducimos nuestro Token
updater = Updater('1166829225:AAGl0qJmYnUggGmNvX4RU2a8BQyD1u5FCmE', use_context=True)

# Definimos los comandos y las funciones a ejecutar
updater.dispatcher.add_handler(CommandHandler('hello', hello))

# Configuramos que esté pendiente y a la espera de mensajes
updater.start_polling()
updater.idle()