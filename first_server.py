import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection form', addr)
    client.send(b'sim babo ' + addr[0].encode())
    client.close()