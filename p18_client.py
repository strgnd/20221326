import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
sock.send(b'Jeong Hyeonji')
msg = sock.recv(1024)
student_id = int.from_bytes(msg, 'big')
print('Received and converted Student ID: ', student_id)
sock.close()