from machine import Pin,PWM
from random import randint
import random
import time

pins=[2,0,4]

pwm0 = PWM(Pin(pins[0]),1000)
pwm1 = PWM(Pin(pins[1]),1000)
pwm2 = PWM(Pin(pins[2]),1000)

red=0
green=0
blue=0

def setColor():
    pwm0.duty(red)
    pwm1.duty(green)
    pwm2.duty(blue)
    
def wheel(pos):
    global red,green,blue
    wheelPos = pos%1023
    print(wheelPos)
    if wheelPos<341:
        red=1023-wheelPos*3
        green=wheelPos*3
        blue=0
    elif wheelPos>=341 and wheelPos<682:
        wheelPos -= 341;
        red=0
        green=1023-wheelPos*3
        blue=wheelPos*3
    else :
        wheelPos -= 682;
        red=wheelPos*3
        green=0
        blue=1023-wheelPos*3
        
while True:
        for i in range(0,1023):
            wheel(i)
            setColor()
            time.sleep_ms(15)
            
pwm0.deinit()
pwm1.deinit()
pwm2.deinit()