import ox
import click
import pprint

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
    ('NAME', r'[-a-zA-Z]+'),
    ('COMMENT', r';.*'),
    ('NEWLINE', r'\n'),
    ('SPACE', r'\s+')
])


tokens = ['RIGHT', 'LEFT', 'INC', 'DEC', 'SUB', 'ADD', 'NUMBER','PRINT', 'LOOP',
            'READ','DEF','PARENTESE_F','PARENTESE_A','DO','NAME']

operator = lambda type_op: (type_op)
op = lambda op: (op)
opr = lambda op, num: (op, num)

parser = ox.make_parser([
	('program : PARENTESE_A expr PARENTESE_F', lambda x,y,z: y),
    ('program : PARENTESE_A PARENTESE_F', lambda x,y: '()'),
	('expr : operator expr', lambda x,y: (x,) + y),
	('expr : operator', lambda x: (x,)),
	('operator : program', op),
    ('operator : LOOP', operator),
    ('operator : DO', operator),
    ('operator : RIGHT', operator),
    ('operator : LEFT', operator),
    ('operator : READ', operator),
    ('operator : INC', operator),
    ('operator : DEC', operator),
    ('operator : DEF', operator),
    ('operator : PRINT', operator),
    ('operator : ADD', operator),
    ('operator : SUB', operator),
    ('operator : NAME', operator),
    ('operator : NUMBER', operator),
], tokens)


@click.command()
@click.argument('source', type=click.File('r'))
def make_tree(source):
    program = source.read()
    print('program: ', program)
    tokens = lexer(program)

    # removing space and comment tokens before passing list to parser
    parser_tokens = [token for token in tokens if token.type != 'COMMENT' and token.type != 'SPACE']

    tree = parser(parser_tokens)
    print('\n\ntree:', tree) # Abstract syntax tree

if __name__ == '__main__':
    make_tree()
