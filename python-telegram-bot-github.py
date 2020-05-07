#!/usr/bin/env python

# Importamos la libreria os
import os

os.system("apt-get update")

# Clonamos el repositorio de python-telegram-bot
os.system("git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive")

# Instalamos las herramientas de python
os.system("apt install python3-setuptools -y")

# Instalamos
os.system("cd python-telegram-bot/")
os.system("python3 setup.py install")
os.system("apt install build-essential python-dev -y")