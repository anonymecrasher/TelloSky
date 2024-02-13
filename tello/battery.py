import socket, time
import tkinter
import keyboard

# constante du programme
host = ''
port = 8889
speed = '25'

# initialistaion adrrese
locaddr = (host,port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(locaddr)

sock.sendto('command'.encode(encoding="utf-8"), tello_address)
a = sock.sendto('battery?'.encode(encoding="utf-8"), tello_address)
print(a)