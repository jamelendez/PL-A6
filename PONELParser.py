import ply.yacc as yacc
import PONELServer
import PONELClient
import PONELLexer
import socket

tokens = PONELLexer.tokens

ids = {}
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 0)


# Parsing Rules
def p_statement(p):
    """
    statement : create_client
            | create_server
            | connect
            | receive
            | send
            | close_client
            | bind
            | listen
            | accept
            | close_server
            | error
    """


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


def p_create_Client(p):
    'create_client : CREATE_CLIENT'
    PONELClient.create_server()


def p_create_Server(p):
    'create_server : CREATE_SERVER'
    PONELServer.create_client()


def p_connect(p):
    'connect : CONNECT'
    PONELClient.connect(client_socket)


def p_receive(p):
    'receive : RECEIVE'
    PONELClient.receive(client_socket)


def p_send(p):
    'send : SEND'
    PONELServer.send(conn)


def p_close_client(p):
    'close_client : CLIENT_CLOSE'
    PONELClient.close(client_socket)


def p_bind(p):
    'bind : BIND'
    PONELServer.bind(server_socket)


def p_listen(p):
    'listen : LISTEN'
    PONELServer.listen(server_socket)


def p_accept(p):
    'accept : ACCEPT'
    return PONELServer.accept(server_socket)


def p_close_server(p):
    'close_server : SERVER_CLOSE'
    PONELServer.close(server_socket)


yacc.yacc()
while True:
    s = input('PONEL >> ')
    if s == 'create_Client':
        p_create_Client(client_socket)
    elif s == 'create_Server':
        p_create_Server(server_socket)
    elif s == 'bind':
        p_bind(server_socket)
    elif s == 'listen':
        p_listen(server_socket)
    elif s == 'connect':
        p_connect(client_socket)
    elif s == 'accept':
        conn, address = p_accept(server_socket)
    elif s == 'send':
        p_send(conn)
    elif s == 'receive':
        p_receive(client_socket)
    elif s == 'close_client':
        p_close_client(client_socket)
    elif s == 'close_server':
        p_close_server(server_socket)
