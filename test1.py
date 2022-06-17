#blinking an led 5 times

import machine
import time
led = machine.Pin(2,machine.Pin.OUT)

counter = 0

while(counter<5):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
    counter+=1
print("blinking done")
