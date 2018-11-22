/* ********************************************************************* */

%{

#include<stdio.h>
#include<stdlib.h>
#include "GodelMachine.tab.h"


void yyerror(const char* s) {
  fprintf(stderr, "%s\n", s);
};

int yylex();  // forward declaration of yylex, provided by flex

void parseprint(char*);  // forward declaration of printing function

%}


%token ZERO SUCCESSOR PLUS TIMES EQUALS LPAREN RPAREN NEXT VARIABLE NOT AND EXISTS END

%%


S: L
| L S
;

L: END {parseprint("ENDLINE");}
| EXPRESSIONS END {parseprint("Expressions")}
| STATEMENTS END {parseprint("Statement")}
;

STATEMENTS: LPAREN EXPRESSIONS AND EXPRESSIONS RPAREN
| EXISTS VARIABLE LPAREN EXPRESSIONS LPAREN
| NOT EXPRESSIONS
;

EXPRESSIONS:
| E1 EQUALS E1
;

E1: PLUS LPAREN E1 NEXT E1 RPAREN
| E2
;

E2: TIMES LPAREN E2 NEXT E2 RPAREN
| E3
;

E3: int
| VARIABLE
;

int: ZERO
| SUCCESSOR LPAREN int RPAREN {parseprint("Integer");}
;

%%

/* After the next %% divider, we put the code at the end.  I included a printing function, just in case, but
 * the biggest item here is a main to do the parsing. Bison builds a function called yyparse, which parses
 * input, calling the yylex function provided by Flex to get the next token.  If yyparse returns zero, then
 * the parse worked correctly to the end of input.  Other values indicate different problems with the parse.
 */


void parseprint(char* str)
{
  printf("             PARSED: %s\n", str);
}


int main() {
  fprintf(stderr, "Enter statements/expressions to parse:\n");
  int res = yyparse();
  if (res == 0)
    fprintf(stderr, "Successful parsing.\n");
  else if (res == 1)
    fprintf(stderr, "Parsing failed due to incorrect input.\n");
  else if (res == 2)
    fprintf(stderr, "Parsing failed due to lack of memory.\n");
  else
    fprintf(stderr, "Weird value: %d\n", res);
}
