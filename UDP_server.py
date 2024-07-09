import socket
UDP_IP = '127.0.0.1'
UDO_PORT = 5005
MESSAGE = b"Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDO_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket.sendto(MESSAGE,(UDP_IP,UDO_PORT))
