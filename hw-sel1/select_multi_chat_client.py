from socket import *
import threading

port = 5555
BUFFSIZE = 1024

def handler(sock):
    while True:
        msg = sock.recv(BUFFSIZE)
        print(msg.decode())

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))

my_id = input('ID를 입력하세요: ')
sock.send(('['+my_id+']').encode())

th = threading.Thread(target=handler, args=(sock,))
th.daemon = True
th.start()

while True:
    msg = '[' + my_id + ']' + input()
    sock.send(msg.encode())