from socket import *
import time
import threading

clients = []
port = 5555
BUFFSIZE = 1024

def handler(sock):
    while True:
        data = sock.recv(BUFFSIZE)

        #'quit'을 수신하면 해당 클라이언트를 목록에서 삭제
        if 'quit' in data.decode():
            if addr in clients:
                print(addr, 'exited')
                clients.remove(addr)
                continue

        print(time.asctime() + str(addr) + ':' + data.decode())

        #모든 클라이언트에게 전송
        for client in clients:
            if client[0] != sock:
                client[0].send(data)

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(1)

print('Server Started')

while True:
    conn, addr = s.accept()

    #새로운 클라이언트면 목록에 추가
    if [conn, addr] not in clients:
        print('new client', addr)
        clients.append([conn, addr])

    th = threading.Thread(target=handler, args=(conn,))
    th.start()