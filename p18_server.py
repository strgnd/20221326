import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
print('Server is listening...')
s. listen(2)

while True:
    client, addr = s.accept()
    print('Connenction form: ', addr)
    student_name = client.recv(1024).decode()
    print('Student Name: ', student_name)
    my_id = 20221326
    send_id = my_id.to_bytes(4, 'big')
    client.send(send_id)
    client.close()
