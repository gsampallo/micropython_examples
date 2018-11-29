# micropython_examples

Se puede encontrar los ejemplos realizados.

MQTT - Publish (dentro de la carpeta mqtt_publish)
Vemos como utilizar la biblioteca umqtt para conectarnos a un servidor broker, en nuestro ejemplo utilizaremos el servidor de Eclipse: iot.eclipse.org para realizar las experiencias.
Cada que vez que se presiona el boton se publica en el servidor broker; los datos son vistos en un pequeño script en Python corriendo en la pc.

MQTT - Subscribe (dentro de la carpeta mqtt_subscribe)
En esta oportunidad tenemos el ejemplo de como recibir información desde otro dispositivo IoT hacia el nodemcu por medio de mqtt.
El dispositivo que se utiliza para transmitir datos es un modulo de temperatura y humedad dht con un esp8266 (esp-01) pueden encontrar el codigo aca: https://github.com/gsampallo/mqtt_modulodht11

Control de Motor DC (dentro de la carpeta motor_driver)
Como controlar la direccion de un motor DC con micropython sin necesidad de una libreria extra.
Se conecta segun el siguiente diagrama:

![alt text](https://raw.githubusercontent.com/gsampallo/micropython_examples/master/motor_driver/motor_python.png "Diagrama")

Controlar el Motor DC con MQTT (dentro de la carpeta mqtt_motor_driver)
Determina la direccion del giro del motor en base al mensaje que reciba desde un servidor broker. Utiliza la misma conexion que el ejemplo anterior.