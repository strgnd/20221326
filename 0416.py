'''
import socket

HOSTS = [
    'www.nba.com',
    'www.korea.net',
    'www.korea.kr',
    'www.netflix.com',
    'IoT'
]

for host in HOSTS:
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{} : {}'.format(host, msg))
'''

'''
import socket
for port in [80, 443, 21, 25, 143, 993, 110, 995]:
    url = '{}://example.co.kr/'.format(socket.getservbyport(port))
    print('{:4d}'.format(port), url)
'''

import binascii
import socket
import sys

for string_address in ['114.71.220.95']:
    packed = socket.inet_aton(string_address)
    print('Original:', string_address)
    print('Packed:', binascii.hexlify(packed))
    print('Unpacked:', socket.inet_ntoa(packed))