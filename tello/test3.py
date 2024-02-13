import socket, time


host = ''
port = 50001

locaddr = (host,port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(locaddr)

time.sleep(10)
sock.sendto('command'.encode(encoding="utf-8"), tello_address)
time.sleep(5)
sock.sendto('takeoff'.encode(encoding="utf-8"), tello_address) # Takeoff
time.sleep(5)
sock.sendto('cw 180'.encode(encoding="utf-8"), tello_address) # Rotate clockwise 360
time.sleep(5)
sock.sendto('land'.encode(encoding="utf-8"), tello_address) # Land
time.sleep(5)