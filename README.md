# micropython_examples

Se puede encontrar los ejemplos realizados.

## MQTT - Publish (dentro de la carpeta mqtt_publish)
Vemos como utilizar la biblioteca umqtt para conectarnos a un servidor broker, en nuestro ejemplo utilizaremos el servidor de Eclipse: iot.eclipse.org para realizar las experiencias.
Cada que vez que se presiona el boton se publica en el servidor broker; los datos son vistos en un pequeño script en Python corriendo en la pc.

## MQTT - Subscribe (dentro de la carpeta mqtt_subscribe)
En esta oportunidad tenemos el ejemplo de como recibir información desde otro dispositivo IoT hacia el nodemcu por medio de mqtt.
El dispositivo que se utiliza para transmitir datos es un modulo de temperatura y humedad dht con un esp8266 (esp-01) pueden encontrar el codigo aca: https://github.com/gsampallo/mqtt_modulodht11

## Control de Motor DC (dentro de la carpeta motor_driver)
Como controlar la direccion de un motor DC con micropython sin necesidad de una libreria extra.
Se conecta segun el siguiente diagrama:

![alt text](https://raw.githubusercontent.com/gsampallo/micropython_examples/master/motor_driver/motor_python.png "Diagrama")

## Controlar el Motor DC con MQTT (dentro de la carpeta mqtt_motor_driver)
Determina la direccion del giro del motor en base al mensaje que reciba desde un servidor broker. Utiliza la misma conexion que el ejemplo anterior.

## MCP23017 - Expansor de IO

Utilizamos el chip MCP23017 para extender hasta 16 IO digitales en el NodeMCU. Para ello utilizamos la libreria https://github.com/ShrimpingIt/micropython-mcp230xx donde ya se encuentran implementados los metodos para usar el chip.
Se conecta segun el siguiente esquema:
![alt text](https://raw.githubusercontent.com/gsampallo/micropython_examples/master/mcp23017/micropython_mcp23017.jpg "Diagrama")

Dentro de la carpeta mcp23017 se encuentra el codigo del ejemplo.

## Display de 7 segmentso con MCP23017

Con los beneficios que nos otorga el chip MCP23017, podemos manejar dos display de 7 segmentos sin problema, se conecta de la siguiente manera:
![alt text](https://raw.githubusercontent.com/gsampallo/micropython_examples/master/mcp23017_7segment/mcp23017_7segmentos.jpg "Diagrama")

Luego creamos un array de elementos para cada display donde indicamos que pin es necesario encender para mostrar cada numero.
Por ejemplo, para el nro. de 2 sera necesario activar los pins [5,4,7,8,9]; esto puede variar si cambia la forma de conexion.

## LCD

Conectar los pines muy sencillo; SCL del display va a D1 y SDA a D2; el display esta conectado a una fuente externa de 5v, tener en cuenta el comun del GND.
La libreria que se utilizo es https://github.com/dhylands/python_lcd

## MOTORES PASO A PASO
Dentro de la carpeta stepper_motor se puede encontrar el ejemplo. Se utiliza el driver A4988 para controlar un motor paso a paso, realizando un giro en cada dirección.
![alt text](https://raw.githubusercontent.com/gsampallo/micropython_examples/master/stepper_motor/stepper_motor.jpg "Diagrama")