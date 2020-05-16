![Python para Sysadmin con Telegram](https://github.com/helee18/python_sysadmin/blob/master/images/titulo.png)
---
[Telegram](https://web.telegram.org/), una plataforma de mensajeria, tiene la opción de crear bots de todo tipo. Los administradores de sistemas pueden hacer uso de estos bots para manipular o consultar el estado de un servidor creando uno. Para ello se puede hacer uso de [Python](https://www.python.org/), un lenguaje de programación multiplataforma, programando las funciones que queremos que resuelva el bot.

- Crear un bot de Telegram
- Instalar python-telegram-bot
- Elementos básicos del script del bot

<br>

## Crear un bot de Telegram

El primer paso para crear un bot iniciar **BotFather**, el bot principal que reconoce una serie de comandos, desde Telegram. Como respuesta, nos devuelve el `token` identificativo de nuestro bot.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/01_conectar_botfather.png" alt="BotFather" width="450"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/02_start_botfather.png" alt="start" width="450"/><br>

Creamos un nuevo bot con `/newbot` y le ponemos nombre al bot y al usuario.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images//03_nombre_bot.png" alt="newbot" width="450"/><br>

Desde el BotFather se puede modificar los bots. Por ejemplo, se puede cambiar el nombre con `/setname` y añadir una foto con `/setuserpic`.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/04_cambio_nombre.png" alt="setname" width="450"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/05_cambio_foto.png" alt="setuserpic" width="450"/>

<br>

## Instalar python-telegram-bot

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

### [Instalación con pip](https://github.com/helee18/python_sysadmin/blob/master/setup.py)
Instalamos [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) que presenta una serie de clases de alto nivel para hacer el desarrollo de bots mas facil.
```
$ sudo apt-get install python3-pip
$ pip3 install python-telegram-bot --upgrade
```

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
<br>

## [Elementos básicos del script del bot](https://github.com/helee18/python_sysadmin/blob/master/bot.py)

### Importar módulos
Al principio del script importamos los módulos de python necesarios. En este caso importamos el módulo `logging` para el registro y los submódulos `Updater`, `CommandHandler`, `MessageHandler` y `Filters` de la librería `telegram.ext` a la que podemos acceder gracias a python-telegram-bot.

### Logging
Habilitamos el registro del historial de eventos. Con `format` configuramos salga la fecha y hora, el nombre del bot, el nivel de registro y el mensaje que muestra. 

La librería `logging` tiene distintos niveles `Debug`, `Info`, `Warning`, `Error` y `Critical` de menos a mayor importancia.

En caso de que no configuremos el nivel, por defecto está configurado para mostrar mensajes de gategoría mínima `warning`. Configuramos que el nivel minimo sea `info` para que muestre también mensajes que no sean algo inesperado, como que el sistema funcione correctamente.
```
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
```

Para registrar las acciones durante la ejecución del programa haremos uso de la funcion `logging.getLogger(nombre del logger)` y como nombre del logger pondremos `__name__` que, en un modulo, es el nombre de este en el espacio de nombres de Python.
```
logger = logging.getLogger(__name__)
```

Después, para el registro de errores definiremos una función en la que haremos uso de `logger.warning`.

### Función main
Al final del codigo, llamamos a la función principal `main`, en la cual tendremos todo el codigo del bot. Para llamar a la función, comprobamos que el codigo se esta ejecutando en el script principal, y no sea importado en otro. Esto se comprueba comparando que el atributo `__name__` con `__main__` ya que `__name__` adopta el nombre de `__main__` cuando se ejecuta en el script principal o adopta le nombre del modulo importado cuando no es así.
```
if __name__ == '__main__':
    main()
```

### Introducción del token
Definimos la función `main` y dentro de esta programamos el script del bot. Lo primero que tenemos que definir el `updater`, donde introducimos nuestro `token`.

`Updater` es una clase que ayuda al programador a codificar el bot. Recibe actualicaciones de telegram y las manda al `Dispatcher`. El `Dispatcher` maneja las actualizaciones y las manda a los `Handlers`. 

Añadimos `user_content=True` para usar las nuevas devoluciones basadas en contexto (`context based callbacks`). Puede producirse un fallo de uso de la antigua API dependiendo de la versión si no se añade. En la versión 13 no hace falta definirlo porque por defecto es `True`.

CallbackContext es un objeto que contiene contexto adicional de update, error o job. Esto almacena chat_data, user_data, job, error y argumentos.
```
def main():
    updater = Updater('TOKEN', use_context=True)
```

### Inicio bot y espera
Le indicamos al bot que inicie la espera de mensajes por parte de Telegram.
```
updater.start_polling()
```

También le decimos que se bloquee y se quede a la espera hasta recibir mensajes. Esto lo hará hasta que, con Ctrl-C, paremos el bot.
```
updater.idle()
```

### Log de errores
Podemos añadir un controlador de errores en los `Dispatcher`. Dentro de la función `main` llamamos a la función.
```
updater.dispatcher.add_error_handler(error)
```

Fuera definimos la función en la que hacemos uso de `logger` previamente definido y `warning` para el registro de mensajes a este nivel, donde funciona correctamente pero se produce una situación inesperada o se predice un problema futuro.
```
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
```

### Comandos no definidos
Cuando el bot reciba comandos que no entienda, los repitirá.

Siempre que querramos definir un comando de entrada que tenga que llamar a una función lo haremos dentro de la función principal (`main`) con `add_handler`. Asi registramos un nuevo controlador (`handler`).

En este caso
```
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
```


```
def echo(update, context):
    update.message.reply_text(update.message.text)
```