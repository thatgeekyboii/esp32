import machine
import time

led = machine.Pin(2,machine.Pin.OUT)

switch = machine.Pin(0,machine.Pin.IN)

while True:
    if(switch.value() ==0):
        led.on()
    else:
        led.off()
        
        