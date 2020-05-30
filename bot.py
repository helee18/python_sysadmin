#!/usr/bin/env python

# Importamos los modulos y submodulos necesarios
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from auth import token, ids
from comandos_linux import terminal

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
    # Confirmamos que se ha iniciado bien con un mensaje de bienvenida
    update.message.reply_text(
        'Welcome to PythonSysadminBot ' + update.message.from_user.first_name
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
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def nombre(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Llamamos a la funcion terminal, que ejecuta el comando pasado
        # Nombre del servidor
        nombre = terminal('hostname')

        # Respondemos al comando con el mensaje
        update.message.reply_text(
            'El nombre del servidor es: \n\n' + nombre
        ) 
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def ip(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Llamamos a la funcion terminal, que ejecuta el comando pasado
        # Nombre del servidor
        nombre = terminal('hostname')
        # Llamamos a la funcion terminal, que ejecuta el comando pasado
        # IP del servidor
        ip = terminal('hostname -I')
        # Eliminamos el ultimo caracter
        ip = ip[:-1] 

        # Respondemos al comando con el mensaje
        update.message.reply_text(
            'La ip del servidor ' + nombre + ' es: \n\n' + ip
        ) 
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def red(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Llamamos a la funcion terminal, que ejecuta el comando pasado
        # Nombre del servidor
        nombre = terminal('hostname')
        # Red a la que está conectado el servidor
        red = terminal('iwgetid')

        # Respondemos al comando con el mensaje
        update.message.reply_text(
            'La red a la que está conectado el servidor ' + nombre + ' es: \n\n' + red
        )
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def particiones(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Llamamos a la funcion terminal, que ejecuta el comando pasado
        # Nombre del servidor
        nombre = terminal('hostname')
        # Particiones de disco del servidor
        particiones = terminal('sudo fdisk -l | grep "Disco"')

        # Respondemos al comando con el mensaje
        update.message.reply_text(
            'Las particiones de disco del servidor ' + nombre + ' son: \n\n' + particiones
        )
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def arquitectura(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Llamamos a la funcion terminal, que ejecuta el comando pasado
        # Nombre del servidor
        nombre = terminal('hostname')
        # Arquitectura del servidor
        arquitectura = terminal('arch')

        # Respondemos al comando con el mensaje
        update.message.reply_text(
            'La arquitectura del sistema del servidor ' + nombre + ' es: \n\n' + arquitectura
        )    
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def version(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Llamamos a la funcion terminal, que ejecuta el comando pasado
        # Nombre del servidor
        nombre = terminal('hostname')
        # Version del kernel del servidor
        version = terminal('cat /proc/version')

        # Respondemos al comando con el mensaje
        update.message.reply_text(
            'La versión de Linux del servidor ' + nombre + ' es: \n\n' + version
        )   
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )

def servicios(update,context):
    # Comprobamos si es un usuario autorizado
    if update.message.chat_id in ids:
        # Comprobamos que ha entrado solo un argumento
        if len(context.args) == 1:
            # Declaramos el comando que se tiene que ejecutar
            if 'estado_servicio' in update.message.text:
                # Comando para ver el estado
                comando = '/etc/init.d/' + context.args[0] + ' status | grep "Active"'
            elif 'iniciar_servicio' in update.message.text:
                # Comando para iniciar
                comando = '/etc/init.d/' + context.args[0] + ' start'
            elif 'parar_servicio' in update.message.text:
                # Comando para parar
                comando = '/etc/init.d/' + context.args[0] + ' stop'
            else:
                # Comando para reiniciar
                comando = '/etc/init.d/' + context.args[0] + ' restart'

            # Intentamos reiniciar y si da error lo notificamos
            try: 
                # Llamamos a la funcion terminal, que ejecuta el comando pasado
                respuesta = terminal(comando)

                # Respondemos al comando con el mensaje
                update.message.reply_text(
                    respuesta
                )
            except:
                # Notificamos error
                update.message.reply_text(
                    'Tiene que introducirse el nombre exacto del servicio'
                )
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
    updater.dispatcher.add_handler(CommandHandler('nombre', nombre))
    updater.dispatcher.add_handler(CommandHandler('ip', ip))
    updater.dispatcher.add_handler(CommandHandler('red', red))
    updater.dispatcher.add_handler(CommandHandler('particiones', particiones))
    updater.dispatcher.add_handler(CommandHandler('arquitectura', arquitectura))
    updater.dispatcher.add_handler(CommandHandler('version', version))
    updater.dispatcher.add_handler(CommandHandler('estado_servicio', servicios, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('iniciar_servicio', servicios, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('parar_servicio', servicios, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('reiniciar_servicio', servicios, pass_args=True))

    # Log para errores
    updater.dispatcher.add_error_handler(error)

    # Cuando no entiende el comando de entrada
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Iniciamos el bot y configuramos que esté pendiente y a la espera
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
