#开发时间：2022/3/29 13:28

import socket
import threading
def link_handler(link,client):
    print("服务器开始接收来自[%s:%s]的请求..."%(client[0],client[1]))
    while True:
        client_data = link.recv(1024).decode()
        if client_data == "exit":
            print("结束与[%s:%s]的通信..." % (client[0], client[1]))
            break
        print("来自[%s:%s]的客户端向你发来信息：%s" % (client[0], client[1], client_data))
        link.senall('服务器已经接收到你的信息'.encode())
    link.close()
#确定服务器ip地址和端口号
ipt = ('127.0.0.1',9999)
#新建套接字
s=socket.socket()
#绑定套接字与端口号
s.bind(ipt)
#进入监听状态
s.listen(5)
print('等待客户端连接...')
#接收客户端发起的连接
while True:
    conn,address = s.accept()
    t = threading.Thread(target=link_handler,args=(conn,address))
    t.start()