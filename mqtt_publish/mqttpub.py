from machine import Pin
import time
from umqtt.simple import MQTTClient
import wlan

wlan.do_connect()

cliente = MQTTClient('cliente_micropython','iot.eclipse.org')
cliente.connect()

boton = Pin(5,Pin.IN,Pin.PULL_UP)

while True:
    if(boton.value() == 0):
        cliente.publish('micropython/demo','Hola desde MicroPython')
        time.sleep_ms(500)

