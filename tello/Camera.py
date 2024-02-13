#importation des modules
import socket, time, cv2,keyboard

#decalration des constantes
host = '192.168.10.2'
port = 55000

# initialistaion adrrese

tello_address = ('192.168.10.1', 8889)
mypc_address = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(mypc_address)
sock.sendto('command'.encode(encoding="utf-8"), tello_address)
time.sleep(1)
print('connecté')
sock.sendto('streamon'.encode(encoding="utf-8"), tello_address)
time.sleep(1)
print('start streaming')
capture = cv2.VideoCapture('udp://0.0.0.0:11111',cv2.CAP_FFMPEG)
if not capture.isOpened():
    capture.open('udp://0.0.0.0:11111')
    
run = True
while run:
    ret,frame=capture.read()
    print(ret)
    if(ret):
        cv2.imshow('frame', frame)
    if keyboard.is_pressed('x'):
        run = False
capture.release()
cv2.destroyAllWindows()
sock.sendto('streamoff'.encode(encoding="utf-8"), tello_address)


