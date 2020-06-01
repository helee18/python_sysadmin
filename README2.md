

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
    - [`Comando /espacio`](#espacio)
    - [`Comando /arquitectura`](#arquitectura)
    - [`Comando /version`](#version)
    - [`Comandos /estado_servicio, /iniciar_servicio, /parar_servicio y /reiniciar_servicio`](#servicios)

<br>












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
[Inicio](#top)<br>

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

Por último hacemos que el bot responda con el resultado del comando ejecutado, en este caso la ip del servidor.
```
        update.message.reply_text(
            'La red a la que está conectado el servidor ' + nombre + ' es: \n' + red
        )
```
[Inicio](#top)<br>

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
[Inicio](#top)<br>

<a name="espacio"></a>

### Comando `/espacio`
Para conocer el espacio del sistema del servidor, añadimos un nuevo [`Handler`](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.handler.html) dentro de la función principal que llama a su función correspondiente.
```
    updater.dispatcher.add_handler(CommandHandler("espacio", espacio))
```

En la función comprobamos si el usuario está autorizado para conocer información del servidor, pedimos el nombre de este y llamamos a la función `terminal` en la que se ejecutará el comando [`df -h`](https://linux.die.net/man/1/df) mostrandonos el espacio total, ocupado y libre en nuestro sistema en Gb, Mb y Kb. 
```
def espacio(update,context):
    if update.message.chat_id in ids:
        nombre = terminal('hostname')
        espacio = terminal('df -h')
```

El bot nos responde con la respuesta del sistema, en este caso el espacio de este.
```
        update.message.reply_text(
                'El espacio del servidor ' + nombre + ' son: \n' + espacio
            )
```

En el caso de que no estuviera el usuario autorizado, mensamos un mensaje informando de ello.
```
    else:
        update.message.reply_text(
            'No perteneces a los usuarios autorizados'
        )
```
[Inicio](#top)<br>

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
[Inicio](#top)<br>

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
[Inicio](#top)<br>

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