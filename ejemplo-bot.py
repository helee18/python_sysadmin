#!/usr/bin/env python

# Importamos los modulos y submodulos necesarios
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from auth import token, ids

# Habilitamos el registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Función para errores

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Función de repetición 

def echo(update, context):
    update.message.reply_text(update.message.text)

# Funciones para comandos

def start(update, context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Confirmamos que se ha iniciado bien con un mensaje de bienvenida
        update.message.reply_text(
            'Welcome to PythonSysadminBot ' + update.message.from_user.first_name
        )
    else:
        # Si no es un usuario autorizado
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def help(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Listamos todos los comandos
        update.message.reply_text(
            '*Lista de comandos* \n\n'
            '/start - inicio del bot \n', 
            parse_mode= 'Markdown'
        )
    else:
        # Si no es un usuario autorizado
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def main():
    # Introducimos nuestro Token
    updater = Updater(token, use_context=True)

    # Definimos los comandos y las funciones a ejecutar
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    # Log para errores
    updater.dispatcher.add_error_handler(error)

    # Cuando no entiende el comando de entrada
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Iniciamos el bot y configuramos que esté pendiente y a la espera de mensajes
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    