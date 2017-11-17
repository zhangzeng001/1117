import socket
ip_port=('127.0.0.1',8080)
BUFSIZE=1024

#创建套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址到套接字
s.bind(ip_port)
#监听链接
s.listen(5)

while True:
    conn,addr = s.accept()
    print(addr)
    while True:
        msg = conn.recv(BUFSIZE)
        print(msg,type(msg))
        conn.send(msg.upper())
    conn.close()
s.close()