# importation des module
import keyboard
import cv2,time
import djitellopy
from threading import Thread

# constante du programme
speed = 10
is_recording = True
# declaration des fonction

def videoRecorder():
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

# declaration des class

# main function
def main():
    # conecte to the drone
    tello = djitellopy.Tello()
    tello.connect()
    print('is connected')
    
    # set speed
    tello.set_speed(speed)
    
    # set the stream
    is_recording = True
    tello.streamon()
    frame_read = tello.get_frame_read()
    recorder = Thread(target=videoRecorder)
    recorder.start()
    print('is streaming')
    
    
    # takeoff
    tello.takeoff()
    print('takeoff')
    
    
    # piloting
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
            print(a)
            run = False
            tello.end()
    
    
    
    tello.land()
    print('landed')

# porgramme principal
if __name__ == '__main__':
    main()
