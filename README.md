![Python para Sysadmin con Telegram](https://github.com/helee18/python_sysadmin/blob/master/images/titulo.png)
---
**Telegram**, una plataforma de mensajeria, tiene la opción de crear bots de todo tipo. Los administradores de sistemas pueden hacer uso de estos bots para manipular o consultar el estado de un servidor creando uno. Para ello **Python** es un lenguaje de programación multiplataforma con el que se puede programar las funciones que queremos que resuelva el bot.

- <a href="#crear_bot">Crear un bot de Telegram</a>
- <a href="#instalar_python_telgram_bot">Instalación python-telegram-bot</a>

<section id="crear_bot"></section>

## Crear un bot de Telegram

El primer paso para crear un bot iniciar **BotFather** desde Telegram.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/01_conectar_botfather.png" alt="BotFather" width="450"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/02_start_botfather.png" alt="start" width="450"/><br>

Creamos un nuevo bot con `/newbot` y le ponemos nombre al bot y al usuario.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images//03_nombre_bot.png" alt="newbot" width="450"/><br>

Desde el BotFather se puede modificar los bots. Por ejemplo, se puede cambiar el nombre con `/setname` y añadir una foto con `/setuserpic`.<br>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/04_cambio_nombre.png" alt="setname" width="450"/>
<img src="https://github.com/helee18/python_sysadmin/blob/master/images/05_cambio_foto.png" alt="setuserpic" width="450"/>


<section id="instalar_python_telgram_bot"></section>

## Instalación python-telegram-bot

**Python-telegram-bot** que presenta una serie de clases de alto nivel para hacer el desarrollo de bots mas facil.
```
$ pip install python-telegram-bot --upgrade
```

Otra forma de instalarlo es clonando el repositorio de github.
```
$ git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
$ cd python-telegram-bot/
```
- Cuando se intenta instalar puede que de un fallo:
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
- Por lo que tendremos que instalar manualmente las `setuptools` y después intalarlo:
```
$ sudo apt-get install python3-setuptools -y
$ sudo python3 setup.py install
```
- Durante la instalación aparece lo siguiente:
```
WARNING: The tornado.speedups extension module could not be compiled. No C extensions are essential for Tornado to run, although they do result in significant speed improvements for websockets.
The output above this warning shows how the compilation failed.
```
- Esto quiere decir que no se pudo compilar la extensión `tornado.speedups`.
Y segun el sistema operativo te dice el comando a ejecutar para instalar lo necesario para una mejora de velocidad:
```
$ sudo apt-get install build-essential python-dev
```
