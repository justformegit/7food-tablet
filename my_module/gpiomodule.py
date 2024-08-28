from gpiozero import DigitalOutputDevice 
from gpiozero import Button


relay = DigitalOutputDevice(pin=2) #реле модуль для контроля замка
gercon = Button(pin=18) #датчик двери

def lock():
    relay.off()

def unlock():
    relay.on()

def door_is_closed():
    return gercon.is_active

def wait_for_open():
    gercon.wait_for_inactive()

def wait_for_close():
    gercon.wait_for_active()

