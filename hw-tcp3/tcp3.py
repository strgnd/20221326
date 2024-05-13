from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n') 
    str = req[0].split(' ')
    filename = str[1][1:]
    if (filename == 'index.html'):
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'
        bodyData = f.read()
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        text = 'Content-Type: ' + mimeType + '\r\n'
        c.send(text.encode())
        c.send('\r\n'.encode())
        c.send(bodyData.encode())
    elif (filename == 'iot.png'):
        f = open(filename, 'rb')
        mimeType = 'image/png'
        bodyData = f.read()
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        text = 'Content-Type: ' + mimeType + '\r\n'
        c.send(text.encode())
        c.send('\r\n'.encode())
        c.send(bodyData)
    elif (filename == 'favicon.ico'):
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
        bodyData = f.read()
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        text = 'Content-Type: ' + mimeType + '\r\n'
        c.send(text.encode())
        c.send('\r\n'.encode())
        c.send(bodyData)
    else:
        c.send('HTTP/1.1 404 Not Found\r\n'.encode())
        c.send('\r\n'.encode())
        c.send('<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'.encode())
        c.send( '<BODY>Not Found</BODY></HTML>'.encode())

    c.close()
