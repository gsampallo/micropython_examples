import mcp
import time
io = mcp.MCP23017()

outPins = list(range(0,16))
for pinNum in outPins:
    io.setup(pinNum, mcp.OUT)

while True:
    for pinNum in outPins:
        io.output(pinNum,1)
        time.sleep_ms(150)
    for pinNum in outPins:
        io.output(pinNum,0)
        time.sleep_ms(100)