import ox
import click

lexer = ox.make_lexer([
    ('RIGHT', r'right'), # > in brainfuck
    ('LEFT', r'left'), # < in brainfuck
    ('INC', r'inc'), # + in brainfuck
    ('DEC', r'dec'), # - in brainfuck
    ('PRINT', r'print'), # . in brainfuck
    ('READ', r'read'), # , in brainfuck
    ('DO',r'do'),
    ('ADD',r'add'),
    ('SUB',r'sub'),
    ('LOOP', r'loop'), # [] in brainfuck
    ('DEF', r'def'),
    ('NUMBER', r'\d+'),
    ('PARENTESE_A', r'\('),
    ('PARENTESE_F', r'\)'),
    ('COMMENT', r';.*'),
    ('NEWLINE', r'\n'),
    ('SPACE', r'\s+')
])

tokens = ['RIGHT', 'LEFT', 'INC', 'DEC', 'SUB', 'ADD', 'NUMBER','PRINT', 'LOOP',
            'READ','DEF','COMMENT','PARENTESE_F','PARENTESE_A','DO']

operator = lambda type_op: ('operator', type_op)
op = lambda op, x: (op, x)

#expr = lambda x, y: (x, y)
parser = ox.make_parser([
    #('program : PARENTESE_A DO expr expr PARENTESE_F ',)
    #('program : PARENTESE_A DO expr expr PARENTESE_F ', lambda a,b,c,d,e: (b,c,d)),
    ('program : PARENTESE_A DO expr  PARENTESE_F', lambda x,y,z,w: (y,z)),
    ('expr : expr expr', lambda x,y: (x,y)),
    ('expr : expr', lambda x: x),
    ('expr : PARENTESE_A expr PARENTESE_F', lambda x,y,z: y),
    ('expr : PARENTESE_A operator PARENTESE_F', lambda x,y,z: y),
    ('expr : expr operator', lambda x,y: (x,y)),
    ('expr : operator', lambda x: x),
    ('operator : LOOP', operator),
    ('operator : RIGHT', operator),
    ('operator : LEFT', operator),
    ('operator : READ', operator),
    ('operator : INC', operator),
    ('operator : DEC', operator),
    ('operator : PRINT', operator),
    ('operator : ADD NUMBER', op),
    ('operator : SUB NUMBER', op),
], tokens)

@click.command()
@click.argument('source', type=click.File('r'))
def make_tree(source):
    program = source.read()
    print(program)
    tokens = lexer(program)
    #print('tokens:', tokens)

    # removing space and comment tokens before passing list to parser
    parser_tokens = [token for token in tokens if token.type != 'COMMENT' and token.type != 'SPACE']
    #print(parser_tokens)
    tree = parser(parser_tokens)
    print('tree:', tree) # Abstract syntax tree

if __name__ == '__main__':
    make_tree()
