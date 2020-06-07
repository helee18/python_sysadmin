<a name="top"></a>

![Python para Sysadmin con Telegram](https://github.com/helee18/python_sysadmin/blob/master/images/titulo.png)
---

**¿Qué puede hacer este bot?**

Este bot funciona como medio de comunicación entre un usuario y un servidor desde cualquier dispositivo. 

Dispone de una serie de comandos para monitorizar el servidor como puede ser: `/ip`, `/usuarios`, `/memoria` o `/parar_servicio`.

- [`Bot de Telegram`](#bot)
    - [`Crear un bot de Telegram`](#crear)
- [`Instalar python-telegram-bot`](#instalar)
    - [`Entorno de desarrollo virutal`](#venv)
    - [`Instalación con pip`](#pip)
    - [`Instalación clonando el repositorio`](#github)
- [`Ejecutar bot`](#ejecutar)
- [`Elementos básicos del script del bot`](#basicos)
    - [`Importar módulos`](#import)
    - [`Logging`](#logging)
    - [`Función main`](#main)
    - [`Introducción del token`](#token)
    - [`Inicio bot y espera`](#inicio)
    - [`Controladores de comandos`](#controladores_comandos)
    - [`Funciones de comandos`](#funciones)
    - [`Control de usuarios`](#usuarios)
    - [`Comando /start`](#start)
    - [`Comando /help `](#help)
    - [`Sugerir comandos`](#sugerir)
    - [`Comandos no definidos`](#echo)
    - [`Log de errores`](#error)
- [`Funciones para ejecutar comandos en Linux`](#comandos_linux)
    - [`Función que devuelve la respuesta en forma de texto`](#terminal_texto)
    - [`Función que devuelve la respuesta en forma de imagen`](#terminal_imagen)
- [`Conversación bot-usuario`](#conversacion)
    - [`Responder con texto`](#texto)
    - [`Responder con imagen`](#imagen)
- [`Comandos para monitorizar un servidor`](#monitorizar)
    - [`Comando /nombre`](#nombre)
    - [`Comando /ip`](#ip)
    - [`Comando /red`](#red)
    - [`Comando /arquitectura`](#arquitectura)
    - [`Comando /version`](#version)
    - [`Comando /usuarios`](#usuarios)
    - [`Comando /espacio`](#espacio)
    - [`Comando /memoria`](#memoria)
    - [`Comando /procesos`](#procesos)
    - [`Comando servicios (/estado_servicio, /iniciar_servicio, /parar_servicio y /reiniciar_servicio)`](#servicios)

[Inicio](#top)<br>

<a name="bot"></a>

## Bot de Telegram

La plataforma de mensajería [`Telegram`](https://web.telegram.org/) tiene la opción de ejecutar bots dentro de ella. Estos bots puede hacer prácticamente cualquier cosa como mostrar noticias, crear herramientas personalizadas, integrarse con otros servicios o incluso crear juegos para un jugador o varios.

Los usuarios pueden interactuar con el bot enviandoles mensajes o comandos desde el chat con el bot o añadiendolo a un grupo. También se pueden enviar solicitudes desde cualquier chat, grupo o canal escribiendo el nombre del bot y la consulta.

<a name="crear"></a>

### Crear un bot de Telegram

El primer paso para crear un bot es iniciar [`BotFather`](https://telegram.me/BotFather), el bot principal de telegram que reconoce una serie de comandos. Como respuesta, nos devuelve el `token` identificativo de nuestro bot.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather01.jpg" alt="BotFather" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather02.jpg" alt="start" width="350"/><br>

Creamos un nuevo bot con `/newbot` y le ponemos nombre al bot y al usuario.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather03.jpg" alt="newbot" width="350"/><br>

Desde el [`BotFather`](https://telegram.me/BotFather) se puede modificar los bots. Por ejemplo, se puede cambiar el nombre con `/setname` y añadir una foto con `/setuserpic`. En cualquier momento podemos mandar el comadno `/help` para ver la lista de comandos que podemos usar dependiendo de lo que queramos hacer.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather04.jpg" alt="setname" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather05.jpg" alt="setuserpic" width="350"/><br>

Podemos añadir una descripción para nuestro bot con `\setdescription`. Esta aparecerá antes de iniciarlo.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather06.jpg" alt="setdescription" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather07.jpg" alt="descripcion" width="350"/><br>

[Inicio](#top)<br>

<a name="instalar"></a>

## Instalar python-telegram-bot

Para programar el bot se puede hacer uso de [`Python`](https://www.python.org/), un lenguaje de programación multiplataforma. Configuraremos al bot para que responda a las distintas peticiones que le hagamos. Esto lo haremos desarrollando un script en el que reflejaremos cada comando de entrada que recibirá el bot y como responderá este.

Para [`Python`](https://www.python.org/) existen varias librerías con las que desarrollar bots de [`Telegram`](https://web.telegram.org/) como por ejemplo [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot).

El submódulo [`telegram.ext`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.html) proporciona una interfaz fácil de usar y le quita algo de trabajo al programador.

Se compone de varias clases, pero las dos más importantes son [`telegram.ext.Updater`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html) y [`telegram.ext.Dispatcher`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html).

[`Updater`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html) que es una clase que ayuda al programador a codificar el bot. Recibe actualizaciones de [`Telegram`](https://web.telegram.org/) y las manda al [`Dispatcher`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html). El [`Dispatcher`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.dispatcher.html) maneja las actualizaciones y las manda a los [`Handlers`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.handler.html).

[Inicio](#top)<br>

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

<a name="basicos"></a>

## Ejecutar bot

Cuando hayamos desarrollado el script de nuestro bot, ejecutamos este en segundo plano.
```
$ python3 bot.py &
```

Para poder ver los procesos que tenemos en segundo plano escribimos `jobs` en nuestro terminal y aparece un número delante del estado del proceso. Para pasar a primer plano el bot y poder pararlo con `Ctrl-C` escibimos `fg` y el número que le corresponda.
```
$ jobs

[1]+  Ejecutando              python3 bot.py &
```
```
fg 1
```

Para ejecutar el bot se puede hacer en un `serverless` como [`AWS Lambda`](https://aws.amazon.com/es/lambda/), que permite ejecutar código y que el bot se quede a la espera de peticiones. `Serverless` es un modelo de ejecución en el que el proveedor de la nube (AWS) es responsable de ejecutar el fragmento de codigo mediante la asignación dinámica de recursos. 

[Inicio](#top)<br>

<a name="basicos"></a>

## [Elementos básicos del script del bot](https://github.com/helee18/python_sysadmin/blob/master/ejemplo-bot.py)

<a name="import"></a>

### Importar módulos
Al principio del script importamos los módulos de python necesarios. Los módulos son ficheros que contienen contenido python y almacenan variables y funciones que podemos usar en nuestro script.

En este caso importamos el módulo [`logging`](https://docs.python.org/3/library/logging.html) para el registro y los submódulos [`Updater`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html), [`CommandHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html), [`MessageHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.messagehandler.html) y [`Filters`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.filters.html) de la librería [`telegram.ext`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html) a la que podemos acceder gracias a [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot).
```
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
```

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

Hacemos uso de [`Updater`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html) que es la clase que recibe las actualizaciones de [`Telegram`](https://web.telegram.org/).

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

<a name="controladores_comandos"></a>

### Controladores de comandos
Nos comunicaremos con el bot mediante comandos, estos comienzan por `/` y programaremos al bot para que, según el comando que reciba, realice una función u otra y haga en el servidor lo que nosotros le pidamos o nos muestre la información de este que nos interesa.

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

Para poder conocer el `id` de un usuario, tenemos que iniciar el bot [`userinfobot`](https://telegram.me/userinfobot) y este nos dará nuestra información.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/userinfobot.jpg" alt="start" width="350"/><br>

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
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/start.jpg" alt="start" width="350"/><br>

[Inicio](#top)<br>

<a name="help"></a>

### Comando `/help`
Para poder recordar la lista de comandos que podemos utilizar en el bot y para que sirve cada uno, definimos el comando `/help`.
```
    updater.dispatcher.add_handler(CommandHandler('help', help))
```

Y en la función vamos añadiendo los comandos que vamos configurando para poder tenerlos en una lista y consultarlo en cualquier momento.
```
def help(update,context):
    if update.message.chat_id in ids:
        update.message.reply_text(
            'Lista de comandos \n\n'
            '/start - inicio del bot \n\n'
        )
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/help.jpg" alt="help" width="350"/><br>

[Inicio](#top)<br>

<a name="sugerir"></a>

### Sugerir comandos
También podemos hacer que el bot nos sugiera que comandos queremos mandar. Para esto tenemos que mandarle al [`BotFather`](https://telegram.me/BotFather) el comando `/setcommands` y después la lista de comandos de los que dispone el bot junto con su descripción.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/botfather08.jpg" alt="setcommands" width="350"/><br>

Cuando escribamos `/` en la barra de mensaje en la conversación con el bot o le demos al botón, nos saldrán todos los comandos que podemos enviar.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/sugerir_comandos.jpg" alt="sugerir_comandos" width="350"/><br>

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
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/no_definidos.jpg" alt="comandos_no_definidos" width="350"/><br>
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

<a name="comandos_linux"></a>

## [Funciones para ejecutar comandos en Linux](https://github.com/helee18/python_sysadmin/blob/master/comandos_linux.py)
Para poder interactuar con el sistema, definimos funciones cuyo trabajo es ejecutar el comando linux que nosotros le pasemos y devolvernos la respuesta del sistema a este.

Podemos hacer dos funciones distintas, una de ellas encargada de devolvernos la respuesta del sistema en modo texto (`terminal_texto`) y otra que nos devuelva esta información en forma de imagen (`terminal_imagen`).

Estas funciones las podemos definir en un script separado ([`comandos_linux`](https://github.com/helee18/python_sysadmin/blob/master/comandos_linux.py)) del resto de forma que se ejecute en un proceso distinto. Esto sirve para que, al ejecutarse un comando, si este tarda en responder no bloquee el bot y este pueda seguir a la escucha de más peticiones.

Para poder llamar a estas funciones en el script principal del bot [`bot.py`](https://github.com/helee18/python_sysadmin/blob/master/bot.py), tenemos que importarlas.
```
from comandos_linux import terminal_texto, terminal_imagen
```

Ambas funciones tienen que interactuar con el sistema por lo que tenemos que importar al principio del script [`comandos_linux`](https://github.com/helee18/python_sysadmin/blob/master/comandos_linux.py) la librería [`os`](https://docs.python.org/3/library/os.html).
```
import os
```

Hacemos uso del módulo [`os`](https://docs.python.org/3/library/os.html) utilizando [`popen`](https://docs.python.org/3/library/os.html#os.popen), que abre una tubería para la comunicación con el sistema mediante el paso de mensajes. De esta forma se pueden ejecutar los comandos linux que queramos a la vez que se está ejecutando el script. 

[Inicio](#top)<br>

<a name="terminal_texto"></a>

### Función que devuelve la respuesta en forma de texto
Definimos la función `terminal_texto` declaramos una variable vacía que será con la que referenciaremos a lo que muestre el terminal como resultado del comando linux que le pasemos.
```
def terminal_texto(entrada):
    salida = ""
```

Ejecutamos el comando que recibimos de entrada con [`popen`](https://docs.python.org/3/library/os.html#os.popen). Esto lo guardamos en una variable (`f`).
```
    f = os.popen(entrada)
```

Después utilizamos el método [`readlines()`](https://uniwebsidad.com/libros/python/capitulo-9/metodos-del-objeto-file) para leer las líneas del contenido referenciado con la variable `f` y con un bucle [`for`](https://docs.python.org/3/reference/compound_stmts.html#for) vamos referenciando caracter a caracter en la variable salida, previamente declarada.
```
    for i in f.readlines():
        salida += i 
```

Eliminamos el último caracter, que será el salto de línea o retorno de carro (`\n`).
```
    salida = salida[:-1]
```

Por último devolvemos la variable con la respuesta para usarla y mostrar la información por la conversación con el bot por Telegram.
```
    return salida
```
[Inicio](#top)<br>

<a name="terminal_imagen"></a>

### Función que devuelve la respuesta en forma de imagen
Para poder convertir la respuesta del sistema en imagen, primero tenemos que instalar [`ImageMagick`](https://imagemagick.org/index.php), una herramienta que hace posible convertir texto en imagen pudiendo elegir el tamaño, color del texto, del fondo y la tipografía.
```
$ sudo apt-get install imagemagick
```

Esta herramienta se usa con el comando [`convert`](https://imagemagick.org/script/convert.php), con [`label:@-`](http://www.imagemagick.org/Usage/text/#label) decimos que el texto que hay que convertir a imagen es el que hemos obtenido por respuesta al comando que se ha ejecutado a la vez y le decimos la ruta donde se va a guardar la imagen junto al nombre de esta.
```
entrada | convert label:@- image.png
```

Podemos elegir la tipografía con [`font`](https://imagemagick.org/script/command-line-options.php#font), el color de la letra [`fill`](https://imagemagick.org/script/command-line-options.php#fill) y el color del fondo [`background`](https://imagemagick.org/script/command-line-options.php#background)
```
comando_linux | convert -font Courier -fill white -background black label:@- image.png
```

Al ejecutarlo podemos encontrarnos con errores. Uno de ellos se soluciona comentando una de las líneas del archivo `/etc/ImageMagick-6/policy.xml`.
```
convert-im6.q16: attempt to perform an operation not allowed by the security policy `@-' @ error/property.c/InterpretImageProperties/3666.
```
```
$ sudo nano /etc/ImageMagick-6/policy.xml
```
```
  <policy domain="path" rights="none" pattern="@*"/>
```
```
  <!-- <policy domain="path" rights="none" pattern="@*"/> -->
```

Otro error es por culpa del tamaño máximo de imagen que acepta. En el archivo `/etc/ImageMagick-6/policy.xml` cambiamos el tamaño de alto y ancho de KP a MP.
```
convert-im6.q16: width or height exceeds limit `@-' @ error/label.c/ReadLABELImage/138.
```
```
$ sudo nano /etc/ImageMagick-6/policy.xml
```
```
  <policy domain="resource" name="width" value="16KP"/>
  <policy domain="resource" name="height" value="16KP"/>
```
```
  <policy domain="resource" name="width" value="16MP"/>
  <policy domain="resource" name="height" value="16MP"/>
```

Definimos la función `terminal_imagen` en la que ejecutamos el comando linux que le pasamos pero convirtiendo la respuesta del sistema en una imagen.

Para que no haya problemas con las imagenes, al principio de esta función borramos con [`popen`](https://docs.python.org/3/library/os.html#os.popen) y [`rm -f`](https://linux.die.net/man/1/rm) la imagen si existe sin pedir confirmación de si queremos borrarla. Para borrarla utilizamos el condicional [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) y comprobamos que existe con [`os.path.exists`](https://docs.python.org/3/library/os.path.html#os.path.exists).
```
def terminal_imagen(entrada):
    if os.path.exists('image.png'): 
        os.popen('rm -f image.png')
```

Tenemos que añadir al comando que recibe de entrada la parte de convertirlo en imagen.
```
    entrada = entrada + ' | convert -font Courier -pointsize 50 -fill white -background black label:@- image.png'
```

Con [`popen`](https://docs.python.org/3/library/os.html#os.popen) ejecutamos el comando en el sistema.
```
    os.popen(entrada)
```
[Inicio](#top)<br>

<a name="conversacion"></a>

## Conversación bot-usuario
Cuando mandamos comando al bot para recibir información del servidor o administrarlo remotamente requerimos una respuesta de este con la información solicitada o una confirmación de que lo que queríamos hacer se ha hecho correctamente. Esta respuesta la podemos querer en forma de mensaje de texto o de imagen.

Para poder decirle al bot de que forma queremos que nos responda, tenemos que configurar una conversación entre el bot y el usuario.

El primer paso es definir un nuevo manejador dentro la función principal, este tendrá dentro la variable `conv_handler` que declararemos encima, también dentro de la función principal, con la estructura de la conversación.
```
    updater.dispatcher.add_handler(conv_handler)
```

Para establecer la estructura usamos [`ConversationHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html) que es el controlador para mantener una conversación. Para poder usarlo tenemos que importarlo al principio del script junto con el resto de submódulos de la librería [`telegram.ext`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html).
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

En nuestro caso tendremos `TIPO`.
```
TIPO = range(1)
```
```
        states={
            TIPO: [ ]
        },
```

Por último declaramos [`fallbacks`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html#telegram.ext.ConversationHandler.fallbacks) donde definimos el comando que podemos usar en cualquier momento dentro de la conversación. Este llamará a una función en la que simplemente devolveremos [`ConversationHandler.END`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html#telegram.ext.ConversationHandler.END) para salir de la conversación. 
```
        fallbacks=[CommandHandler('cancel', cancel)]
```
```
def cancel(update,context):
    update.message.reply_text(
        'Se ha cancelado el comando',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/cancel.jpg" alt="cancel" width="350"/><br>

Cuando definimos las funciones de los comandos tenemos que definir una variable global en la que haremos referencia al comando linux que queremos ejecutar según el comando que le hayamos mandado al bot.

También declaramos una variable en la que tendremos la respuesta que nos va a dar posteriormente el bot pero sin los datos que solicitamos del servidor ya que aún no los conocemos. Esta respuesta será una línea en la que diremos que estamos mostrando.
```
def funcion(update,context):
    if update.message.chat_id in ids:
        global comando_linux, respuesta
        comando_linux = " "
        respuesta = " "
```

Después hacemos que el bot nos pregunte si queremos recibir la respuesta en modo de texto o imagen. Para esto hacemos que aparezca un botón en la barra de mensaje al cual le das y aparecen las dos opciones en el espacio del teclado del móvil. Estas opciones pueden aparecer directamente en el teclado o puede hacer falta darle al botón.

Primero tenemos que declarar una variable con las opciones que van a aparecer.
```
        keyboard = [['Texto', 'Imagen']]
```

Después con [`message.reply_text`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.reply_text) le decimos al bot qué tiene que responder. Con [`reply_markup`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.inlinequeryresultgame.html?highlight=reply_markup#telegram.InlineQueryResultGame.reply_markup) configuramos lo que va a aparecer en el teclado. [`ReplyKeyboardMarkup`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html) representa al teclado y dentro establecemos lo que va a aparecer con la variable [`keyboard`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html#telegram.ReplyKeyboardMarkup.keyboard) y con [`one_time_keyboard=True`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html#telegram.ReplyKeyboardMarkup.one_time_keyboard) hacemos que se oculte tras usarlo pero no que desaparezca del todo, eso lo haremos posteriormente con [`ReplyKeyboardRemove`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardremove.html).

Para poder usar el módulo [`ReplyKeyboardMarkup`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html) tenemos que importarlo al principio del script.
```
from telegram import ReplyKeyboardMarkup
```
```
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/tex_img_01.jpg" alt="botón" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/tex_img_02.jpg" alt="opciones" width="350"/><br>

Por último hacemos que la función devuelva el nombre del estado al que queremos pasar.
```
        return TIPO
```

Dentro del controlador de la conversación, en el estado, definimos dos manejadores de mensajes [`MessageHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.messagehandler.html) en los que filtraremos los dos mensajes que pueden introducirse y la función a la que llamamos según el mensaje. Para filtrar el mensaje usamos [`Filters.regex`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.filters.html?highlight=regex#telegram.ext.filters.Filters.regex) que nos permite filtrar el texto de entrada con patrones, en nuestro caso haremos uso de `^` y `$` para referirnos que empieza y acaba la cadena así.
```
        states={
            TIPO: [MessageHandler(Filters.regex('^Texto$'), texto),
                   MessageHandler(Filters.regex('^Imagen$'), imagen)]
        },
```
[Inicio](#top)<br>

<a name="texto"></a>

### Responder con texto
Si lo que hemos introducido es `Texto` llamaremos a la función `texto` donde llamamos a la función `terminal_texto` y le pasamos como parámetro el comando linux previamente establecido en la función del comando que introdujimos. Esta función nos devuelve la respuesta del sistema al comando linux y la guardamos en una variable (`respuesta_sistema`) para posteriormente usarla en la respuesta del bot.
```
def texto(update,context):
    respuesta_sistema = terminal_texto(comando_linux)
```

Programamos al bot para que responda haciendo uso de la variable `respuesta_sistema` y la variable `respuesta` declarada en la función del comando.

Es aquí donde, con [`reply_markup`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.inlinequeryresultgame.html?highlight=reply_markup#telegram.InlineQueryResultGame.reply_markup) y el módulo [`ReplyKeyboardRemove`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardremove.html) eliminamos que salta en el teclado las opciones de `Texto` e `Imagen`.

Para poder usar el módulo tenemos que importarlo junto con [`ReplyKeyboardMarkup`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html).
```
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
```
```
    update.message.reply_text(
        respuesta + '\n' + respuesta_sistema,
        reply_markup=ReplyKeyboardRemove()
    )
```

Por último salimos de la conversación devolviendo [`ConversationHandler.END`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html#telegram.ext.ConversationHandler.END).
```
    return ConversationHandler.END
```
[Inicio](#top)<br>

<a name="imagen"></a>

### Responder con imagen
Si por lo contrario introducimos `Imagen` llamamos a la función `imagen` en la que llamaremos a la función `terminal_imagen` donde se ejecutará el comando y se convertirá en imagen.
```
def imagen(update,context):
    terminal_imagen(comando_linux)
```

Hacemos que el bot responda primero con la variable `respuesta`, declarada en la función del comando, y eliminamos del teclado la opción de elegir entre `Texto` o `Imagen` con  [`reply_markup`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.inlinequeryresultgame.html?highlight=reply_markup#telegram.InlineQueryResultGame.reply_markup) y el módulo [`ReplyKeyboardRemove`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardremove.html)
```
        update.message.reply_text(
            respuesta,
            reply_markup=ReplyKeyboardRemove()
        )
```

Para que el bot nos responda con la imagen, primero hacemos uso de las excepciones de python [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) para que intente mostrarla y, en caso de que de error al mostrarla, con [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) el bot responda con un mensaje avisando de que no se puede mostrar. 
```
    try:
        
    except:
        update.message.reply_text(
            '-No se puede mostrar la imagen-'
        )
```

Antes de hacer que el bot nos mande la imagen, esperamos unos segundos porque puede tardar en crearse. Para esto hacemos uso del condicional [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) y comprobando que no existe con [`not`](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) y [`os.path.exists`](https://docs.python.org/3/library/os.path.html#os.path.exists). En el caso de que no exista, utilizamos [`time.sleep(1)`](https://docs.python.org/3/library/time.html#time.sleep) para esperar un segundo en nuestro caso. 

Al principio del script tenemos que importar [`os`]([`os`](https://docs.python.org/3/library/os.html)) y [`time`](https://docs.python.org/3/library/time.html) para poder usar estos módulos.
```
import os
import time
```
```
        if not os.path.exists('image.png'): 
            time.sleep(1)
```

Después hacemos que el bot nos mande la imagen con [`bot.send_photo`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.bot.html?highlight=bot.send_photo#telegram.Bot.send_photo). Dentro tenemos que añadir el parámetro `chat_id` y pasarle el chat_id actual ([`update.message.chat_id`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.chat_id)). 

Para abrir la foto añadimos el parámetro `photo` y se la pasamos con la función [`open`](https://docs.python.org/3/library/functions.html#open) donde añadimos la ruta a la imagen y `rb` para que lo abra para lectura en modo binario.
```
        update.message.bot.send_photo(
            chat_id=update.message.chat_id, 
            photo=open('image.png', 'rb')
        )
```

Por último salimos de la conversación devolviendo [`ConversationHandler.END`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html#telegram.ext.ConversationHandler.END).
```
    return ConversationHandler.END
```
[Inicio](#top)<br>

<a name="monitorizar"></a>

## [Comandos para monitorizar un servidor](https://github.com/helee18/python_sysadmin/blob/master/bot.py)

Con todos los comandos que utilicemos para monitorizar nuestro servidor tendremos la opción de elegir si recibir la información con texto o con imagenes. Por ello definimos los [`CommandHandler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html) dentro del controlador de la conversación del usuario con el bot para decir como recibir la respuesta.
```
conv_handler = ConversationHandler(
        entry_points=[CommandHandler('comando', funcion)],
         
```

La estructura de las funciones de la mayoria de comandos es la siguiente:
```
def funcion(update,context):
    if update.message.chat_id in ids:
        global comando_linux, respuesta
        comando_linux = ' '
        respuesta = ' '

        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        return TIPO
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```
[Inicio](#top)<br>

<a name="nombre"></a>

### Comando `/nombre`
Podemos conocer el nombre del servidor añadiendo comando que le pida al sistema que le diga cual es el nombre del servidor en el que se esta ejecutando el script ([`hostname`](https://linux.die.net/man/1/hostname)).
```
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('nombre', nombre),
                      ...],
```
```
def nombre(update,context):
    if update.message.chat_id in ids:
        global comando_linux, respuesta
        comando_linux = 'hostname'
        respuesta = 'El nombre del servidor es: '

        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        return TIPO
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```

En el resto de comandos añadimos el nombre del servidor a la respuesta llamando a la función `terminal_texto`.
```
        respuesta = '' + terminal_texto('hostname') + ' es: '
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/nombre01.jpg" alt="nombre01" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/nombre02.jpg" alt="nombre02"/><br>

[Inicio](#top)<br>

<a name="ip"></a>

### Comando `/ip`
Con este comando consultamos cual es la ip del servidor en el que se está ejecutando el script del bot. El comando linux que le pasamos para que nos devuelva la ip es [`hostname -I`](https://linux.die.net/man/1/hostname).
```
    conv_handler = ConversationHandler(
        entry_points=[...
                      CommandHandler('ip', ip)],
```
```
def ip(update,context):
    if update.message.chat_id in ids:
        global comando_linux, respuesta
        comando_linux = 'hostname -I'
        respuesta = 'La ip del servidor ' + terminal_texto('hostname') + ' es: '

        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        return TIPO
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/ip01.jpg" alt="ip01" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/ip02.jpg" alt="ip02"/><br>

[Inicio](#top)<br>

<a name="red"></a>

### Comando `/red`
Conoceremos la red a la que está conectador nuestro servidor con [`iwgetid`](https://linux.die.net/man/8/iwgetid).
```
    conv_handler = ConversationHandler(
        entry_points=[...
                      CommandHandler('red', red)],

```
```
def red(update,context):
    if update.message.chat_id in ids:
        global comando_linux, respuesta
        comando_linux = 'iwgetid'
        respuesta = 'La red a la que está conectado el servidor ' + terminal_texto('hostname') + ' es: '

        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        return TIPO
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/red01.jpg" alt="red01" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/red02.jpg" alt="red02"/><br>

[Inicio](#top)<br>

<a name="arquitectura"></a>

### Comando `/arquitectura`
En este caso usamos el comando linux [`arch`](https://linux.die.net/man/1/arch) que nos devuelve la arquitectura del sistema del servidor.
```
    conv_handler = ConversationHandler(
        entry_points=[...
                      CommandHandler('arquitectura', arquitectura)],          
```
```
def arquitectura(update,context):
    if update.message.chat_id in ids:
        global comando_linux, respuesta
        comando_linux = 'arch'
        respuesta = 'La arquitectura del sistema del servidor ' + terminal_texto('hostname') + ' es: '

        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        return TIPO
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/arquitectura01.jpg" alt="arquitectura01" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/arquitectura02.jpg" alt="arquitectura02"/><br>

[Inicio](#top)<br>

<a name="version"></a>

### Comando `/version`
Para conocer la versión de Linux del servidor tenemos que ejecutar la linea de comando [`uname -r](https://linux.die.net/man/1/uname) en el terminal de este.
```
    conv_handler = ConversationHandler(
        entry_points=[...
                      CommandHandler('version', version)],      
```
```
def version(update,context):
    if update.message.chat_id in ids:
        global comando_linux, respuesta
        comando_linux = 'cat /proc/version'
        respuesta = 'La versión de Linux del servidor ' + terminal_texto('hostname') + ' es: '

        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        return TIPO
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/version01.jpg" alt="version01" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/version02.jpg" alt="version02"/><br>

[Inicio](#top)<br>

<a name="usuarios"></a>

### Comando `/usuarios`
Con el comando [`who`](https://linux.die.net/man/1/finger) podemos conocer los usuarios conectados al servidor en ese momento.
```
    conv_handler = ConversationHandler(
        entry_points=[...
                      CommandHandler('usuarios', usuarios)],
```
```
def usuarios(update,context):
    if update.message.chat_id in ids:
        global comando_linux, respuesta
        comando_linux = 'who'
        respuesta = 'Los usuarios que están conectados al servidor ' + terminal_texto('hostname') + ' son: '

        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        return TIPO
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/usuarios01.jpg" alt="usuarios01" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/usuarios02.jpg" alt="usuarios02"/><br>

[Inicio](#top)<br>

<a name="espacio"></a>

### Comando `/espacio`
Podemos conocer el espacio del sistema del servidor con el comando de linux [`df -h`](https://linux.die.net/man/1/df) que nos muestra el espacio total, ocupado y libre en nuestro sistema en Gb, Mb y Kb. 
```
    conv_handler = ConversationHandler(
        entry_points=[...
                      CommandHandler('espacio', espacio)],
```
```
def espacio(update,context):
    if update.message.chat_id in ids:
        global comando_linux, respuesta
        comando_linux = 'df -h'
        respuesta = 'El espacio del servidor ' + terminal_texto('hostname') + ' es: '

        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        return TIPO
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/espacio01.jpg" alt="espacio01" width="350"/><br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/espacio02.jpg" alt="espacio02" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/espacio03.jpg" alt="espacio03"/><br>

[Inicio](#top)<br>

<a name="memoria"></a>

### Comando `/memoria`
Para obtener datos de la memoria como el total, lo usado o libre, entre otra información, ejecutamos el comando [`free -h`](https://raiolanetworks.es/blog/memoria-ram-usada-memoria-ram-libre-linux/).
```
    conv_handler = ConversationHandler(
        entry_points=[...
                      CommandHandler('memoria', memoria)],
```
```
def memoria(update,context):
    if update.message.chat_id in ids:
        global comando_linux, respuesta
        comando_linux = 'free -h'
        respuesta = 'La memoria del servidor ' + terminal_texto('hostname') + ' es: '

        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        return TIPO
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/memoria01.jpg" alt="memoria01" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/memoria02.jpg" alt="memoria02"/><br>

[Inicio](#top)<br>

<a name="procesos"></a>

### Comando `/procesos`
Para conocer los procesos que hay en ejecución en el servidor, hacemos que el bot ejecute el comando linux [`ps`](https://linux.die.net/man/1/ps).
```
    conv_handler = ConversationHandler(
        entry_points=[...
                      CommandHandler('procesos', procesos)],
```
```
def procesos(update,context):
    if update.message.chat_id in ids:
        global comando_linux, respuesta
        comando_linux = 'ps'
        respuesta = 'Los procesos que se están ejecutando en el servidor ' + terminal_texto('hostname') + ' son: '

        keyboard = [['Texto', 'Imagen']]
        update.message.reply_text(
            '¿Quieres la respuesta en texto o en imagen?',
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        return TIPO
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```

<img src="https://github.com/helee18/python_sysadmin/blob/master/images/procesos01.jpg" alt="procesos01" width="350"/> <img src="https://github.com/helee18/python_sysadmin/blob/master/images/procesos02.jpg" alt="procesos02"/><br>

[Inicio](#top)<br>

<a name="servicios"></a>

### Comandos (`/estado_servicio`, `/iniciar_servicio`, `/parar_servicio` y `/reiniciar_servicio`)
Podemos administrar los servicios instalados en el servidor viendo su estado, iniciandolos, parandolos o reiniciandolos. Podemos configurar el bot para que lo haga pasandole un comando diciendo lo que queremos que haga junto con un argumento que será el servicio que queremos consultar o modificar su estado.

Para poder administrar los servicios sin necesitar contraseña, primero creamos un usuario, en mi caso `bot`, con [`adduser`](https://linux.die.net/man/8/adduser) y después, con [`passwd -d`](https://linux.die.net/man/1/passwd) le borramos la contraseña.
```
$ sudo adduser bot
$ sudo passwd -d bot
```

Podemos necesitar que el usuario tenga permisos para poder instalar con `apt-get install` servicios en el servidor. Para ello editamos el archivo `/etc/sudoers` y añadimos que los usuarios del grupo (`bot`) puedan ejecutar en el host (`NOMBRE_SERVIDOR`) como `root` del gurpo `root` el comando `/usr/bin/apt-get install` del cualquier servicio (`*`). También añadimos `/usr/bin/apt-get upodate` para poder hacerlo al principio del todo.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/sudoers01.png" alt="apt-get" width="350"/><br>

Después tenemos que editar el archivo `/etc/sudoers` donde añadimos el usuario (`bot`) del grupo (`bot`), el servidor (`NOMBRE_SERVIDOR`), que no va a tener contraseña (`NO PASSWD`) y los comandos que ejecutará sin contraseña.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/sudoers02.png" alt="servicios" width="350"/><br>

En el caso de los servicios, lo haremos de otra forma. Tendremos cuatro comandos distintos que llamarán a la misma función e incluirán que se puedan pasar argumentos [`pass_args=True`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html#telegram.ext.CommandHandler.pass_args) para que se introduzca un argumento con el nombre del servicio.
```
    conv_handler = ConversationHandler(
        entry_points=[...
                      CommandHandler('estado_servicio', servicios, pass_args=True),
                      CommandHandler('iniciar_servicio', servicios, pass_args=True),
                      CommandHandler('parar_servicio', servicios, pass_args=True),
                      CommandHandler('reiniciar_servicio', servicios, pass_args=True)],               
```

Aunque podrías hacerlo con la conversación con el bot, desarrollaremos la función de otra forma. 

Con el condicional [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) comprobaremos que se pasa un argumento. Para referirnos a los argumentos usamos [`context.args`](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Types-of-Handlers#commandhandlers-with-arguments) y calculamos cuantos son con [`len()`](https://docs.python.org/3/library/functions.html#len). En caso de que no sea un argumento, el bot nos responde con un aviso y nos da un ejemplo de como tenemos que hacer uso del comando.
```
def servicios(update,context):
    if update.message.chat_id in ids:
        if len(context.args) == 1:
            
        else:
            # En caso de que no se pase un argumento, notificarlo
            update.message.reply_text(
                'Se debe especificar el servicio (apache2 o ssh).\n\n'
                'Ejemplo:\n/reiniciar_servicio apache2'
            ) 
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/sin_nombre_servicio.jpg" alt="sin_nombre_servicio" width="350"/><br>

En el caso de que si que se pase un argumento, veremos cuál es el comando que se ha pasado comprobando con [`in`](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) si, por ejemplo, `estado_servidor` se encuentra en la texto recibido [`update.message.text`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.text).

Segun lo que pidamos el comando linux será uno u otro. En todos los casos lo haremos con [`/etc/init.d/SERVICIO`](https://www.linuxtotal.com.mx/index.php?cont=info_admon_003) porque asi nos devuelve siempre un mensaje para confirmar si se ha ejecutado el comando. Usamos [`context.args[0]`](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Types-of-Handlers#deep-linking-start-parameters) para referirnos al parametro que se ha pasado, el servicio, y añadirlo a la linea de comando que el bot va a ejecutar.

En el caso del estado, añadimos a la linea de comando [`head -n3`](https://linux.die.net/man/1/head) para que solo nos muestre las tres primeras línesas donde te dice el estado y desde cuándo.
```
            if 'estado_servicio' in update.message.text:
                # Comando para ver el estado
                comando_linux = '/etc/init.d/' + context.args[0] + ' status | head -n3'
            elif 'iniciar_servicio' in update.message.text:
                # Comando para iniciar
                comando_linux = 'sudo /etc/init.d/' + context.args[0] + ' start'
            elif 'parar_servicio' in update.message.text:
                # Comando para parar
                comando_linux = 'sudo /etc/init.d/' + context.args[0] + ' stop'
            else:
                # Comando para reiniciar
                comando_linux = 'sudo /etc/init.d/' + context.args[0] + ' restart'
```

Como en el resto de comandos, preguntamos si queremos `Texto` o `Imagen` y hacemos que el teclado solo muestre esas dos opciones.
```
            keyboard = [['Texto', 'Imagen']]
            update.message.reply_text(
                '¿Quieres la respuesta en texto o en imagen?',
                reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
            )
```

En este caso devolvemos un estado distinto que será `TIPO_SERVICIOS` el cual tenemos que declarar al principio del script y definir en el controlador de la conversación donde llamaremos a distintas funciones que en el otro estado.
```
            return TIPO_SERVICIOS
```
```
TIPO, TIPO_SERVICIOS = range(2)
```
```
        states={
            ...

            TIPO_SERVICIOS: [MessageHandler(Filters.regex('^Texto$'), texto_servicios),
                             MessageHandler(Filters.regex('^Imagen$'), imagen_servicios)],
        },
```

Definimos las funciones `texto_servicios` e `imagen_servicios` que van a ser iguales que `texto` e `imagen` excepto porque no haremos uso de la variable `respuesta` ya que no la hemos creado en las funciones correspondientes a los servicios. 

Además, en `texto_servicios` haremos uso de las excepciones de linux para intentar ejecutar el comando ([`try`](https://docs.python.org/3/reference/compound_stmts.html#try)) y si funciona mostrar el mensaje pero si da fallo ([`except`](https://docs.python.org/3/reference/compound_stmts.html#except)), mostrar un mensaje con cómo debe mandarse el mensaje al bot. Por último siempre saldremos de la conversación. 

Tanto en el caso de que funcione cómo en el caso de que no, tenemos que eliminar el botón con las opciones de `Texto` o `Imagen` con [`ReplyKeyboardRemove`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardremove.html).
```
def texto_servicios(update,context):
    try:
        respuesta_sistema = terminal_texto(comando_linux)

        update.message.reply_text(
            respuesta_sistema,
            reply_markup=ReplyKeyboardRemove()
        )
    except:
        update.message.reply_text(
            'Tiene que introducirse el nombre exacto del servicio (apache2 o ssh)',
            reply_markup=ReplyKeyboardRemove()
        )
    finally:
        return ConversationHandler.END
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/error_texto_servicio.jpg" alt="error_texto_servicio" width="350"/><br>

En el caso de `imagen_servicios` será una mezcla entre `texto_servicios` e `imagen` ya que podemos tener problemas con la imagen pero también puede darnos error el hecho de introducir el nombre del servicio mal. 

Por esto mismo, en la respuesta del bot en el caso de que haya problemas comentaremos que puede ser por culpa de introducir mal el nombre del servicio.
```
def imagen_servicios(update,context):
    # Intentamos ejecutar el comando
    try:
        # Llamamos a la funcion terminal, que ejecuta el comando pasado
        terminal_imagen(comando_linux)

        # Si aun no existe esperamos un segundo
        if not os.path.exists('image.png'): 
            time.sleep(1)

        # Respondemos con la imagen
        update.message.bot.send_photo(
            chat_id=update.message.chat_id, 
            photo=open('image.png', 'rb'),
            # Quitamos las opciones del teclado
            reply_markup=ReplyKeyboardRemove()
        ) 
    except:
        # En caso de que haya algun error
        update.message.reply_text(
            '-No se puede mostrar la imagen- \n'
            'Puede que no se haya introducido el nombre exacto del servicio (apache2 o ssh)',
            # Quitamos las opciones del teclado
            reply_markup=ReplyKeyboardRemove()
        )
    finally:
        # Terminamos la conversación
        return ConversationHandler.END
```
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/error_imagen_servicio.jpg" alt="error_imagen_servicio" width="350"/><br>

---

<img src="https://github.com/helee18/python_sysadmin/blob/master/images/estado_servicio_01.jpg" alt="estado_servicio_01" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/estado_servicio_02.jpg" alt="estado_servicio_02"/><br>

<img src="https://github.com/helee18/python_sysadmin/blob/master/images/iniciar_servicio_01.jpg" alt="iniciar_servicio_01" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/iniciar_servicio_02.jpg" alt="iniciar_servicio_02"/><br>

<img src="https://github.com/helee18/python_sysadmin/blob/master/images/parar_servicio_01.jpg" alt="parar_servicio_01" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/parar_servicio_02.jpg" alt="parar_servicio_02"/><br>

<img src="https://github.com/helee18/python_sysadmin/blob/master/images/reiniciar_servicio_01.jpg" alt="reiniciar_servicio_01" width="350"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/reiniciar_servicio_02.jpg" alt="reiniciar_servicio_02"/><br>

[Inicio](#top)<br>