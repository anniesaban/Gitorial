import machine
import time

if False:
    led = machine.Pin('WL_GPIO0', machine.Pin.OUT)
    led.on()
    time.sleep(5)
    led.off()

def blink_led(counter):
    while counter > 0:
        counter = counter - 1
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
    led.off()



led = machine.Pin('WL_GPIO0', machine.Pin.OUT)
counter1=10
blink_led(counter1)
time.sleep(5)
#led = machine.Pin('WL_GPIO0', machine.Pin.OUT)
#counter2=20
#blink_led(counter2)
#time.sleep(5)