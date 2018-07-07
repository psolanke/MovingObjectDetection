import cv2
import numpy as np
import os
import sys
from PIL import Image
import time
import scipy.ndimage.filters as filters

DRONE_CAPTURES_ROOTDIR = '/media/a3s/New Volume/Youtube_Videos/DroneCaptures/'
DRONE_CAPTURES = ['DroneShot1.mp4',
                    'DroneShot2.mp4',
                    'DroneShot3.mp4',
                    'DroneShot4.mp4',
                    'DroneShot5.mp4',
                    'DroneShot6.mp4']

def get_video_file(filename):
    full_path = os.path.join(DRONE_CAPTURES_ROOTDIR, filename)
    cap = cv2.VideoCapture(full_path)
    return cap

def convert_BGR2GRAY(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def filter(frame):
	filter1 = filters.gaussian_filter(frame,sigma=0.5)
	filter2 = filters.median_filter(frame,size=2)
	return filter2

def show_video_loop():
    pointer = 0
    video = get_video_file(DRONE_CAPTURES[pointer])
    ret, image_np = video.read()
    while True:
        ret, image_np = video.read()
        if not ret:
            pointer += 1
            if pointer >= len(DRONE_CAPTURES):
              pointer = 0
            video = get_video_file(DRONE_CAPTURES[pointer])
            continue
        
        frame_gray = convert_BGR2GRAY(image_np)
        filter_frame = filter(frame_gray)

        cv2.imshow('frame',filter_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        time.sleep(0.01)

def main(args):
    show_video_loop()

if __name__ == '__main__':
    main(sys.argv[1:])
