import wlan
import machine
import ssd1306
import time
from umqtt.simple import MQTTClient

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
wlan.do_connect()

def mostrar(topico,mensaje):
    oled.fill(0)
    oled.text(mensaje,0,0)
    oled.show()

cliente = MQTTClient('microp_demo','iot.eclipse.org')
cliente.set_callback(mostrar)
cliente.connect()
cliente.subscribe(b"temperatura1")

while True:
    cliente.check_msg()
    time.sleep_ms(100)