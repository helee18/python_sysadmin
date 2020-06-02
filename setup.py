#!/usr/bin/env python

# Solo para el ejemplo basico de bot, en el bot hace falta instalar 
# y configurar imagemagick

# Importamos el modulo os
import os

os.system("sudo apt-get update")

# Instalamos el paquete de python para entornos de desarrollo
os.system("sudo apt-get install python3-venv -y")

# Creamos un entorno de desarrollo virtual
os.system("python3 -m venv bot-venv")

# Activamos el entorno
os.system("source bot-venv/bin/activate")

# Instalamos el gestor de paquetes de python
os.system("sudo apt-get install python3-pip -y")

# Instalamos python-telegram-bot
os.system("pip3 install python-telegram-bot --upgrade")

# Ejecutamos el script de nuestro bot
#os.system("python3 ejemplo-bot.py")
