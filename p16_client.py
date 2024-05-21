import socket

def main():
    #서버의 호스트와 포트 정보
    host = 'localhost'
    port = 5000
    #소켓 객체 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #서버에 연결
    client_socket.connect((host, port))

    #서버로 메시지 보내기
    message = 'Hello, server! I am 20221326'
    client_socket.sendall(message.encode())
    #서버로부터 응답 받기
    response = client_socket.recv(1024).decode()

    #받은 메시지 출력
    print('Received from server: ', response)

    #소켓 닫기
    client_socket.close()

if  __name__ == '__main__':
    main()