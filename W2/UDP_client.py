import socket
UDP_IP = '127.0.0.1'
UDO_PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind((UDP_IP,UDO_PORT))

while True:
    data,addr = sock.recvfrom(1024)
    print("received message: %s" % data)