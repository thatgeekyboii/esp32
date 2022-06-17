 import machine
 
led = machine.Pin(2,machine.Pin.OUT)
switch = machine.Pin(0,machine.Pin.IN)

def handle_interrupt(pin):
    led.value(not led.value())

switch.irq(trigger=machine.Pin.IRQ_FALLING,handler=handle_interrupt)