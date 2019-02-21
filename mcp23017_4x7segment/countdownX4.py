import mcp
import time
io = mcp.MCP23017()
io1 = mcp.MCP23017(0x24)

outPins = list(range(0,16))
for pinNum in outPins:
    io.setup(pinNum, mcp.OUT)
    io1.setup(pinNum, mcp.OUT)

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

countdown = 1114
digitoOld1 = 0
digitoOld2 = 0
digitoOld3 = 0
digitoOld4 = 0
while True:
    countdown_str = str(countdown)
    digito1 = 0
    digito2 = 0
    digito3 = 0
    digito4 = 0
   
    if(countdown >= 1000):
        digito1 = int(countdown_str[3:4])
        digito2 = int(countdown_str[2:3])
        digito3 = int(countdown_str[1:2])
        digito4 = int(countdown_str[0:1])
    elif(countdown >= 100):
        digito1 = int(countdown_str[2:3])
        digito2 = int(countdown_str[1:2])
        digito3 = int(countdown_str[0:1])       
    elif(countdown >= 10):
        digito1 = int(countdown_str[1:2])
        digito2 = int(countdown_str[0:1])         
    else:
        valor1 = 0
        valor2 = int(countdown_str[0:1])

    if(digito1 != digitoOld1):
        for numero in segmento2[8]:
            io.output(numero,0)
    
    if(digito2 != digitoOld2):
        for numero in segmento1[8]:
            io.output(numero,0)

    if(digito3 != digitoOld3):            
        for numero in segmento2[8]:
            io1.output(numero,0)

    if(digito4 != digitoOld4):            
        for numero in segmento1[8]:
            io1.output(numero,0) 
    
    

    for numero in segmento2[digito1]:
        io.output(numero,1)
    for numero in segmento1[digito2]:
        io.output(numero,1)
    for numero in segmento2[digito3]:
        io1.output(numero,1)
    for numero in segmento1[digito4]:
        io1.output(numero,1)

    time.sleep_ms(100)
        

    digitoOld1 = digito1
    digitoOld2 = digito2
    digitoOld3 = digito3
    digitoOld4 = digito4

    if(countdown > 0):
        countdown = countdown - 1
    else:
        countdown = 1115