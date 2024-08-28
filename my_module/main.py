from bluedot import BlueDot
from gpiomodule import lock, unlock, door_is_closed, wait_for_close, wait_for_open
from signal import pause
from time import sleep
import framesaver
from framesaver import FrameSaver

import cv2
import os
import argparse
import numpy as np
import time

from datetime import datetime, timedelta
from pathlib import Path

import multiprocessing


server = None



def give_access():
    index = 0
    period = 1
    print("------------- new request -------------")
    unlock()
    print("RPi: Door unlocked")

    if not door_is_closed():
        print("RPi: Door was opaned before request")
    else:
        wait_for_open()
        print("RPi: Door opened")
    
    time.sleep(0.5)
    lock()

        
    rtsp_url = 'rtsp://192.168.2.30:554/user=admin_password=1234_channel=1_stream=0.sdp?Real_stream'

    framesaver = FrameSaver(0.5)
    p = multiprocessing.Process(target=framesaver.capturing)
    p.start()
    wait_for_close()
    p.terminate()
    p.join()
    if server is not None:
        print("RPi: client_con:", server._client_connected, server._client_sock)
        print("RPi: Message sended")
        server.send("hi!")

    print("RPi: Door closed")



bd = BlueDot()
server = bd.server
bd.when_pressed = give_access

pause()
