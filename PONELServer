import socket


def create_server():
    print('Server created')
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def bind(s):
    port = int(input('Type port: '))
    s.bind(('', port))
    print('Binded socket')


def listen(s):
    s.listen(10)
    print('listening...')


def accept(s):
    print('Got connection.')
    conn, address = s.accept()
    return conn, address


def send(connection):
    response = 'Successfully connected'
    connection.send(response.encode())
    print('Response sent')


def close(s):
    s.close()
    print('Session terminated')
