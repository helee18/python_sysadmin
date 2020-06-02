#!/usr/bin/env python

# Importamos los modulos y submodulos necesarios
import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from auth import token, ids
from comandos_linux import terminal_texto, terminal_imagen

# Habilitamos el registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Declaramos el objeto estado de la conversacion
TIPO, TIPO_SERVICIOS = range(2)

# Función para errores

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Función de repetición 

def echo(update, context):
    update.message.reply_text(update.message.text)

# Funciones ejecutar comandos linux

def texto(update,context):
    # Llamamos a la funcion terminal, que ejecuta el comando pasado
    respuesta_sistema = terminal_texto(comando_linux)

    # Respondemos al comando con el mensaje
    update.message.reply_text(
        respuesta + '\n\n' + respuesta_sistema,
        reply_markup=ReplyKeyboardRemove()
    )

    # Terminamos la conversación
    return ConversationHandler.END

def imagen(update,context):
    # Llamamos a la funcion terminal, que ejecuta el comando pasado
    terminal_imagen(comando_linux)

    # Respondemos con la imagen
    update.message.reply_text(
        respuesta,
        reply_markup=ReplyKeyboardRemove()
    )
    update.message.bot.send_photo(
        chat_id=update.message.chat_id, 
        photo=open('./images/image.png', 'rb')
    )

    # Terminamos la conversación
    return ConversationHandler.END

# Funciones ejecutar comandos linux para servicios

def texto_servicios(update,context):
    try:
        # Llamamos a la funcion terminal, que ejecuta el comando pasado
        respuesta_sistema = terminal_texto(comando_linux)

        # Respondemos al comando con el mensaje
        update.message.reply_text(
            respuesta + '\n\n' + respuesta_sistema,
            reply_markup=ReplyKeyboardRemove()
        )
    except:
        # Notificamos error
        update.message.reply_text(
            'Tiene que introducirse el nombre exacto del servicio'
        )
    finally:
        # Terminamos la conversación
        return ConversationHandler.END

def imagen_servicios(update,context):
    try:
        # Llamamos a la funcion terminal, que ejecuta el comando pasado
        terminal_imagen(comando_linux)

        # Respondemos con la imagen
        update.message.reply_text(
            respuesta,
            reply_markup=ReplyKeyboardRemove()
        )
        update.message.bot.send_photo(
            chat_id=update.message.chat_id, 
            photo=open('./images/image.png', 'rb')
        )
    except:
        # Notificamos error
        update.message.reply_text(
            'Tiene que introducirse el nombre exacto del servicio'
        )
    finally:
        # Terminamos la conversación
        return ConversationHandler.END

# Funcion para terminar la conversacion

def cancel(update,context):
    return ConversationHandler.END

# Funciones para comandos

def start(update, context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Confirmamos que se ha iniciado bien con un mensaje de bienvenida
        update.message.reply_text(
            'Welcome to PythonSysadminBot ' + update.message.from_user.first_name
        )
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def help(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Listamos todos los comandos
        update.message.reply_text(
            '*Lista de comandos* \n\n'
            '/start - inicio del bot \n' 
            '/ip - ip del servidor \n', 
            parse_mode= 'Markdown'
        )
    else:
        # Si no es un usuario autorizado
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def nombre(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Declaramos las variable globales
        global comando_linux, respuesta
        # Definimos el comando linux que queremos ejecutar
        comando_linux = 'hostname'
        # Preparamos la respuesta
        respuesta = 'El nombre del servidor es: '

        # Preguntamos y cambiamos el teclado por las opciones
        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        # Devolvemos el estado de la conversacion al que pasamos
        return TIPO
    else:
        # Si no es un usuario autorizado
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def ip(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Declaramos las variable globales
        global comando_linux, respuesta
        # Definimos el comando linux que queremos ejecutar
        comando_linux = 'hostname -I'
        # Preparamos la respuesta
        respuesta = 'La ip del servidor ' + terminal_texto('hostname') + ' es: '

        # Preguntamos y cambiamos el teclado por las opciones
        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        # Devolvemos el estado de la conversacion al que pasamos
        return TIPO
    else:
        # Si no es un usuario autorizado
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def red(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Declaramos las variable globales
        global comando_linux, respuesta
        # Definimos el comando linux que queremos ejecutar
        comando_linux = 'iwgetid'
        # Preparamos la respuesta
        respuesta = 'La red a la que está conectado el servidor ' + terminal_texto('hostname') + ' es: '

        # Preguntamos y cambiamos el teclado por las opciones
        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        # Devolvemos el estado de la conversacion al que pasamos
        return TIPO
    else:
        # Si no es un usuario autorizado
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def espacio(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Declaramos las variable globales
        global comando_linux, respuesta
        # Definimos el comando linux que queremos ejecutar
        comando_linux = 'df -h'
        # Preparamos la respuesta
        respuesta = 'El espacio del servidor ' + terminal_texto('hostname') + ' es: '

        # Preguntamos y cambiamos el teclado por las opciones
        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        # Devolvemos el estado de la conversacion al que pasamos
        return TIPO
    else:
        # Si no es un usuario autorizado
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def arquitectura(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Declaramos las variable globales
        global comando_linux, respuesta
        # Definimos el comando linux que queremos ejecutar
        comando_linux = 'arch'
        # Preparamos la respuesta
        respuesta = 'La arquitectura del sistema del servidor ' + terminal_texto('hostname') + ' es: '

        # Preguntamos y cambiamos el teclado por las opciones
        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        # Devolvemos el estado de la conversacion al que pasamos
        return TIPO
    else:
        # Si no es un usuario autorizado
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def version(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Declaramos las variable globales
        global comando_linux, respuesta
        # Definimos el comando linux que queremos ejecutar
        comando_linux = 'cat /proc/version'
        # Preparamos la respuesta
        respuesta = 'La versión de Linux del servidor ' + terminal_texto('hostname') + ' es: '

        # Preguntamos y cambiamos el teclado por las opciones
        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        # Devolvemos el estado de la conversacion al que pasamos
        return TIPO
    else:
        # Si no es un usuario autorizado
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def servicios(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Comprobamos que ha entrado solo un argumento
        if len(context.args) == 1:
            # Declaramos la variable global para el comando
            global comando_linux

            # Declaramos el comando que se tiene que ejecutar
            if 'estado_servicio' in update.message.text:
                # Comando para ver el estado
                comando_linux = '/etc/init.d/' + context.args[0] + ' status | grep "Active"'
            elif 'iniciar_servicio' in update.message.text:
                # Comando para iniciar
                comando_linux = '/etc/init.d/' + context.args[0] + ' start'
            elif 'parar_servicio' in update.message.text:
                # Comando para parar
                comando_linux = '/etc/init.d/' + context.args[0] + ' stop'
            else:
                # Comando para reiniciar
                comando_linux = '/etc/init.d/' + context.args[0] + ' restart'
            
            # Preguntamos y cambiamos el teclado por las opciones
            keyboard = [['Texto', 'Imagen']]
            update.message.reply_text(
                '¿Quieres la respuesta en texto o en imagen?',
                reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
            )
            
            # Devolvemos el estado de la conversacion al que pasamos
            return TIPO_SERVICIOS
        else:
            # En caso de que no se pase un argumento, notificarlo
            update.message.reply_text(
                'Se debe especificar el servicio.\n\n'
                'Ejemplo:\n/reiniciar_servicio apache2'
            ) 
    else:
        # Si no es un usuario autorizado
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

# Funcion principal

def main():
    # Introducimos nuestro Token
    updater = Updater(token, use_context=True)

    # Definimos los comandos y las funciones a ejecutar
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    # Definimos la conversación para respuestas de imagen o texto
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('nombre', nombre),
                      CommandHandler('ip', ip),
                      CommandHandler('red', red),
                      CommandHandler('espacio', espacio),
                      CommandHandler('arquitectura', arquitectura),
                      CommandHandler('version', version),
                      CommandHandler('estado_servicio', servicios, pass_args=True),
                      CommandHandler('iniciar_servicio', servicios, pass_args=True),
                      CommandHandler('parar_servicio', servicios, pass_args=True),
                      CommandHandler('reiniciar_servicio', servicios, pass_args=True)],
                      
        states={
            TIPO: [MessageHandler(Filters.regex('^Texto$'), texto),
                   MessageHandler(Filters.regex('^Imagen$'), imagen)],
            
            TIPO_SERVICIOS: [MessageHandler(Filters.regex('^Texto$'), texto_servicios),
                             MessageHandler(Filters.regex('^Imagen$'), imagen_servicios)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    updater.dispatcher.add_handler(conv_handler)

    # Log para errores
    updater.dispatcher.add_error_handler(error)

    # Cuando no entiende el comando de entrada
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Iniciamos el bot y configuramos que esté pendiente y a la espera
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()