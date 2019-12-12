import socket


def create_client():
    print('Client created')
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect(s):
    host_ip = input('Type host ip address (if localhost, type 127.0.0.1): ')
    port = int(input('Type port (Must be the same port opened by the server): '))
    s.connect((host_ip, port))
    print('Established connection')


def receive(s):
    print(s.recv(4096))


def close(s):
    s.close()
    print('Disconnected')
