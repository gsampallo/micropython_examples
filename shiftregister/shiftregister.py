from machine import Pin
import time

data = Pin(13, Pin.OUT, value=0)
clock = Pin(15, Pin.OUT, value=0)
latch = Pin(14, Pin.OUT, value=0)

while True:
    for value in [1,3,7,15,31,63,127,255]:
        bits = [value >> i & 1 for i in range(7,-1,-1)]
        for i in range(7,-1,-1):
            print(bits[i])
            data.value(bits[i])
            clock.value(1)
            clock.value(0)
        latch.value(1)
        latch.value(0)

        time.sleep_ms(200)
