<a name="top"></a>

![Python para Sysadmin con Telegram](https://github.com/helee18/python_sysadmin/blob/master/images/titulo.png)
---
[`Telegram`](https://web.telegram.org/), una plataforma de mensajeria, tiene la opción de crear bots de todo tipo. Los administradores de sistemas pueden hacer uso de estos bots para manipular o consultar el estado de un servidor creando uno. 

Para ello se puede hacer uso de [`Python`](https://www.python.org/), un lenguaje de programación multiplataforma. Programaremos al bot para que responda a las distintas peticiones que le hagamos. Esto lo haremos desarrollando un script en el que reflejaremos cada mensaje de entrada que recibirá el bot y como responderá este. El script tendremos que ejecutar en un servidor para que el bot funciones y lo ejecutaremos en segundo plano.
```
$ python3 bot.py &
```

Nos comunicaremos con el bot mediante comandos, estos comienzan por `/` y programaremos al bot para que, segun el comando que reciba, realice una función u otra y haga en el servidor lo que nosotros le pidamos o nos muestre la información de este que nos interesa.

- [`Crear un bot de Telegram`](#crear)
- [`Instalar python-telegram-bot`](#instalar)
    - [`Entorno de desarrollo virutal`](#venv)
    - [`Instalación con pip`](#pip)
    - [`Instalación clonando el repositorio`](#github)
- [`Elementos básicos del script del bot`](#basicos)
    - [`Importar módulos`](#import)
    - [`Logging`](#logging)
    - [`Función main`](#main)
    - [`Introducción del token`](#token)
    - [`Inicio bot y espera`](#espera)
    - [`Comando /start`](#start)
    - [`Comando /help`](#help)
    - [`Comandos no definidos`](#echo)
    - [`Log de errores`](#error)
- [`Comandos para monitorizar un servidor`](#monitorizar)
    - [`Función para ejecutar comandos en Linux`](#f_terminal)
    - [`Comando /nombre`](#nombre)
    - [`Comando /ip`](#ip)
    - [`Comando /red`](#red)
    - [`Comando /particines`](#particiones)
    - [`Comando /arquitectura`](#arquitectura)
    - [`Comando /version`](#version)
    - [`Comandos /estado_servicio, /iniciar_servicio, /parar_servicio y /reiniciar_servicio`](#servicios)

<br>

<a name="crear"></a>

## Crear un bot de Telegram

El primer paso para crear un bot iniciar **BotFather**, el bot principal que reconoce una serie de comandos, desde Telegram. Como respuesta, nos devuelve el `token` identificativo de nuestro bot.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather01.jpg" alt="BotFather" width="450"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather02.jpg" alt="start" width="450"/><br>

Creamos un nuevo bot con `/newbot` y le ponemos nombre al bot y al usuario.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather03.jpg" alt="newbot" width="450"/><br>

Desde el BotFather se puede modificar los bots. Por ejemplo, se puede cambiar el nombre con `/setname` y añadir una foto con `/setuserpic`. En cualquier momento podemos mandar el comadno `/help` para ver la lista de comandos que podemos usar dependiendo de lo que queramos hacer.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather04.jpg" alt="setname" width="450"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather05.jpg" alt="setuserpic" width="450"/>

[Inicio](#top)<br>

<a name="instalar"></a>

## Instalar python-telegram-bot

<a name="venv"></a>

### Entorno de desarrollo virutal 
Para instalar el modulo `python-telegram-bot` utilizamos un entorno de desarrollo virtual, el cual permite gestionar módulos de python en un entorno aislado, un directorio, sin tener permisos de administrador.

Primero tendremos que instalar de modulo `venv` que es el que nos permitira crear el entorno virtual.
```
$ sudo apt-get install python3-venv
```

Después creamos un enterno, al que le ponemos un nombre.
```
$ python3 -m venv [nombre]
```

Activamos el entorno de desarollo.
```
$ source [nombre]/bin/activate
```

Una vez activamos en entorno de desarrollo virtual estaremos dentro de él, y es donde tenemos que instalar el modulo de pythom-telegram-bot, o cualquier otro.

Cuando se termine de trabajar dentro del entorno, salimos de este desactivandolo y no tendremos acceso a ninguno de los modulos instalados dentro de este.
```
$ deactivate
```

<a name="pip"></a>

### [Instalación con pip](https://github.com/helee18/python_sysadmin/blob/master/setup.py)
Instalamos [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot) que presenta una serie de clases de alto nivel para hacer el desarrollo de bots mas facil.
```
$ sudo apt-get install python3-pip
$ pip3 install python-telegram-bot --upgrade
```

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

Por lo que tendremos que instalar manualmente las `setuptools` y después intalarlo:
```
$ sudo apt-get install python3-setuptools
$ sudo python3 setup.py install
```

Durante la instalación aparece lo siguiente:
```
WARNING: The tornado.speedups extension module could not be compiled. No C extensions are essential for Tornado to run, although they do result in significant speed improvements for websockets.
The output above this warning shows how the compilation failed.
```

Esto quiere decir que no se pudo compilar la extensión `tornado.speedups`.
Y segun el sistema operativo te dice el comando a ejecutar para instalar lo necesario para una mejora de velocidad:
```
$ sudo apt-get install build-essential python-dev
```
[Inicio](#top)<br>

<a name="basicos"></a>

## [Elementos básicos del script del bot](https://github.com/helee18/python_sysadmin/blob/master/ejemplo-bot.py)

<a name="import"></a>

### Importar módulos
Al principio del script importamos los módulos de python necesarios. En este caso importamos el módulo [`logging`](https://docs.python.org/3/library/logging.html) para el registro y los submódulos [`Updater`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html), [`CommandHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html), [`MessageHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.messagehandler.html) y [`Filters`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.filters.html) de la librería [`telegram.ext`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html) a la que podemos acceder gracias a python-telegram-bot.

<a name="logging"></a>

### Logging
Habilitamos el registro del historial de eventos con [`basicConfig`](https://docs.python.org/3/library/logging.html#logging.basicConfig). Con `format` configuramos salga la fecha y hora, el nombre del bot, el nivel de registro y el mensaje que muestra. 

La librería [`logging`](https://docs.python.org/3/library/logging.html) tiene distintos niveles `Debug`, `Info`, `Warning`, `Error` y `Critical` de menos a mayor importancia.

En caso de que no configuremos el nivel, por defecto está configurado para mostrar mensajes de gategoría mínima `warning`. Configuramos que el nivel minimo sea `info` para que muestre también mensajes que no sean algo inesperado, como que el sistema funcione correctamente. 
```
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
```

Para registrar las acciones durante la ejecución del programa haremos uso de la funcion [`logging.getLogger(nombre del logger)`](https://docs.python.org/3/library/logging.html#logging.getLogger) y como nombre del logger pondremos `__name__` que, en un modulo, es el nombre de este en el espacio de nombres de Python.
```
logger = logging.getLogger(__name__)
```

Después, para el registro de errores definiremos una función en la que haremos uso de `logger.warning`.

<a name="main"></a>

### Función main
Al final del codigo, llamamos a la función principal `main`, en la cual tendremos todo el codigo del bot. Para llamar a la función, comprobamos que el codigo se esta ejecutando en el script principal, y no sea importado en otro. Esto se comprueba comparando que el atributo `__name__` con `__main__` ya que `__name__` adopta el nombre de `__main__` cuando se ejecuta en el script principal o adopta le nombre del modulo importado cuando no es así.
```
if __name__ == '__main__':
    main()
```

<a name="token"></a>

### Introducción del token
Definimos la función `main` y dentro de esta programamos el script del bot. Lo primero que tenemos que definir el `updater`, donde introducimos nuestro `token`.

[`Updater`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html) es una clase que ayuda al programador a codificar el bot. Recibe actualicaciones de telegram y las manda al [`Dispatcher`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html). El [`Dispatcher`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html) maneja las actualizaciones y las manda a los [`Handlers`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.handler.html). 

Añadimos `user_content=True` para usar las nuevas devoluciones basadas en contexto (`context based callbacks`). Puede producirse un fallo de uso de la antigua API dependiendo de la versión si no se añade. En la versión 13 no hace falta definirlo porque por defecto es `True`.

CallbackContext es un objeto que contiene contexto adicional de update, error o job. Esto almacena chat_data, user_data, job, error y argumentos.
```
def main():
    updater = Updater('TOKEN', use_context=True)
```

Para mayor seguridad, en el caso de que tengamos un repositorio, se puede crear otro archivo `.py` (auth.py) en el que definamos una variable a la que le asignamos el `token`. Este archivo no lo subiremos al repositorio, en el caso de utilizar el script del bot en otra maquina, tendremos que crear `auth.py` en el mismo directorio en el que esté el script antes de ejecutarlo.
```
token = 'TOKEN'
```

También en este archivo añadimos una lista con los `ids` de los usuarios que van a poder ejecutar los comandos del bot, así es mas seguro y no cualquier persona puede hacer uso de estos. 

Para poder conocer el `id` de un usuario, tenemos que iniciar el bot [`userinfobot`](https://telegram.me/userinfobot) y este nos dará nuesta información.
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/userinfobot.jpg" alt="start" width="450"/>

Hay que tener en cuenta que los `ids` no se ponen entre comillas porque son datos de tipo `int`.
```
ids = [ID1, ID2, ID3]
```

Para poder hacer uso de esta información, importamos tanto `token` como `ids` del archivo `auth`.
```
from auth import token
```

En el script del bot, en vez de poner el `token` directamente, solo mencionamos la variable. Y el uso de los `ids` se hará en las funciones de los comandos.
```
def main():
    updater = Updater(token, use_context=True)
```

Para que el archivo que tiene esta información no se suba por error a nuestro repositorio, añadiremos un archivo oculto [`.gitignore`](https://github.com/helee18/python_sysadmin/blob/master/.gitignore) en el que añadiremos lo que no queremos que se suba. Entre otras cosas, el archivo `auth.py`.
```
bot-venv/
auth.py
__pycache__/
```

Subiremos este archivo a nuestro repositorio y después ignorará los archivos que hayamos incluido en este.
```
git add .gitignore
git commit -m "no subir a github"
git push
```

<a name="espera"></a>

### Inicio bot y espera
Dentro de la funcion principal le indicamos al bot que inicie la espera de mensajes por parte de Telegram con [`start_polling()`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html#telegram.ext.Updater.start_polling).
```
    updater.start_polling()
```

También le decimos que se bloquee y se quede a la espera hasta recibir mensajes con [`idle()`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html#telegram.ext.Updater.idle). Esto lo hará hasta que, con Ctrl-C, paremos el bot.
```
    updater.idle()
```

<a name="start"></a>

### Comando `/start`
Siempre que querramos configurar un comando, declaramos en la función principal (`main`) un nuevo controlador [`add_handler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html#telegram.ext.Dispatcher.add_handler). Para manejar el comando utilizaremos [`CommandHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html) y dentro tendremos que decir cual es el mensaje de entrada que recibe (el comando) y cual es la función a la que llama. Haremos uso de `updater`, previamente declarado, que nos ayudará a codificar el bot ya que hace referencia al token identificativo.
```
    updater.dispatcher.add_handler(CommandHandler('start', start))
```

Fuera de la función principal tenemos que definir esta nueva función, con los parametros de entrada `update` y `context` y dentro de esta le diremos al bot que tiene que hacer en cada caso.

En este caso simplemente devolveremos un mensaje confirmando que ha conectado y funciona.

[`Update`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.update.html) es un objeto que representa una actualización entrate, [`message`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.update.html#telegram.Update.message) se refiere a un mensaje y [`reply_text`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.reply_text) a la respuesta que va a dar el bot, especificada dentro. Con `from_user.first_name` mostraremos el nombre del usuario que esta mandando el comando al bot.
```
def start(update, context):
    update.message.reply_text(
        'Welcome to PythonSysadminBot ' + update.message.from_user.first_name
    )
```

<a name="help"></a>

### Comando `/help`
Para que en cualquier momento se pueda recordar los comandos disponibles en el bot, creamos una función llamada `help` que nos liste todos los comandos que podemos utilizar.

Primero le decimos al bot dentro de la función principal que si recibe el comando `/help` llame a la función `help`.
```
    updater.dispatcher.add_handler(CommandHandler('help', help))
```

Después declaramos la función y comprobamos si el usuario está en la lista de usuarios que pueden hacer uso de los comandos. Para esto añadimos una lista de `ids` al archivo `auth.py` con los ids de estos usuarios y la importamos al principio de este archivo, como hemos comentado antes con el `token`.
```
from auth import ids
```

Después, con un [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) comprobamos si el id del usuario que ha mandado el mensaje [`message.chat_id`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html?highlight=chat_id#telegram.Message.chat_id) está en la lista.

En caso de que no se encuentre en la lista devolvemos un mensaje.
```
def help(update,context):
    if update.message.chat_id in ids:
        
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```

En caso de que sí que se encuentre en la lista, mostramos los comandos disponibles en el bot.

Para poder poner el titulo en negrita (Lista de comandos) le ponemos `*` al principio y al final y despues declaramos que lo lea como si fuese Markdown `parse_mode= 'Markdown'`. Y para introducir saltos te línea, añadimos `\n`.
```
        update.message.reply_text(
            '*Lista de comandos* \n'
            '/start - inicio del bot' , 
            parse_mode= 'Markdown'
        )
```

<a name="echo"></a>

### Comandos no definidos
Definimos una función con la cual se repetiran todos los mensajes o comandos que le mandemos al bot y este no entienda, es decir, que repetira el mensaje o comando que reciba si no hay una función definida para este.

Utilizaremos [`MessageHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.messagehandler.html) para manejar los mensajes introducidos. Esta clase de handler puede contener texto, archivos multimedia o actualizaciones de estado.

Con [`Filters.text`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.filters.html#telegram.ext.filters.Filters.successful_payment) filtramos la cadena de caracteres que pasamos. Y llamamos a la función `echo`.
```
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
```

Definimos la función y es aquí donde programammos al bot para que repita el mensaje recibido. Con [`update.message.text`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.text) le decimos al bot que lo que tiene que devolver el mismo mensaje entrante.
```
def echo(update, context):
    update.message.reply_text(update.message.text)
```

<a name="error"></a>

### Log de errores
Podemos añadir un controlador de errores en los [`Dispatcher`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html). Dentro de la función `main` llamamos a la función `error`.
```
    updater.dispatcher.add_error_handler(error)
```

Fuera definimos la función en la que hacemos uso de `logger` previamente definido y [`warning`](https://docs.python.org/3/library/logging.html#logging.Logger.warning) para el registro de mensajes a este nivel, donde funciona correctamente pero se produce una situación inesperada o se predice un problema futuro.
```
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
```
[Inicio](#top)<br>

<a name="monitorizar"></a>

## [Comandos para monitorizar un servidor](https://github.com/helee18/python_sysadmin/blob/master/bot.py)

<a name="f_terminal"></a>

### [Función para ejecutar comandos en Linux](https://github.com/helee18/python_sysadmin/blob/master/comandos_linux.py)
Definimos una función cuya finalidad es leer lo que nos devuelve el sistema al ejecutar el comando que nosotros le pasemos. Cuando nosotros mandemos ciertos comandos al bot, este llamará a la función y nos responderá con lo que el terminal muestre.

Esta función la podemos definir en un script separado del resto de forma que se ejecute en un proceso distinto. Esto sirve para que, al ejecutarse un comando, si este tarda en responder no bloquee el bot y este pueda seguir a la escucha de mas peticiones.

Para poder llamar a esta función en el script principal del bot [`bot.py`](https://github.com/helee18/python_sysadmin/blob/master/bot.py), tenemos que importarla.
```
from comandos_linux import terminal
```

Definimos la función en el script [`comandos_linux`](https://github.com/helee18/python_sysadmin/blob/master/comandos_linux.py) y declaramos una variable vacía que será con la que referenciaremos a lo que muestre el terminal como resultado del comando que le pasemos.
```
def terminal(entrada):
    salida = ""
```

Para interactuar con el sistema operativo tenemos que importar al principio del script la librería [`os`](https://docs.python.org/3/library/os.html).
```
import os
```

Hacemos uso del módulo [`os`](https://docs.python.org/3/library/os.html) utilizando [`popen`](https://docs.python.org/3/library/os.html#os.popen), que abre una tubería para la comunicación con el sistema mediante el paso de mensajes. De esta forma se pueden ejecutar los comandos que queramos a la vez que se esta ejecutando el script. Esto lo guardamos en una variable (f).
```
    f = os.popen(entrada)
```

Después utilizamos el método [`readlines()`](https://uniwebsidad.com/libros/python/capitulo-9/metodos-del-objeto-file) para leer las líneas del contenido referenciado con la variable f y con un bucle vamos referenciando caracter a caracter en la variable salida, previamente declarada.
```
    for i in f.readlines():
        salida += i 
```

Eliminamos el ultimo caracter, que sera el salto de línea o retorno de carro (\n).
```
    salida = salida[:-1]
```

Por último devolvemos la variable con la respuesta para poder usarla en la función del comando y poder mostrarla por la conversación con el bot por Telegram.
```
    return salida
```

<a name="nombre"></a>

### Comando `/nombre`
Podemos conocer el nombre del servidor añadiendo comando que le pida al sistema que le diga cual es el nombre del servidor en el que se esta ejecutando el script.

Para ello primero tenemos qe declarar un nuevo controlador [`add_handler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html#telegram.ext.Dispatcher.add_handler) dentro de la función `main` en el que indicamos el comando de entrada que recibe el bot y la función a la que llamamos con [`CommandHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html), como con todos los comandos.
```
    updater.dispatcher.add_handler(CommandHandler('nombre', nombre))
```

Definimos la función y comprobamos si el id del usuario que ha mandado el mensaje se encuentra en la lista de ids que tenemos definida para controlar quienes pueden hacer uso de las funciones del bot.
```
def nombre(update,context):
    if update.message.chat_id in ids:

    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```

Si se encuentra en la lista llamamos a la función `terminal` en la que se ejecutará el comando que nos devolverá el nombre del servidor ([`hostname`](https://linux.die.net/man/1/hostname)).
```
        nombre = terminal('hostname')
```

Hacemos que el bot nos responda con la información que le pedimos haciendo uso de una variable con la que hacemos referencia a lo que nos devuelve la función.
```
        update.message.reply_text(
            'El nombre del servidor es: \n' + nombre
        ) 
```

<a name="ip"></a>

### Comando `/ip`
Con este comando consultamos cual es la ip del servidor en el que se está ejecutando el script del bot.

En la función principal añadimos un nuevo manejador para que cuando mandemos un mensaje al bot con el comando `/ip` llame a la función `ip`.
```
    updater.dispatcher.add_handler(CommandHandler('ip', ip))
```

Definimos la función `ip` en la que comprobamos que el usuario está autorizado para hacer uso del comando y si no lo está mandamos un mensaje informando de ello.
```
def ip(update,context):
    if update.message.chat_id in ids:

    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```

Si pertenece a los usuarios autorizados, simplemente pedimos el nombre del servidor y llamamos a la función `terminal` en la que se ejecuta el comando que le pasemos y nos devuelve la respuesta del sistema. El comando que le pasamos para que nos devuelva la ip es [`hostname -I`](https://linux.die.net/man/1/hostname).
```
        nombre = terminal('hostname')
        ip = terminal("hostname -I")
```

Eliminamos el ultimo caracter del contenido que nos devuelve la función, al que referenciamos con una variable (ip.)
```
        ip = ip[:-1]
```

Por último hacemos que el bot responda con el resultado del comando ejecutado, en este caso la ip del servidor.
```
        update.message.reply_text(
            'La red a la que está conectado el servidor ' + nombre + ' es: \n' + red
        )
```

<a name="red"></a>

### Comando `/red`
Añadimos un nuevo manejador, con [`add_handler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html#telegram.ext.Dispatcher.add_handler), a la función principal (`main`) para el comando `/red`, el cual nos mostrará la red a la que está conectador nuestro servidor.
```
    updater.dispatcher.add_handler(CommandHandler("red", red))
```

Al igual que en la función `ip`, comprobamos que el usuario está autorizado, pedimos el nombre del servidor y llamamos a la función `terminal` la cual ejecutará el comando que le pasamos [`iwgetid`](https://linux.die.net/man/8/iwgetid) y nos devolverá la respuesta a este.
```
def red(update,context):
    if update.message.chat_id in ids:
        nombre = terminal('hostname')
        red = terminal("iwgetid")
```

Con una variable hacemos referencia a la respuesta que nos devuelve la función `terminal` y es está la que usamos dentro de [`reply_text`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.reply_text) para que el bot nos responda con la red conectada.
```
        update.message.reply_text(
        'La red a la que está conectado el servidor ' + nombre + ' es: \n\n' + red
    )
```

Si el usuario no estaba autorizado para conocer está información, el bot solo devuelve el siguiente mensaje.
```
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```

<a name="particiones"></a>

### Comando `/particiones`
Para conocer las particiones de disco que tiene el servidor, añadimos un nuevo [`Handler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.handler.html) dentro de la función principal que llama a su función correspondiente.
```
    updater.dispatcher.add_handler(CommandHandler("particiones", particiones))
```

En la función comprobamos si el usuario está autorizado para conocer información del servidor, pedimos el nombre de este y llamamos a la función `terminal` en la que se ejecutará el comando [`fdisk -l`](https://linux.die.net/man/8/fdisk) listandonos así las particiones existentes. Para que solo nos salga una lista con las particiones y un poco de información pero no toda, pasamos por tubería [`grep "Disco"`](https://linux.die.net/man/1/grep).
```
def particiones(update,context):
    if update.message.chat_id in ids:
        nombre = terminal('hostname')
        _fdisk = terminal('sudo fdisk -l | grep "Disco"')
```

El bot nos responde con la lista de todas las particiones que tiene el servidor.
```
        update.message.reply_text(
                'Las particiones del servidor ' + nombre + ' son: \n' + _fdisk
            )
```

En el caso de que no estuviera el usuario autorizado, mensamos un mensaje informando de ello.
```
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```

<a name="arquitectura"></a>

### Comando `/arquitectura`
Para conocer la arquitectura del sistema añadimos un comando que funciones como los anteriores.

Añadimos un manejador en la función principal (`main`) en el que al mandar al bot el comando `/arquitectura` llame a su función correspondiente `arquitectura` con [`CommandHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html).
```
    updater.dispatcher.add_handler(CommandHandler('arquitectura', arquitectura))
```

En la función comprobamos si el id del usuario pertenece a la lista de ids de los usuarios autorizados para hacer uso de los comandos del bot. En el caso de no estarlo el bot responderá con un mensaje al respecto.
```
def arquitectura(update,context):
    if update.message.chat_id in ids:

    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```

Si está autorizado el usuario llamamos a la función que nos devuelve el nombre del servidor `nombre` y a la función `terminal` que ejecuta el comando [`arch`](https://linux.die.net/man/1/arch) que nos devuelve la arquitectura del sistema del servidor. Lo que nos devuelve cada función lo referenciamos con distintas variables que utilizamos para que nos responda el bot con la información.
```
        nombre = terminal('hostname')
        arquitectura = terminal('arch')
        update.message.reply_text(
            'La arquitectura del sistema del servidor ' + nombre + ' es: \n' + arquitectura
        )
```

<a name="version"></a>

### Comando `/version`
Para conocer la versión de Linux del servidor tenemos que ejecutar el comando [`cat /proc/version`](https://docs.bluehosting.cl/tutoriales/servidores/como-saber-la-version-de-instalacion-de-mi-distribucion-linux.html ) en el terminal de este. Podemos programar al bot para que lo haga al mendarle el comando `/version` al igual que con comandos anteriores.

Primero añadimos un nuevo manejador en la función principal para que al recibir le bot el comando llame a la función correspondeinte.
```
    updater.dispatcher.add_handler(CommandHandler('version', version))
```

Y después definimos la función en la que, si el usuario está autorizado, llamamos a la función `terminal` y el pasamos los comandos que tiene que ejercutar para conocer el nombre del servidor y la versión del kernel. 

Finalmente hacemos que el bot nos responda con la versión y nos diga el nombre del servidor, así siempre estamos seguros de que consultamos el servidor que queremos.

Si el usuario no está autorizado para conocer esta información, el bot responderá con otro mensaje mencionando que no es un usuario autorizado.
```
def version(update,context):
    if update.message.chat_id in ids:
        nombre = terminal('hostname')
        version = terminal('cat /proc/version')

        update.message.reply_text(
            'La versión de Linux del servidor ' + nombre + ' es: \n\n' + version
        )   
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```

<a name="servicios"></a>

### Comandos `/estado_servicio`, `/iniciar_servicio`, `/parar_servicio` y `/reiniciar_servicio`
Podemos administrar los servicios instalados en el servidor viendo su estado, iniciandolos, parandolos o reiniciandolos. Podemos configurar el bot para que lo haga pasandole un comando diciendo lo que queremos que haga junto con un argumento que será el servicio que queremos consultar o modificar su estado.

Primnero declaramos cuatro nuevos manejadores para los cuatro comandos `/estado_servicio`, `/iniciar_servicio`, `/parar_servicio` y `/reiniciar_servicio`. Dentro de los [`CommandHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html) llamamos a la misma función `servicios` y configuramos que se puedan pasar argumentos [`pass_args=True`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html#telegram.ext.CommandHandler.pass_args) para que se introduzca el nombre del servicio.
```
    updater.dispatcher.add_handler(CommandHandler('estado_servicio', servicios, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('iniciar_servicio', servicios, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('parar_servicio', servicios, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('reiniciar_servicio', servicios, pass_args=True))
```

Definimos la función `servicios` y comprabamos con un condicional [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) si el usuario está autorizado para poder administrar el servidor.
```
def servicios(update,context):
    if update.message.chat_id in ids:

    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```

En el caso de que si que esté autorizado, con otro [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) comrobamos que se pasa un argumento. Para referirnos a los argumentos usamos [`context.args`](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Types-of-Handlers#commandhandlers-with-arguments) y calculamos cuantos son con [`len()`](https://docs.python.org/3/library/functions.html#len) En caso de que no sea un argumento, el bot nos responde con un aviso y nos da un ejemplo de como tenemos que hacer uso del comando.
```
        if len(context.args) == 1:

        else:
            update.message.reply_text(
                'Se debe especificar el servicio.\n\n'
                'Ejemplo:\n/reiniciar_servicio apache2'
            )    
```

En el caso de que si que se pase un argumento tenemos que comprobar cuál es el comando que se ha pasado comprobando con [`in`](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) si, por ejemplo, `estado_servidor` se encuentra en la texto recibido [`update.message.text`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.text). 

Segun lo que pidamos el comando que pasaremos a la función `terminal` para ejecutarlo en el servidor será uno u otro. En todos los casos lo haremos con [`/etc/init.d/SERVICIO`](https://www.linuxtotal.com.mx/index.php?cont=info_admon_003) porque asi nos devuelve siempre un mensaje para confirmar si se ha ejecutado el comando. Usamos [`context.args[0]`](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Types-of-Handlers#deep-linking-start-parameters) para referirnos al parametro que se ha pasado, el servicio, y añadirlo a la linea de comando que el bot va a ejecutar.

En el caso del estado, añadimos a la linea de comando `grep "Activate"` para que en vez de salirnos toda la información solo nos salga la linea que dice si esta activado o parado.
```
            if 'estado_servicio' in update.message.text:
                comando = '/etc/init.d/' + context.args[0] + ' status | grep "Active"'
            elif 'iniciar_servicio' in update.message.text:
                comando = '/etc/init.d/' + context.args[0] + ' start'
            elif 'parar_servicio' in update.message.text:
                comando = '/etc/init.d/' + context.args[0] + ' stop'
            else:
                comando = '/etc/init.d/' + context.args[0] + ' restart'
```

Una vez referienzado en una variable el comando que queremos ejecutar, llamamos a la función `terminal` y le pasamos de parametro la variable `comando` para que la ejecute y referenciamos con la variable `respuesta` lo que nos responde el sistema para que el bot nos lo devuelva como respuesta a nuestro mensaje.

Esto puede dar un fallo si el nombre del servicio no es correcto, por lo que hacemos uso de las excepciones de python [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) para que en caso de que de error y no se pueda ejecutar, con [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) se notifique por el chat con el bot y no se quede solo reflejado en el servidor.
```
            try: 
                respuesta = terminal(comando)

                update.message.reply_text(
                    respuesta
                )
            except:
                update.message.reply_text(
                    'Tiene que introducirse el nombre exacto del servicio'
                )
```


[Inicio](#top)<br>