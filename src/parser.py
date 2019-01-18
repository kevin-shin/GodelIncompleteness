import ply.lex as lex
import ply.yacc as yacc

# Variable associated with executed parser. The importance of this variable will become more apparent
# in lines 98-100, but basically this serves as a toggle to see whether the parser generated an error.
# This allows the GodelIncompleteness program to generate the appropriate message.

parsedCorrectly = True

##-------------TOKENS-------------##

tokens = ['ZERO', 'SUCCESSOR', 'PLUS', 'TIMES', 'EQUALS',
          'LPAREN', 'RPAREN', 'NEXT', 'VARIABLE', 'NOT', 'AND',
          'EXISTS', 'END']

t_ZERO = r'0'
t_SUCCESSOR = r's'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NEXT = r'\,'
t_VARIABLE = r'x\|*'
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

# Build the lexer
lex.lex()

# Precedence rules. A bit unnecessary since we're not actually performing the operation.
precedence = (
    ('left', 'PLUS'),
    ('left', 'TIMES'),
)

##------------------------------------------------------##
#          CONTEXT FREE GRAMMAR FOR ARITHMETIC           #
##------------------------------------------------------##


def p_start(p):
    '''S : L
        | L S'''
    p[0] = None

def p_l(p):
    '''L : EXPRESSIONS END
         | STATEMENTS END
         | END '''
    p[0] = None

def p_statement(p):
    '''STATEMENTS : LPAREN EXPRESSIONS AND EXPRESSIONS RPAREN
                 | EXISTS VARIABLE LPAREN EXPRESSIONS LPAREN
                 | NOT EXPRESSIONS'''
    p[0] = None

def p_expression(p):
    '''EXPRESSIONS : E1
                   | E1 EQUALS E1'''
    p[0] = None

def p_e1(p):
    '''E1 : E2
          | PLUS LPAREN E1 NEXT E1 RPAREN'''
    p[0] = None

def p_e2(p):
    '''E2 : E3
          | TIMES LPAREN E2 NEXT E2 RPAREN '''
    p[0] = None

def p_e3(p):
    '''E3 : int
          | VARIABLE'''
    p[0] = None

def p_int(p):
    '''int : ZERO
           | SUCCESSOR LPAREN int RPAREN'''
    p[0] = None


# Error function
def p_error(p):
    global parsedCorrectly
    yacc.parsedCorrectly = False

# Build parser
yacc.yacc()


# If the user wants to run the lexer/parser independently, lines 105-110 will run the parser on the
# console. The lines are left for ease of use/debugging purposes.

#while True:
#    try:
#        s = input('>>> ')   # use input() on Python 3
#    except EOFError:
#        break
#    yacc.parse(s)
