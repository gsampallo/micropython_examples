import json
import network
import urequests
import mcp
import time
io = mcp.MCP23017()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect('linksys', 'perromateo')

outPins = list(range(0,16))
for pinNum in outPins:
    io.setup(pinNum, mcp.OUT)

segmento1 = [   
    [4,5,6,8,9,10],
    [4,10],
    [5,4,7,8,9],
    [5,4,7,10,9],
    [6,7,4,10],
    [5,6,7,10,9],
    [5,6,7,8,9,10],
    [5,4,10],
    [4,5,6,7,8,9,10],
    [4,5,6,7,10]
]

segmento2 = [
    [0,1,2,12,13,14],
    [0,14],
    [0,1,3,12,13],
    [1,0,3,14,13],
    [2,3,0,14],
    [1,2,3,14,13],
    [1,2,3,12,13,14],
    [1,0,14],
    [0,1,2,3,12,13,14],
    [0,1,2,3,14]
]

digito1 = 8
digito2 = 8

for numero in segmento2[digito2]:
    io.output(numero,1)
for numero in segmento1[digito1]:
    io.output(numero,1)

digito1_old = digito1
digito2_old = digito2

while True:

    for numero in segmento2[8]:
        time.sleep_ms(100)
        io.output(numero,0)

    for numero in segmento1[8]:
        time.sleep_ms(100)
        io.output(numero,0)
        
    
    #time.sleep_ms(100)

    r = urequests.get("http://api.openweathermap.org/data/2.5/weather?q=Corrientes, AR&units=metric&appid=abdd0d89cab1704cf4fc68692386960f").json()

    print(r["main"]["temp"])

    temp = r["main"]["temp"]
    countdown_str = str(temp)
    digito1 = int(countdown_str[0:1])
    digito2 = int(countdown_str[1:2])

    for numero in segmento2[digito2]:
        io.output(numero,1)
        time.sleep_ms(100)
    for numero in segmento1[digito1]:
        io.output(numero,1)
        time.sleep_ms(100)

    digito1_old = digito1
    digito2_old = digito2

    #lista = list(range(0,4))
    #for i in lista:
    #    print(i)
    #    time.sleep_ms(i*1000)
    time.sleep_ms(5*1000) #esperamos 5 minutos antes de volver a consultar
