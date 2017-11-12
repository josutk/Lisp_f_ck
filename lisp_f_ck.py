import ox

lexer = ox.make_lexer([
    ('RIGHT', r'right'), # > in brainfuck
    ('LEFT', r'left'), # < in brainfuck
    ('INC', r'inc'), # + in brainfuck
    ('DEC', r'dec'), # - in brainfuck
    ('PRINT', r'print'), # . in brainfuck
    ('READ', r'read'), # , in brainfuck
    ('DO',r'do'),
    ('DEF', r'def'),
    ('PARENTESE_A', r'\('),
    ('PARENTESE_F', r'\)'),
    ('LOOP', r'loop'), # [] in brainfuck
    ('COMENTARIO', r'^;([A-Za-z0-9]+)?'),
])

tokens = ['RIGHT', 'LEFT', 'INC', 'DEC', 'PRINT', 'LOOP', 'READ','DEF',
            'COMENTARIO','PARENTESE_F','PARENTESE_A','DO']

def read(a):
    a = input('valor: ')
    return a


parser = ox.make_parser([
    #('program : DO expr', None),
    #('expr: loop | operators', None),
    ('read : READ', read),
    #('loop : LOOP operators', None),
    #('operators : RIGHT | LEFT | INC | DEC | PRINT | READ', None),
], tokens)


st = input('expr: ')
tokens = lexer(st)
res = parser(tokens)
print('tokens:', tokens)
print('res:', res) # Abstract syntax tree
