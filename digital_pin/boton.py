from machine import Pin

led = Pin(15,Pin.OUT)
button = Pin(4,Pin.IN,Pin.PULL_UP)
while True:
    if(button.value()):
        led.off()
    else:
        led.on()
