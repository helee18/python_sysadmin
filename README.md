<a name="top"></a>

![Python para Sysadmin con Telegram](https://github.com/helee18/python_sysadmin/blob/master/images/titulo.png)
---
[`Telegram`](https://web.telegram.org/), una plataforma de mensajeria, tiene la opción de crear bots de todo tipo. Los administradores de sistemas pueden hacer uso de estos bots para manipular o consultar el estado de un servidor creando uno. Para ello se puede hacer uso de [`Python`](https://www.python.org/), un lenguaje de programación multiplataforma, programando las funciones que queremos que resuelva el bot.

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

<br>

<a name="crear"></a>

## Crear un bot de Telegram

El primer paso para crear un bot iniciar **BotFather**, el bot principal que reconoce una serie de comandos, desde Telegram. Como respuesta, nos devuelve el `token` identificativo de nuestro bot.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/01.jpg" alt="BotFather" width="400"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/02.jpg" alt="start" width="400"/><br>

Creamos un nuevo bot con `/newbot` y le ponemos nombre al bot y al usuario.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images//03.jpg" alt="newbot" width="400"/><br>

Desde el BotFather se puede modificar los bots. Por ejemplo, se puede cambiar el nombre con `/setname` y añadir una foto con `/setuserpic`.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/04.jpg" alt="setname" width="400"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/05.jpg" alt="setuserpic" width="400"/>

<br>[Inicio](#top)

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
<br>[Inicio](#top)

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

Para mayor seguridad, en el caso de que tengamos un repositorio, se puede crear otro archivo `.py` (auth.py), dentro de la carpeta una carpeta (auth) en mi caso, en el que definamos una variable a la que le asignamos el `token`. Este archivo no lo subiremos al repositorio, en el caso de utilizar el script del bot en otra maquina, tendremos que crear `auth/auth.py` en el mismo directorio en el que esté el script antes de ejecutarlo.
```
token='TOKEN'
```

Para poder hacer uso de esa variable, la importamos al principio del script del bot.
```
from auth.auth import token
```

Y en el script del bot, en vez de poner el `token` directamente, solo mencionamos la variable.
```
def main():
    updater = Updater(token, use_context=True)
```

Para que el archivo que tiene nuestro `token` no se suba por error a nuestro repositorio, añadiremos un archivo oculto [`.gitignore`](https://github.com/helee18/python_sysadmin/blob/master/.gitignore) en el que añadiremos lo que no queremos que se suba.
```
bot-venv/
auth/
```

Subiremos este archivo a nuestro repositorio y después ignorará los archivos que no deseemos que este en nuestro repositorio en github.
```
git add .gitignore
git commit -m "bot-venv y auth"
git push
```

<a name="espera"></a>

### Inicio bot y espera
Dentro de la funcion principal le indicamos al bot que inicie la espera de mensajes por parte de Telegram.
```
    updater.start_polling()
```

También le decimos que se bloquee y se quede a la espera hasta recibir mensajes. Esto lo hará hasta que, con Ctrl-C, paremos el bot.
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

En este caso simplemente devolveremos un emnsaje confirmando que ha conectado y funciona.

[`Update`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.update.html) es un objeto que representa una actualización entrate, [`message`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.update.html#telegram.Update.message) se refiere a un mensaje y [`reply_text`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.reply_text) a la respuesta que va a dar el bot, especificada dentro. Con `from_user.first_name` mostraremos el nombre del usuario que esta mandando el comando al bot.
```
def start(update, context):
    update.message.reply_text(
        'Welcome to PythonSysadminBot ' + update.message.from_user.first_name
    )
```

<a name="help"></a>

### Comando `/help`
Para que  en cualquier comento se pueda recordar los comandos disponibles en el bot, creamos una función llamada `help` que nos liste todos los comandos que podemos utilizar.
```
updater.dispatcher.add_handler(CommandHandler('help', help))
```

Para poder poner el titulo en negrita (Lista de comandos) le ponemos `*` al principio y al final y despues declaramos que lo lea como si fuese Markdown `parse_mode= 'Markdown'`. Y para introducir saltos te línea, añadimos `\n`.
```
def help(update,context):
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
<br>[Inicio](#top)

<a name="monitorizar"></a>

## [Comandos para monitorizar un servidor](https://github.com/helee18/python_sysadmin/blob/master/bot.py)

<a name="f_terminal"></a>

### Función para ejecutar comandos en Linux
Definimos una función cuya finalidad es leer lo que nos devuelve el sistema al ejecutar el comando que nosotros le pasemos. Cuando nosotros mandemos ciertos comandos al bot, este llamará a la función y nos responderá con lo que el terminal muestre.

Definimos la función y declaramos una variable vacía que será con la que referenciaremos a lo que muestre el terminal como resultado del comando que le pasemos.
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

Después utilizamos el método `readlines()` para leer las líneas del contenido referenciado con la variable f y con un bucle vamos referenciando caracter a caracter en la variable salida, previamente declarada.
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

Definimos la función y en ella llamamos  al afunción `terminal` en la que se ejecutará el comando que nos devolverá el nombre del servidor.
```
def nombre(update,context):
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

Definimos la función `ip` en la que simplemente pedimos el nombre del servidor y llamamos a la función `terminal` en la que se ejecuta el comando que le pasemos y nos devuelve la respuesta del sistema. El comando que le pasamos para que nos devuelva la ip es `hostname -I`.
```
def ip(update,context):
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

Al igual que en la función `ip`, pedimos el nombre del servidor y llamamos a la función `terminal` la cual ejecutará el comando que le pasamos `iwgetid` y nos devolverá la respuesta a este.
```
def red(update,context):
    nombre = terminal('hostname')
    red = terminal("iwgetid")
```

Con una variable hacemos referencia a la respuesta que nos devuelve la función `terminal` y es está la que usamos dentro de [`reply_text`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.reply_text) para que el bot nos responda con la red conectada.
```
    update.message.reply_text(
        'Las particiones del servidor ' + nombre + ' son: \n' + _fdisk
    )
```

<a name="particiones"></a>

### Comando `/particiones`
Para conocer las particiones de disco que tiene el servidor, añadimos un nuevo [`Handler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.handler.html) dentro de la función principal que llama a su función correspondiente.
```
    updater.dispatcher.add_handler(CommandHandler("particiones", particiones))
```

En la función pedimos el nombre del servidor y llamamos a la función `terminal` en la que se ejecutará el comando `fdisk -l` listandonos así las particiones existentes. Para que solo nos salga una lista con las particiones y un poco de información pero no toda, pasamos por tubería `grep "Disco"`.
```
def particiones(update,context):
    nombre = terminal('hostname')
    _fdisk = terminal('sudo fdisk -l | grep "Disco"')
```

El bot nos responde con la lista de todas las particiones que tiene el servidor.
```
    update.message.reply_text(
        'Las particiones del servidor son: \n' + _fdisk
    )

```

<a name="arquitectura"></a>

### Comando `/arquitectura`
Para conocer la arquitectura del sistema añadimos un comando que funciones como los anteriores.

Añadimos un manejador en la función principal (`main`) en el que al mandar al bot el comando `/arquitectura` llame a su función correspondiente `arquitectura` con [`CommandHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html).
```
    updater.dispatcher.add_handler(CommandHandler('arquitectura', arquitectura))
```

En la función llamamos a la función que nos devuelve el nombre del servidor `nombre` y a la función `terminal` que ejecuta el comando `arch` que nos devuelve la arquitectura del sistema del servidor. Lo que nos devuelve cada función lo referenciamos con distintas variables que utilizamos para que nos responda el bot con la información.
```
def arquitectura(update,context):
    nombre = terminal('hostname')
    arquitectura = terminal('arch')
    update.message.reply_text(
        'La arquitectura del sistema del servidor ' + nombre + ' es: \n' + arquitectura
    )
```

<br>[Inicio](#top)