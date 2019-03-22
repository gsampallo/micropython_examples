from machine import Pin
import time

pinEnabled = Pin(5, Pin.OUT,value=0)
pinStep = Pin(4, Pin.OUT)
pinDirection = Pin(0, Pin.OUT)

stepsPerRevolution = 200

while True:

    pinDirection.on()

    for i in range(0,stepsPerRevolution):
        pinStep.on()
        time.sleep_ms(10)
        pinStep.off()
        time.sleep_ms(10)

    pinDirection.off()

    for i in range(0,stepsPerRevolution):
        pinStep.on()
        time.sleep_ms(10)
        pinStep.off()
        time.sleep_ms(10)    