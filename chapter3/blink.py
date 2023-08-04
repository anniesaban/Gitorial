import machine
import time

LED_PIN = 'WL_GPIO0'
BUTTON_PIN = 2 #GP2 pin


def blink():
    led = machine.Pin(LED_PIN, machine.Pin.OUT)
    button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    while button.value():
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
    led.off()

def blink_long():
    led = machine.Pin(LED_PIN, machine.Pin.OUT)
    button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    while button.value():
        led.on()
        time.sleep(2)
        led.off()
        time.sleep(2)
    led.off()

blink_long()


