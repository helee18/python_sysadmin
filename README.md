<a name="top"></a>

![Python para Sysadmin con Telegram](https://github.com/helee18/python_sysadmin/blob/master/images/titulo.png)
---
[`Telegram`](https://web.telegram.org/), una plataforma de mensajería, tiene la opción de crear bots de todo tipo. Los administradores de sistemas pueden hacer uso de estos bots para manipular o consultar el estado de un servidor creando uno. 

Para ello se puede hacer uso de [`Python`](https://www.python.org/), un lenguaje de programación multiplataforma. Programaremos al bot para que responda a las distintas peticiones que le hagamos. Esto lo haremos desarrollando un script en el que reflejaremos cada mensaje de entrada que recibirá el bot y como responderá este. El script tendremos que ejecutar en un servidor para que el bot funciones y lo ejecutaremos en [`segundo plano`](https://www.atareao.es/como/procesos-en-segundo-plano-en-linux/).
```
$ python3 bot.py &
```

Nos comunicaremos con el bot mediante comandos, estos comienzan por `/` y programaremos al bot para que, según el comando que reciba, realice una función u otra y haga en el servidor lo que nosotros le pidamos o nos muestre la información de este que nos interesa.

<a name="crear"></a>

## Crear un bot de Telegram

El primer paso para crear un bot tenemos que iniciar [`BotFather`](https://telegram.me/BotFather), el bot principal que reconoce una serie de comandos, desde Telegram. Como respuesta, nos devuelve el `token` identificativo de nuestro bot.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather01.jpg" alt="BotFather" width="450"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather02.jpg" alt="start" width="450"/><br>

Creamos un nuevo bot con `/newbot` y le ponemos nombre al bot y al usuario.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather03.jpg" alt="newbot" width="450"/><br>

Desde el BotFather se puede modificar los bots. Por ejemplo, se puede cambiar el nombre con `/setname` y añadir una foto con `/setuserpic`. En cualquier momento podemos mandar el comadno `/help` para ver la lista de comandos que podemos usar dependiendo de lo que queramos hacer.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather04.jpg" alt="setname" width="450"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather05.jpg" alt="setuserpic" width="450"/>

# AÑADIR DESCRIPCIÓN #

[Inicio](#top)<br>

<a name="instalar"></a>

## Instalar python-telegram-bot

<a name="venv"></a>

### Entorno de desarrollo virutal 
Para la gestión de paquetes y programas de python existen unos entornos virtuales de desarrollo. Con estos entorno virtuales, no hace falta tener permisos de administrador para tener estos espacios aislados, directorios, en los que instalar distintas versiones de programas y paquetes.

Para poder crear un entorno virtual para instalar el módulo [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot) primero tenemos que instalar el modulo [`venv`](https://docs.python.org/3/library/venv.html).
```
$ sudo apt-get install python3-venv
```

Después creamos un entorno con le nombre que queramos.
```
$ python3 -m venv [nombre]
```

Activamos el entorno de desarrollo.
```
$ source [nombre]/bin/activate
```

Una vez activamos el entorno de desarrollo virtual estaremos dentro de él, y es donde tenemos que instalar el modulo de [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot), o cualquier otro. Tendremos que ejecutar nuestro script dentro para poder hacer uso de los módulos que instalemos.

Cuando se termine de trabajar dentro del entorno, salimos de este desactivandolo y no tendremos acceso a ninguno de los modulos instalados dentro de él.
```
$ deactivate
```
[Inicio](#top)<br>

<a name="pip"></a>

### [Instalación con pip](https://github.com/helee18/python_sysadmin/blob/master/setup.py)
La forma más fácil y rápida de instalar la librería de [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot) es con el uso de [`pip`](https://pypi.org/project/pip/).
```
$ sudo apt-get install python3-pip
$ pip3 install python-telegram-bot --upgrade
```
[Inicio](#top)<br>

<a name="github"></a>

### [Instalación clonando el repositorio](https://github.com/helee18/python_sysadmin/blob/master/setup2.py)
Otra forma de instalarlo es clonando el repositorio de github.
```
$ git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
$ cd python-telegram-bot/
```

Cuando se intenta instalar puede que de un fallo:
```
$ sudo python3 setup.py install
```
```
python3 setup.py install
Traceback (most recent call last):
  File "setup.py", line 8, in <module>
    from setuptools import setup, find_packages
ModuleNotFoundError: No module named 'setuptools'
```

Por lo que tendremos que instalar manualmente las `setuptools` y después instalarlo:
```
$ sudo apt-get install python3-setuptools
$ sudo python3 setup.py install
```

Durante la instalación aparece lo siguiente:
```
WARNING: The tornado.speedups extension module could not be compiled. No C extensions are essential for Tornado to run, although they do result in significant speed improvements for websockets.
The output above this warning shows how the compilation failed.
```

Esto quiere decir que no se pudo compilar la extensión `tornado.speedups`. Y según el sistema operativo te dice el comando a ejecutar para instalar lo necesario para una mejora de velocidad.
```
$ sudo apt-get install build-essential python-dev
```
[Inicio](#top)<br>

## [Elementos básicos del script del bot](https://github.com/helee18/python_sysadmin/blob/master/ejemplo-bot.py)

<a name="import"></a>

### Importar módulos
Al principio del script importamos los módulos de python necesarios. Los módulos son ficheros que contienen contenido python y almacenan variables y funciones que podemos usar en nuestro script.

En este caso importamos el módulo [`logging`](https://docs.python.org/3/library/logging.html) para el registro y los submódulos [`Updater`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html), [`CommandHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html), [`MessageHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.messagehandler.html) y [`Filters`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.filters.html) de la librería [`telegram.ext`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html) a la que podemos acceder gracias a [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot).

[Inicio](#top)<br>

<a name="logging"></a>

### Logging
Habilitamos el registro del historial de eventos con [`basicConfig`](https://docs.python.org/3/library/logging.html#logging.basicConfig). Con `format` configuramos salga la fecha y hora, el nombre del bot, el nivel de registro y el mensaje que muestra. 

La librería [`logging`](https://docs.python.org/3/library/logging.html) tiene distintos niveles `Debug`, `Info`, `Warning`, `Error` y `Critical` de menos a mayor importancia.

En caso de que no configuremos el nivel, por defecto está configurado para mostrar mensajes de categoría mínima `warning`. Configuramos que el nivel mínimo sea `info` para que muestre también mensajes que no sean algo inesperado, como que el sistema funcione correctamente. 
```
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
```

Para registrar las acciones durante la ejecución del programa haremos uso de la función [`logging.getLogger(nombre del logger)`](https://docs.python.org/3/library/logging.html#logging.getLogger) y como nombre del logger pondremos `__name__` que, en un módulo, es el nombre de este en el espacio de nombres de Python.
```
logger = logging.getLogger(__name__)
```

Después, para el registro de errores definiremos una función en la que haremos uso de `logger.warning`.

[Inicio](#top)<br>

<a name="main"></a>

### Función main
Al final del código, llamamos a la función principal `main`, en la cual tendremos todo el código del bot. Para llamar a la función, comprobamos que el código se está ejecutando en el script principal, y no sea importado en otro. Esto se comprueba comparando que el atributo `__name__` con `__main__` ya que `__name__` adopta el nombre de `__main__` cuando se ejecuta en el script principal o adopta le nombre del módulo importado cuando no es así.
```
if __name__ == '__main__':
    main()
```
[Inicio](#top)<br>

<a name="token"></a>

### Introducción del token
Definimos la función `main` y dentro de esta programamos el script del bot. Lo primero que tenemos que definir el `updater`, donde introducimos nuestro `token`.

Hacemos uso de [`Updater`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html) que es una clase que ayuda al programador a codificar el bot. Recibe actualizaciones de telegram y las manda al [`Dispatcher`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html). El [`Dispatcher`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html) maneja las actualizaciones y las manda a los [`Handlers`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.handler.html).

Añadimos `user_content=True` para usar las nuevas devoluciones basadas en contexto (`context based callbacks`). [`CallbackContext`](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Transition-guide-to-Version-12.0#what-exactly-is-callbackcontext) es un objeto que contiene contexto adicional de update, error o job. Esto almacena chat_data, user_data, job, error y argumentos. Puede producirse un fallo de uso de la antigua API dependiendo de la versión si no se añade, aunque en la versión 13 no hace falta ya que por defecto es `True`.
```
def main():
    updater = Updater('TOKEN', use_context=True)
```

Para mayor seguridad, en el caso de que tengamos un repositorio, se puede crear otro archivo `.py` (auth.py) en el que definamos una variable a la que le asignamos el `token`. Este archivo no lo subiremos al repositorio, en el caso de utilizar el script del bot en otra maquina, tendremos que crear `auth.py` en el mismo directorio en el que esté el script antes de ejecutarlo.
```
token = 'TOKEN'
```

Para poder hacer uso de este, importamos el `token`del archivo `auth`.
```
from auth import token
```

Y en el script del bot, en vez de poner el `token` directamente, solo mencionamos la variable.
```
def main():
    updater = Updater(token, use_context=True)
```
Para que el archivo que tiene esta información no se suba por error a nuestro repositorio, añadiremos un archivo oculto [`.gitignore`](https://github.com/helee18/python_sysadmin/blob/master/.gitignore) en el que añadiremos lo que no queremos que se suba. Junto con otros archivos o carpetas, añadiremos el archivo `auth.py`.
```
bot-venv/
auth.py
```

Subiremos este archivo a nuestro repositorio y después ignorará los archivos que hayamos incluido en este.
```
git add .gitignore
git commit -m "no subir a github"
git push
```
[Inicio](#top)<br>

<a name="inicio"></a>

### Inicio bot y espera
Dentro de la función principal le indicamos al bot que inicie la espera de mensajes por parte de Telegram con [`start_polling()`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html#telegram.ext.Updater.start_polling).
```
    updater.start_polling()
```

También le decimos que se bloquee y se quede a la espera hasta recibir mensajes con [`idle()`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html#telegram.ext.Updater.idle). Esto lo hará hasta que, con Ctrl-C, paremos el bot.
```
    updater.idle()
```
[Inicio](#top)<br>

<a name="recepcion"></a>

### Recepción de comandos
Siempre que queramos configurar un comando, declaramos en la función principal (`main`) un nuevo controlador [`add_handler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html#telegram.ext.Dispatcher.add_handler). Para manejar el comando utilizaremos [`CommandHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html) y dentro tendremos que decir cual es el mensaje de entrada que recibe (el comando) y cual es la función a la que llama. Haremos uso de `updater`, previamente declarado, que nos ayudará a codificar el bot ya que hace referencia al token identificativo.
```
    updater.dispatcher.add_handler(CommandHandler('comando', funcion))
```
[Inicio](#top)<br>

<a name="funciones"></a>

### Funciones de comandos
Fuera de la función principal tenemos que definir la función correspondiente a cada comando, con los parámetros de entrada `update` y `context` y dentro de esta le diremos al bot que tiene que hacer en cada caso.

Cada comando hará una cosa distinta pero todos nos devolverán un mensaje ya sea con información o confirmando que lo que le pedimos se ha realizado.

[`Update`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.update.html) es un objeto que representa una actualización entrate, [`message`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.update.html#telegram.Update.message) se refiere a un mensaje y [`reply_text`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.reply_text) a la respuesta que va a dar el bot, especificada dentro.
```
def funcion(update, context):
    update.message.reply_text(
        'Esta es la respuesta del bot'
    )
```
[Inicio](#top)<br>

<a name="usuarios"></a>

### Control de usuarios
Para poder tener un controlar los usuarios que pueden interactuar con el bot, hacemos una lista con los `ids` de los usuarios a los que autorizamos para consultar o administrar nuestro servidor en el mismo archivo en el que guardamos nuestro `token` (`auth.py`).

Hay que tener en cuenta que los `ids` no se ponen entre comillas porque son datos de tipo `int` y han de guardarse así para que luego podamos consultarlos.
```
ids = [ID1, ID2, ID3]
```

Para poder conocer el `id` de un usuario, tenemos que iniciar el bot [`userinfobot`](https://telegram.me/userinfobot) y este nos dará nuestra información.
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/userinfobot.jpg" alt="start" width="450"/>

Al igual que con el `token` tenemos que importar la lista de `ids`.
```
from auth import token, ids
```

Comprobamos en las funciones de los comandos si el id del usuario que ha mandado el mensaje ([`message.chat_id`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html?highlight=chat_id#telegram.Message.chat_id)) está en la lista con un condicional [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) y el operador [`in`](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations). Y en caso de que no sea un usuario autorizado el bot devolverá un mensaje informando de ello.
```
def funcion(update, context):
    if update.message.chat_id in ids:
        update.message.reply_text(
            'Esta es la respuesta en caso de que si esté autorizado'
        )
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```
[Inicio](#top)<br>

<a name="start"></a>

### Comando `/start`
El primer comando que enviará el usuario al bot al iniciarlo será `/start`. Configuraremos al bot para que tras recibir este comando llame a la función `start`.
```
    updater.dispatcher.add_handler(CommandHandler('start', start))
```

En este caso en la función simplemente devolveremos un mensaje confirmando que ha conectado y funciona. Esto será en el caso de que el usuario sea uno de los usuarios autorizados y su `id` se encuentre en la lista que hemos importado de nuestro archivo `auth.py`.
```
def start(update, context):
    if update.message.chat_id in ids:
        update.message.reply_text(
            'Welcome to PythonSysadminBot ' + update.message.from_user.first_name
        )
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```
[Inicio](#top)<br>

<a name="help"></a>

### Comando `/help`
Para poder recordar la lista de comandos que podemos utilizar en el bot y para que sirve cada uno, definimos el comando `/help`.
```
    updater.dispatcher.add_handler(CommandHandler('help', help))
```

Y en la función vamos añadiendo los comandos que vamos configurando para poder tenerlos en una lista y consultarlo en cualquier momento.

Para poder poner el titulo en negrita (Lista de comandos) le ponemos `*` al principio y al final y despues declaramos que lo lea como si fuese Markdown `parse_mode= 'Markdown'`. Y para introducir saltos te línea, añadimos `\n`.
```
def help(update,context):
    if update.message.chat_id in ids:
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
```
[Inicio](#top)<br>

<a name="echo"></a>

### Comandos no definidos
Definimos una función con la cual se repetirán todos los mensajes o comandos que le mandemos al bot y este no entienda, es decir, que repetirá el mensaje o comando que reciba si no hay una función definida para este.

Utilizaremos [`MessageHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.messagehandler.html) para manejar los mensajes introducidos. Esta clase de handler puede contener texto, archivos multimedia o actualizaciones de estado.

Con [`Filters.text`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.filters.html#telegram.ext.filters.Filters.successful_payment) filtramos la cadena de caracteres que pasamos. Y llamamos a la función `echo`.
```
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
```

Definimos la función y es aquí donde programamos al bot para que repita el mensaje recibido. Con [`update.message.text`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.text) le decimos al bot que lo que tiene que devolver es exactamente el mismo mensaje entrante.
```
def echo(update, context):
    update.message.reply_text(update.message.text)
```
[Inicio](#top)<br>

<a name="error"></a>

### Log de errores
Podemos añadir un controlador de errores en los [`Dispatcher`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html) con [`add_error_handler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html#telegram.ext.Dispatcher.add_error_handler). Dentro llamamos a la función `error` sin definir ningún mensaje o comando de entrada.
```
    updater.dispatcher.add_error_handler(error)
```

Definimos la función en la que hacemos uso de `logger`, previamente definido, y [`warning`](https://docs.python.org/3/library/logging.html#logging.Logger.warning) para el registro de mensajes a este nivel, donde funciona correctamente pero se produce una situación inesperada o se predice un problema futuro.
```
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
```
[Inicio](#top)<br>

<a name="monitorizar"></a>

## [Comandos para monitorizar un servidor](https://github.com/helee18/python_sysadmin/blob/master/bot.py)

<a name="f_terminal"></a>

### [Función para ejecutar comandos en Linux](https://github.com/helee18/python_sysadmin/blob/master/comandos_linux.py)
Para poder interactuar con el sistema, definimos una función cuyo trabajo es ejecutar el comando linux que nosotros le pasemos y devolvernos la respuesta del sistema a este.

#Cuando el bot reciba un comando, dentro de la función de este #comando llamaremos a la función `terminal` la cual ejecutara el #comando linux correspondiente.
#```
#def funcion(update,context):
#    if update.message.chat_id in ids:
#        respuesta_sistema = terminal('comando_linux')
#        update.message.reply_text(respuesta_sistema) 
#```

Esta función la podemos definir en un script separado del resto de forma que se ejecute en un proceso distinto. Esto sirve para que, al ejecutarse un comando, si este tarda en responder no bloquee el bot y este pueda seguir a la escucha de más peticiones.

Para poder llamar a esta función en el script principal del bot [`bot.py`](https://github.com/helee18/python_sysadmin/blob/master/bot.py), tenemos que importarla.
```
from comandos_linux import terminal
```

Definimos la función `terminal` en el script [`comandos_linux`](https://github.com/helee18/python_sysadmin/blob/master/comandos_linux.py) y declaramos una variable vacía que será con la que referenciaremos a lo que muestre el terminal como resultado del comando linux que le pasemos.
```
def terminal(entrada):
    salida = ""
```

Para interactuar con el sistema operativo tenemos que importar al principio del script la librería [`os`](https://docs.python.org/3/library/os.html).
```
import os
```

Hacemos uso del módulo [`os`](https://docs.python.org/3/library/os.html) utilizando [`popen`](https://docs.python.org/3/library/os.html#os.popen), que abre una tubería para la comunicación con el sistema mediante el paso de mensajes. De esta forma se pueden ejecutar los comandos linux que queramos a la vez que se está ejecutando el script. Esto lo guardamos en una variable (`f`).
```
    f = os.popen(entrada)
```

Después utilizamos el método [`readlines()`](https://uniwebsidad.com/libros/python/capitulo-9/metodos-del-objeto-file) para leer las líneas del contenido referenciado con la variable `f` y con un bucle [`for`](https://docs.python.org/3/reference/compound_stmts.html#for) vamos referenciando caracter a caracter en la variable salida, previamente declarada.
```
    for i in f.readlines():
        salida += i 
```

Eliminamos el último caracter, que será el salto de línea o retorno de carro (\n).
```
    salida = salida[:-1]
```

Por último devolvemos la variable con la respuesta para usarla y mostrar la información por la conversación con el bot por Telegram.
```
    return salida
```
[Inicio](#top)<br>

<a name="respuesta"></a>

### Responder con texto o una imagen
Cuando mandamos un comando al bot, este ejecuta el comando linux correspondiente en el terminal con la función `terminal` y nos devuelve la respuesta del sistema. Nos puede interesar que esta respuesta nos la de el bot en forma de mensaje de texto o de imagen.

Para poder decirle al bot de que forma queremos que nos responda, tenemos que configurar una conversación entre el bot y el usuario.

El primer paso es definir un nuevo manejador dentro la función principal, este tendrá dentro la variable `conv_handler` que declararemos encima, también dentro de la función principal, con la estructura de la conversación.
```
    updater.dispatcher.add_handler(conv_handler)
```

Usamos [`ConversationHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html) que es el controlador para mantener una conversación. Para poder usarlo tenemos que importarlo al principio del script junto con el resto de submodulos de la librería [`telegram.ext`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html).
```
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
```
```
    conv_handler = ConversationHandler(
    
    )
```

Lo primero que declaramos dentro del controlador es [`entry_points`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html#telegram.ext.ConversationHandler.entry_points), se trata de una lista en la que establecemos cuales son los comandos que inician la conversación. En este caso añadimos todos los comandos que quieran ejecutar un comando linux en el sistema.
```
        entry_points=[CommandHandler('comando', funcion)],
```

Lo siguiente que declaramos es [`states`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html#telegram.ext.ConversationHandler.states) que es un dictado donde definimos los distintos estados por los que pasa la conversación.
```
        states={
            ESTADO: [ ]
        },
```

El nombre del estado es un objeto que tenemos que declarar al principio del script. Lo haremos con un rango de tanto como estados tengamos. Esto le asignará un valor numérico a cada estado.
```
ESTADO1, ESTADO2 = range(2)
```

En nuestro caso tenemos un solo estado que será `TIPO`.
```
TIPO = range(1)
```

Por último declaramos [`fallbacks`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html#telegram.ext.ConversationHandler.fallbacks) donde definimos el comando que podemos usar en cualquier momento dentro de la conversación. Este llamará a una función en la que simplemente devolveremos [`ConversationHandler.END`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html#telegram.ext.ConversationHandler.END) para salir de la conversación.
```
        fallbacks=[CommandHandler('cancel', cancel)]
```
```
def cancel(update,context):
    return ConversationHandler.END
```

Cuando definimos las funciones de los comandos tenemos que definir una variable global en la que haremos referiencia al comando linux que queremos ejecutar segun el comando que le hayamos mandado al bot.

También declaranmos una variable en la que tendremos la respuesta que nos va a dar posteriormente el bot pero sin los datos que solicitamos del servidor.
```
def funcion(update,context):
    if update.message.chat_id in ids:
        global comando_linux, respuesta
        comando_linux = " "
        respuesta = " "
```

Después hacemos que el bot nos pregunte si queremos recibir la respuesta en modo de texto o imagen. Para esto hacemos que en el espacio del teclado del móvil aparezcan las dos opciones.

Primero tenemos que declarar una variable con las opciones que van a aparecer.
```
        keyboard = [['Texto', 'Imagen']]
```

Después con [`message.reply_text`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.reply_text) le decimos al bot que tiene que responder. Con [`reply_makeup`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.inlinequeryresultgame.html?highlight=reply_markup#telegram.InlineQueryResultGame.reply_markup) configuramos lo que va a aparecer en el teclado. [`ReplyKeyboardMarkup`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html) representa al teclado y dentro establecemos lo que va a aparecer con la variable [`keyboard`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html#telegram.ReplyKeyboardMarkup.keyboard) y con [`one_time_keyboard=True`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html#telegram.ReplyKeyboardMarkup.one_time_keyboard) hacemos que se oculte tras usarlo pero no que desaparezca del todo, eso lo haremos posteriormente.

Para poder usar el módulo [`ReplyKeyboardMarkup`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html) tenemos que importarlo al principio del script.
```
from telegram import ReplyKeyboardMarkup
```
```
        update.message.reply_text(
            '¿Quieres la respuesta en modo texto o en modo imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
```

Por último hacemos que la función devuelva el nombre del estado al que queremos pasar.
```
        return TIPO
```

Dentro del controlador de la conversación, en el estado, definimos dos manejadores de mensajes [`MessageHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.messagehandler.html) en los que filtraremos los dos mensajes que pueden introducirse y la función a la que llamamos segun el mensaje. Para filtrar el mensaje usamos [`Filters.regex`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.filters.html?highlight=regex#telegram.ext.filters.Filters.regex) que nos permite filtrar el texto de entrada con patrones, en nuestro caso haremos uso de `^` y `$` para referirnos que empieza y acaba la cadena así.
```
        states={
            TIPO: [MessageHandler(Filters.regex('^Texto$'), texto),
                   MessageHandler(Filters.regex('^Imagen$'), imagen)]
        },
```

<a name="texto"></a>

#### Responder con texto

Si lo que hemos introducido es `Texto` llamaremos a la función `texto` donde llamamos a la función `terminal` le pasamos como parametro el comando linux previamente estalecido en la función del comando que introdujimos. Lo que devuelva la función `terminal` (la respuesta del terminal) lo "guardamos" en una variable.
```
def texto(update,context):
    respuesta_sistema = terminal(comando_linux)
```

Programamos al bot para que responda haciendo uso de la variable `respuesta_sistema` y la variable `respuesta` declarada en la función del comando.
```
    update.message.reply_text(respuesta + '\n' + respuesta_sistema)
```

Por último salimos de la conversación devolviendo [`ConversationHandler.END`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html#telegram.ext.ConversationHandler.END).
```
    return ConversationHandler.END
```

<a name="imagen"></a>

#### Responder con imagen

# CUANDO ELIGES IMAGEN
Para poder devolver la respuesta con una imagen, tenemos que instalar [`ImageMagick`](https://imagemagick.org/index.php) que hará posible guardar la respuesta y además seleccionar la tipografía y los colores.
```
$ sudo apt-get install imagemagick
```

# EXPLICAR PARTE IMAGEN

[`bot.send_photo`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.bot.html?highlight=photo#telegram.Bot.send_photo)

[Inicio](#top)<br>