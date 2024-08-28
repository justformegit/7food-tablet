from bluedot import BlueDot
from gpiomodule import lock, unlock, door_is_closed, wait_for_close, wait_for_open
from signal import pause
from time import sleep

server = None

def give_access():
    print("------------- new request -------------")
    unlock()
    print("RPi: Door unlocked")

    if not door_is_closed():
        print("RPi: Door was opaned before request")
    else:
        wait_for_open()
        print("RPi: Door opened")
    
    lock()
    wait_for_close()

    if server is not None:
        print("RPi: client_con:", server._client_connected, server._client_sock)
        print("RPi: Message sended")
        server.send("hi!")

    print("RPi: Door closed")



bd = BlueDot()
server = bd.server
bd.when_pressed = give_access

pause()
