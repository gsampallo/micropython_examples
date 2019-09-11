#How to use 4067 analog multiplexer with MicroPython and NodeMCU
# Check the blog page https://www.gsampallo.com/blog/?p=475
from machine import Pin, ADC
import time

s0 = Pin(2, Pin.OUT)
s1 = Pin(0, Pin.OUT)
s2 = Pin(4, Pin.OUT)
s3 = Pin(5, Pin.OUT)

adc = ADC(0)

multiplexor = [   
    [0,0,0,0], #0
    [1,0,0,0], #1
    [0,1,0,0], #2
    [1,1,0,0], #3
    [0,0,1,0], #4
    [1,0,1,0], #5
    [0,1,1,0], #6
    [1,1,1,0], #7
    [0,0,0,1], #8
    [1,0,0,1], #9
    [0,1,0,1], #10
    [1,1,0,1], #11
    [0,0,1,1], #12
    [1,0,1,1], #13
    [0,1,1,1], #14
    [1,1,1,1], #15
]



def valor_analogico(cx):
    s0.value(multiplexor[cx][0])
    s1.value(multiplexor[cx][1])
    s3.value(multiplexor[cx][3])
    s2.value(multiplexor[cx][2])

    lectura = adc.read()     

    return lectura

pinCx = list(range(0,15))

while True: 


    c0 = valor_analogico(0)  
    c1 = valor_analogico(1)  

    print(c0,c1)

    time.sleep_ms(250)