# importation
import socket, time
import tkinter
import keyboard
import cv2
import threading

# constante du programme
host = '192.168.10.2'
port = 9000
speed = '25'

# initialistaion adrrese
locaddr = (host,port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(locaddr)


# connection avec le  drone
time.sleep(10)
sock.sendto('command'.encode(encoding="utf-8"), tello_address)
print('connect')
sock.sendto('streamon'.encode(encoding="utf-8"), tello_address)
frame_read = sock.sendto('get_frame_read'.encode(encoding="utf-8"), tello_address)
# decolage
time.sleep(5)
sock.sendto('takeoff'.encode(encoding="utf-8"), tello_address) # Takeoff
print('decollage')
time.sleep(5)
# programme principal
run = True
while run:
    if keyboard.is_pressed('z'):#z
        sock.sendto(str('forward ' + speed).encode(encoding="utf-8"), tello_address)
        print('z')
    elif keyboard.is_pressed('s'):#s
        sock.sendto(str('back ' + speed).encode(encoding="utf-8"), tello_address)
        print('s')
    elif keyboard.is_pressed('d'):#d
        sock.sendto(str('right ' + speed).encode(encoding="utf-8"), tello_address)
        print('d')
    elif keyboard.is_pressed('q'):#q
        sock.sendto(str('left ' + speed).encode(encoding="utf-8"), tello_address)
        print('q')
    elif keyboard.is_pressed('a'):#a
        sock.sendto(str('cw ' + speed).encode(encoding="utf-8"), tello_address)
        print('a')
    elif keyboard.is_pressed('e'):#e
        sock.sendto(str('ccw ' + speed).encode(encoding="utf-8"), tello_address)
        print('e')
    elif keyboard.is_pressed('r'):#e
        sock.sendto(str('up ' + speed).encode(encoding="utf-8"), tello_address)
        print('r')
    elif keyboard.is_pressed('f'):#e
        sock.sendto(str('down ' + speed).encode(encoding="utf-8"), tello_address)
        print('f')
    elif keyboard.is_pressed('x'):
        sock.sendto('land'.encode(encoding="utf-8"), tello_address) # Land
        print('x')
        run = False
        


sock.sendto('streamoff'.encode(encoding="utf-8"), tello_address)
time.sleep(5)