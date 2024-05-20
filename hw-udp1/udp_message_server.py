from socket import *

port = 3333
BUFFSIZE = 1024
mboxID = []
procedure = [0]

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    msg = data.decode()
    req = msg.split(' ')
    if (req[0] == 'send'):
        for i in range(len(procedure)):
            if (req[1] == procedure[i]):
                stat = True
                break
            else:
                stat = False
        if(stat == True):
            str = ' '.join(req[2:])
            mboxID[i - 1].append(str)
            sock.sendto('OK'.encode(), addr)
        else:
            procedure.append(req[1])
            new =[]
            str = ' '.join(req[2:])
            new.append(str)
            mboxID.append(new)
            sock.sendto('OK'.encode(), addr)
    if (req[0] == 'receive'):
        for i in range(len(procedure)):
            if(req[1] == procedure[i]):
                rec_stat = True
                break
            else:
                rec_stat = False 
        if(rec_stat == True):
            output_msg = mboxID[i-1][0]
            sock.sendto(output_msg.encode(), addr)
            mboxID[i- 1].pop(0)                
            if(len(mboxID[i-1]) == 0):
                procedure.remove(req[i])
                mboxID.pop(i - 1)
        else:
            sock.sendto('No messages'.encode(), addr) 
    if(req[0] == 'quit'):
        break 

