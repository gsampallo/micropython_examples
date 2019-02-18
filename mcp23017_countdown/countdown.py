import mcp
import time
io = mcp.MCP23017()

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

countdown = 60
while True:
    countdown_str = str(countdown)
    if(countdown >= 10):
        valor1 = int(countdown_str[0:1])
        valor2 = int(countdown_str[1:2])
    else:
        valor1 = 0
        valor2 = int(countdown_str[0:1])

    for numero in segmento1[valor1]:
        io.output(numero,1)
    for numero in segmento2[valor2]:
        io.output(numero,1)

    time.sleep_ms(1000)
    
    for numero in segmento1[valor1]:
        io.output(numero,0)        
    for numero in segmento2[valor2]:
        io.output(numero,0)        
    
    if(countdown > 0):
        countdown = countdown - 1
    else:
        countdown = 60