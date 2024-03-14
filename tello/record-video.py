import time, cv2
import keyboard
from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    # 创建一个VideoWrite对象，存储画面至./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

# we need to run the recorder in a seperate thread, otherwise blocking options
#  would prevent frames from getting added to the video
# 我们需要在另一个线程中记录画面视频文件，否则其他的阻塞操作会阻止画面记录
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
    elif keyboard.is_pressed('e'):#a
        tello.rotate_clockwise(10)
        print('e')
    elif keyboard.is_pressed('a'):#e
        tello.rotate_counter_clockwise(10)
        print('a')
    elif keyboard.is_pressed('r'):#e
        tello.move_up(20)
        print('r')
    elif keyboard.is_pressed('f'):#e
        tello.move_down(20)
        print('f')
    elif keyboard.is_pressed('x'):
        tello.land()
        print('x')
        #Niveau batterie aterissage
        print(tello.get_battery())
        run = False
        tello.end()



keepRecording = False
recorder.join()
