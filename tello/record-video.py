import time, cv2
import keyboard
import pygame
from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

def videoRecorder():
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        img = frame_read.frame
        video.write(img)
        time.sleep(1 / 30)
        cv2.imshow(img)
        cv2.WaitKey(1)

    video.release()


recorder = Thread(target=videoRecorder)
recorder.start()

tello.takeoff()
run = True
while run:
    if keyboard.is_pressed('z'):#z
        tello.move_forward(20)
        print('z')
    elif keyboard.is_pressed('s'):#s
        tello.move_back(20)
        print('s')
    elif keyboard.is_pressed('d'):#d
        tello.move_right(20)
        print('d')
    elif keyboard.is_pressed('q'):#q
        tello.move_left(20)
        print('q')
    elif keyboard.is_pressed('e'):#e
        tello.rotate_clockwise(10)
        print('e')
    elif keyboard.is_pressed('a'):#a
        tello.rotate_counter_clockwise(10)
        print('a')
    elif keyboard.is_pressed('r'):#r
        tello.move_up(20)
        print('r')
        tello.get_height()
    elif keyboard.is_pressed('f'):#f
        tello.move_down(20)
        print('f')
    elif keyboard.is_pressed('x'):#x
        tello.land()
        print('x')
        #Niveau batterie aterissage
        print(tello.get_battery())
        run = False
        tello.end()



keepRecording = False
recorder.join()
