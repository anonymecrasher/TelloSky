import cv2
import socket
import threading

tello_ip = '192.168.10.1'
tello_port = 11111
tello_address = (tello_ip, 8889)

host = '192.168.10.2'
port = 9000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))
sock.sendto('command'.encode(encoding="utf-8"), tello_address)
print('connect')
sock.sendto('streamon'.encode(encoding="utf-8"), tello_address)
print('stream')
def recieve_video():
    cap = cv2.VideoCapture(f'udp://{tello_ip}:{tello_port}')
    
    while True:
        try:
            ret, frame = cap.read()
            if not ret:
                break
            encoded_frame = cv2.imencode('.jpg', frame)[1].tobytes()
            sock.sendto(encoded_frame,('192.168.10.1', 11111))
        except KeyboardInterrupt:
            break
            
        cap.realease()
        
video_thread = threading.Thread(target = recieve_video)
video_thread.start()