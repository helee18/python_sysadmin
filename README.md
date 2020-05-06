## Proyecto Integrado: Python para Sysadmin con Telegram
### Helena Gutiérrez Ibáñez - ASIR
---
```
git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
```
```
cd python-telegram-bot/
```
```
sudo python3 setup.py install
```
```
python3 setup.py install
Traceback (most recent call last):
  File "setup.py", line 8, in <module>
    from setuptools import setup, find_packages
ModuleNotFoundError: No module named 'setuptools'
```
```
sudo apt-get install python3-setuptools -y
```
```
sudo python3 setup.py install
```
```
WARNING: The tornado.speedups extension module could not be compiled. No C extensions are essential for Tornado to run, although they do result in significant speed improvements for websockets.
The output above this warning shows how the compilation failed.
```
```
sudo apt-get install build-essential python-dev -y
```
