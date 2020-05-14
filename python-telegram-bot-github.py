#!/usr/bin/env python

# Importamos el modulo os
import os

os.system("apt-get update")

# Instalamos el paquete de python para entornos de desarrollo
os.system("apt-get install python3-venv -y")

# Creamos un entorno de desarrollo virtual
os.system("python3 -m venv bot-venv")

# Activamos el entorno
os.system("source bot-venv/bin/activate")

# Clonamos el repositorio de python-telegram-bot
os.system("git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive")

# Instalamos las herramientas de python
os.system("apt install python3-setuptools -y")

# Instalamos
os.chdir("./python-telegram-bot/")
os.system("python3 setup.py install")
os.system("apt-get install build-essential python-dev -y")

# Ejecutamos el script de nuestro bot
os.system("python3 bot.py")

# Desactivamos el entorno de desarrollo
os.system("deactivate")