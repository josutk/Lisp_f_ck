import ox

lexer = ox.make_lexer([
    ('DIRECAO',r'[><]'),
    ('OP',r'[-+]'),
    ('PONTO',r'.'),
    ('VIRGULA', r'[,]'),
    ('COMENTARIO', r'^;([A-Za-z0-9]+)?'),
    ('PARENTESE_A', r'\('),
    ('PARENTESE_F', r'\)'),
    ('DO',r'(do)')
    ('DEF', r'(def)')

])
tokens = ['DEF','VIRGULA','DIRECAO', 'OP','PONTO', 'COMENTARIO','PARENTESE_F','PARENTESE_A','DO']

def read(a):
    a = input('valor: ')
    return a


parser = ox.make_parser([
    ('read : VIRGULA', read),
], tokens)


st = input('expr: ')
tokens = lexer(st)
res = parser(tokens)
print('tokens:', tokens)
print('res:', res)
