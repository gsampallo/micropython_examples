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

while True:
    for i in range(10):
        for numero in segmento1[i]:
            io.output(numero,1)
        for numero in segmento2[i]:
            io.output(numero,1)
        time.sleep_ms(1000)
        for numero in segmento1[i]:
            io.output(numero,0)        
        for numero in segmento2[i]:
            io.output(numero,0)        
        