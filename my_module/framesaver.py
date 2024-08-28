import cv2
import os
import argparse
import numpy as np
import time
import glob

from datetime import datetime, timedelta
from pathlib import Path


class FrameSaver:
    def __init__(self, period):
        self.index = 0
        self.period = period
    def capturing(self):
        rtsp_url = 'rtsp://192.168.2.30:554/user=admin_password=1234_channel=1_stream=0.sdp?Real_stream'
        
        list_of_files = glob.glob('/home/fridge/bluedot/captures/*') # * means all if need specific format then *.csv
        # print("length: ", len(list_of_files))
        if len(list_of_files) > 0:
            self.index = len(list_of_files)
            # print(self.index)
        # Open a connection to the RTSP stream
        cap = cv2.VideoCapture(rtsp_url)
        start_time = time.time()
        while True:
            ret, frame = cap.read()

            if not ret:
                print("Error: Could not read frame")
                break

            current_time = time.time()
            elapsed_time = current_time - start_time

            # Check if the interval period has passed
            if elapsed_time >= self.period:
                # Save the frame
                frame_filename = f'../captures/{self.index}.jpg'
                cv2.imwrite(frame_filename, frame)
                print(f'Saved {frame_filename}')

                # Reset the timer
                start_time = current_time
                self.index += 1
        
if __name__ == '__main__':
    # RTSP stream URL
    rtsp_url = 'rtsp://192.168.2.30:554/user=admin_password=1234_channel=1_stream=0.sdp?Real_stream'

    # Open a connection to the RTSP stream
    cap = cv2.VideoCapture(rtsp_url)
    framesaver = FrameSaver(0.6)
    while(True):
        framesaver.capturing()
        
    
