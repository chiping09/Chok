import socket

try:
    print("Fully qualifued domain name: " + socket.getfqdn("8.8.8.8"))
    print("host name to IP address: "+ socket.gethostbyname("www.python.org"))
    print("Host name to IP address, extended: "+ str(socket.gethostbyname_ex("www.python.org")))
    print("Get host name of local machine: "+ socket.gethostbyname("DESKTOP-JTIT4LN"))
except Exception as err:
    print("Error: " + str(err))