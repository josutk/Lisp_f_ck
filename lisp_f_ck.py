import ox

lexer = ox.make_lexer([
    ('DIRECAO',r'[><]'),
    ('OP',r'[-+]'),
    ('PONTO',r'[.]'),
    ('VIRGULA', r'[,]'),
    ('COMENTARIO', r'^;([A-Za-z0-9]+)?'),
    ('CONCHETE_A', r'\('),
    ('CONCHETE_f', r'\)'),
    ('DO',r'(do)')

])
tokens = ['VIRGULA','DIRECAO', 'OP','PONTO', 'COMENTARIO','CONCHETE_f','CONCHETE_A','DO']

def read(a):
    a = input('valor: ')
    return a

def print_valor(a):
    print(a)

parser = ox.make_parser([
    ('read : VIRGULA', read),
], tokens)


st = input('expr: ')
tokens = lexer(st)
res = parser(tokens)
print('tokens:', tokens)
print('res:', res)
