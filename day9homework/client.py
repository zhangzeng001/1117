import socket
ip_port = ('127.0.0.1',8080)
BUFSIZE=1024
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect_ex(ip_port)

while True:
    msg = input('>>>:')
    if len(msg) == 0:continue
    c.send(msg.encode('utf-8'))
    feedback = c.recv(BUFSIZE)
    print(feedback)
c.close()

