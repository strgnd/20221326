from socket import *

port = 2500
BUFSIZE = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)

while True:
    data = conn.recv(BUFSIZE)
    strings = data.decode()
    result = eval(strings)
    if type(result) == float:
        result = round(result, 1)
    result = str(result)

    conn.send(result.encode())

conn.close()
sock.close()

