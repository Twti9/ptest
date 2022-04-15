#开发时间：2022/3/29 21:16
import socket
ipt = ('127.0.0.1',9999)
s=socket.socket()
s.connect(ipt)
while True:
    inp = input('输入你要发送的信息'.encode())
    if not inp:
        continue
    s.sendall(inp.encode())
    if inp== 'exit':
        print('结束通信')
        break
    server_reply = s.recv(1024).decode()
    print(server_reply)
s.close()