from machine import Pin
import time
import wlan
from umqtt.simple import MQTTClient

motorA1 = Pin(14, Pin.OUT)
motorA2 = Pin(12, Pin.OUT)

wlan.do_connect()

def manejoMotor(topico,mensaje):
    print(mensaje[0])
    if(mensaje[0] == 48):
        motorA1.off()
        motorA2.off()
    if(mensaje[0] == 49):
        motorA1.on()
        motorA2.off()
    if(mensaje[0] == 50):
        motorA1.off()
        motorA2.on()

cliente = MQTTClient('microp_demo','iot.eclipse.org')
cliente.set_callback(manejoMotor)
cliente.connect()
cliente.subscribe(b"motor")

while True:
    cliente.check_msg()
    time.sleep_ms(100)