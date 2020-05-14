#!/usr/bin/env python

# Importamos los modulos y submodulos necesarios
import logging
from telegram.ext import Updater, CommandHandler
import os

# Habilitamos el registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Definimos las funciones
def start(update, context):
    update.message.reply.text(
        'Hello{}',format(update.message.from_user.first_name)
    )

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Introducimos nuestro Token
    updater = Updater('1166829225:AAGl0qJmYnUggGmNvX4RU2a8BQyD1u5FCmE', use_context=True)

    # Definimos los comandos y las funciones a ejecutar
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_error_handler(error)

    # Iniciamos el bot y configuramos que esté pendiente y a la espera de mensajes
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()