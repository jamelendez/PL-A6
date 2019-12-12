import ply.lex as lex

# Reserved Words
reserved = {'create_Client': 'CREATE_CLIENT',
    'create_Server': 'CREATE_SERVER',
    'connect': 'CONNECT',
    'receive': 'RECEIVE',
    'send': 'SEND',
    'close_client': 'CLIENT_CLOSE',
    'bind': 'BIND',
    'listen': 'LISTEN',
    'accept': 'ACCEPT',
    'close_server': 'SERVER_CLOSE',
}

# Tokens
tokens = [] + list(reserved.values())

# Regular Expressions
t_ignore = '\t'


# Define a rule so we can track line numbers
def t_newline(t):
    r"""
    \n+
    """
    t.lexer.lineno += len(t.value)


def t_error(t):
    print('Illegal character %s', t.value[0])
    t.lexer.skip(1)
    return t


# Build the lexer
lexer = lex.lex()
