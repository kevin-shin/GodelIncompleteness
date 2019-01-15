import ply.lex as lex
import ply.yacc as yacc

tokens = ('ZERO', 'SUCCESSOR', 'PLUS', 'TIMES', 'EQUALS',
          'LPAREN', 'RPAREN', 'NEXT', 'VARIABLE', 'NOT', 'AND',
          'EXISTS', 'END')

#TOKENS
t_ZERO = r'0'
t_SUCCESSOR = r's'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NEXT = r'\,'
t_VARIABLE = r'x'
t_NOT = r'~'
t_AND = r'\&'
t_EXISTS = r'E'
t_END = r'\;'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#Build the lexer
lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'))

def p_start(p):
    '''S: L
        | L S'''
    print(p[0] + "Start Variable")


def p_l(p):
    '''L: END
        | EXPRESSIONS END
        | STATEMENTS END'''

def p_statement(p):
    '''STATEMENTS: LPAREN EXPRESSIONS AND EXPRESSIONS RPAREN
                 | EXISTS VARIABLE LPAREN EXPRESSIONS LPAREN
                 | NOT EXPRESSIONS'''

def p_expression(p):
    '''EXPRESSIONS: | E1 EQUALS E1'''

def p_e1(p):
    '''E1: PLUS LPAREN E1 NEXT E1 RPAREN
         | E2'''

def p_e2(p):
    '''E2: TIMES LPAREN E2 NEXT E2 RPAREN
         | E3'''

def p_e3(p):
    '''E3: int
         | VARIABLE'''

def p_int(p):
    '''int: ZERO
          | SUCCESSOR LPAREN int RPAREN'''

yacc.yacc()

while True:
    try:
        s = input('calc > ')   # use input() on Python 3
    except EOFError:
        break
    yacc.parse(s)