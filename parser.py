import ply.lex as lex
import ply.yacc as yacc

tokens = ('ZERO', 'SUCCESSOR', 'PLUS', 'TIMES', 'EQUALS',
          'LPAREN', 'RPAREN', 'NEXT', 'VARIABLE', 'NOT', 'AND',
          'EXISTS', 'END')

#TOKENS

#t_ZERO = r'0'
#t_SUCCESSOR = r's'
#t_PLUS = r'\+'
#t_TIMES = r'\*'
#t_EQUALS = r'='
#t_LPAREN = r'\('
#t_RPAREN = r'\)'
#t_NEXT = r'\,'
#t_VARIABLE = r'x'
#t_NOT = r'~'
#t_AND = r'\&'
#t_EXISTS = r'E'
#t_END = r'\;'

def t_ZERO(t):
    r'0'
    t.value = int(t.value)
    return t

def t_SUCCESSOR(t):
    r's'
    t.value = "s"
    return t

def t_PLUS(t):
    r'\+'
    t.value = "+"
    return t

def t_TIMES(t):
    r'\*'
    t.value = "*"
    return t

def t_EQUALS(t):
    r'='
    t.value = "="
    return t

def t_LPAREN(t):
    r'\('
    t.value = "("
    return t

def t_RPAREN(t):
    r'\)'
    t.value = ")"
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#Build the lexer
lex.lex()

precedence = (
    ('left', 'PLUS'),
    ('left', 'TIMES'),
)


def p_start(p):
    '''S : L
        | L S'''
    print("Start Variable recognized")

def p_l(p):
    '''L : END
        | EXPRESSIONS END
        | STATEMENTS END'''
    print("L Recognized")

def p_statement(p):
    '''STATEMENTS : LPAREN EXPRESSIONS AND EXPRESSIONS RPAREN
                 | EXISTS VARIABLE LPAREN EXPRESSIONS LPAREN
                 | NOT EXPRESSIONS'''
    print("Statement Recognized")

def p_expression(p):
    '''EXPRESSIONS : E1 EQUALS E1'''
    print("Expression recognized")

def p_e1(p):
    '''E1 : PLUS LPAREN E1 NEXT E1 RPAREN
          | E2'''
    print("E1 recognized")

def p_e2(p):
    '''E2 : TIMES LPAREN E2 NEXT E2 RPAREN
         | E3'''
    print("E2 recognized")

def p_e3(p):
    '''E3 : int
         | VARIABLE'''
    print("E3 recognized")

def p_int(p):
    '''int : ZERO
          | SUCCESSOR LPAREN int RPAREN'''
    print("Integer Recognized")
    p[0] = p[3]+p[3]

def p_error(p):
    print("Error, not a well formed sentence of the language.")
    print("Syntax error at '%s'" % p.value)


yacc.yacc()

while True:
    try:
        s = input('calc > ')   # use input() on Python 3
    except EOFError:
        break
    yacc.parse(s)