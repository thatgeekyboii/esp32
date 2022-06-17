from machine import Pin,PWM
import time

pwm = PWM(Pin(2,Pin.OUT),1000)

while True:
    for i in range(0,1023):
        pwm.duty(i)
        time.sleep_ms{1)
        
    for i in range(0,1023):
        pwm.duty(1023-i)
        time.sleep_ms(1)

pwm.deinit()