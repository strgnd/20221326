import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s. bind(('', 5000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Server is listening on port 5000')
    print('Connection form: ', addr)
    recv_msg = client.recv(1024).decode()
    print('Received from server: ', recv_msg)
    msg = recv_msg[-8:]
    new_msg = 'Hi, stranger! You are ' + msg
    client.send(new_msg.encode())
    client.close()