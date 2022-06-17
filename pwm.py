# using the pwm module

import machine
import time

led = machine.Pin(2,machine.Pin.OUT)
switch = machine.Pin(0,machine.Pin.IN)

def blink_n_times(num,t_on,t_off,msg):
    counter = 0;
    while (counter < num):
        led.on()
        time.sleep(t_on)
        led.off()
        time.sleep(t_off)
        counter+=1
    print(msg)
        

while True:
    if(switch.value() ==0):
        blink_n_times(5,1,1,'blinking done')
        
        