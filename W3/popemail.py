import poplib
from email.message import EmailMessage

server = "192.168.207.131"
user = "chiping"
passwd = "1470"

server = poplib.POP3(server)
server.user(user)
server.pass_(passwd)

msgNum = len(server.list()[1])

for i in range(msgNum):
    for msg in server.retr(i+1)[1]:
        print(msg.decode())