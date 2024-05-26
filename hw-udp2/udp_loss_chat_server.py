from socket import *
import random
import time

BUFF_SIZE = 1024
port = 3333

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.randint(1, 10) <= 5: 
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break
    
    msg = input('-> ')
    reTx = 0
    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break