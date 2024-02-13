# simple example demonstrating how to control a Tello using your keyboard.
# For a more fully featured example see manual-control-pygame.py
# 
# Use W, A, S, D for moving, E, Q for rotating and R, F for going up and down.
# When starting the script the Tello will takeoff, pressing ESC makes it land
#  and the script exit.

# 简单的演示如何用键盘控制Tello
# 欲使用全手动控制请查看 manual-control-pygame.py
#
# W, A, S, D 移动， E, Q 转向，R、F上升与下降.
# 开始运行程序时Tello会自动起飞，按ESC键降落
# 并且程序会退出

from DJITelloPy.djitellopy import 
import cv2, math, time

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()


while True:
    # In reality you want to display frames in a seperate thread. Otherwise
    #  they will freeze while the drone moves.
    # 在实际开发里请在另一个线程中显示摄像头画面，否则画面会在无人机移动时静止
    img = frame_read.frame
    cv2.imshow("drone", img)
    time.sleep(1)
