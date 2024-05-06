import socket

address = ("localhost", 2500)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Message to formula: ")
    if msg == 'q':
        break
    s.send(msg.encode()) #send a message to server
    data = s.recv(BUFSIZE) #receive message from server
    print("Result: %s" % data.decode())

s.close()
