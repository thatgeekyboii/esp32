from machine import Pin,PWM
from pwm import myPWM
import time

mypwm = myPWM(15,2,0,4,5,18,19,21)
channels = [0,1,2,3,4,5,6,7]

dutys=[0,0,0,0,0,0,0,0,1023,512,256,128,64,32,16,8,0,0,0,0,0,0,0,0]

for i in range(0,16):
    for j in range(0,8):
        mypwm.ledcWrite(channels[j],dutys[i+j])
    time.sleep_ms(50)
    
for i in range(0,16):
    for j in range(0,8):
        mypwm.ledcWrite(channels[7-j],dutys[i+j])
    time.sleep_ms(50)

mypwm.deinit()