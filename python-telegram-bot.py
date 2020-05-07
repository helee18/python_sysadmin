#!/usr/bin/env python

# Importamos la libreria os
import os

os.system("apt-get update")

# Instalamos el gestor de paquetes de python
os.system("apt install python-pip -y")

# Instalamos python-telegram-bot
os.system("pip install python-telegram-bot --upgrade")
