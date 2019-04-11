from machine import Pin, SPI
import max7219
import time

hspi = SPI(1, baudrate=10000000, polarity=0, phase=0)
display = max7219.Max7219(hspi, Pin(15))
display.clear()

while(True):

    i = 0
    while(i < 99999999):
        display.write_num(i)
        i = i + 1
        time.sleep_ms(250)