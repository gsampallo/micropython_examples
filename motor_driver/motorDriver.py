import time
from machine import Pin

motorA1 = Pin(14, Pin.OUT)
motorA2 = Pin(12, Pin.OUT)

while True:
    motorA1.on();
    motorA2.off();
    time.sleep_ms(2000)
    motorA1.off();
    motorA2.on();
    time.sleep_ms(2000)    