/* ********************************************************************* */

/* The code between the brackets below will be included verbatim at the
 * top of the C file flex creates.  This includes any needed include
 * files and a few declarations...
 */

%{
#include<stdio.h>
#include<stdlib.h>

void printer(char*);  // Forward declaration of printing function

%}

/* After the verbatim code, we may declare names that correspond to
 * common patterns that will show up in the rules.  A lot may be
 * done here, but I typically keep this simple, and let the rules
 * handle everything else
 */


/* Below the %% are the "rules" for the lexical analyzer.  They are
 * a sequence of regular expressions on the left, and a fragment
 * of C code on the right.  The code may do anything you like, but
 * any procedures you need for it should be declared at the bottom
 * of the file.
 */
%%
("0") {printer("Zero"); return ZERO;}
("s") {printer("Successor"); return SUCCESSOR;}
("+") {printer("Plus"); return PLUS;}
("*") {printer ("Times");return TIMES;}
("=") {printer("Assign"); return EQUALS;}
("(") {printer ("LParen"); return LPAREN;}
(")") {printer ("RParen"); return RPAREN;}
(",") {printer("Next"); return NEXT;}
("x") {printer("Variable"); return VARIABLE;}
("|") {printer("Subscript"); return SUBSCRIPT;}
("~") {printer("Not"); return NOT;}
("&") {printer("And"); return AND;}
("E") {printer("Exists"); return EXISTS;}
(";") {printer("End"); return END;}

[ \t\n]+		;  /*when see whitespace, do nothing*/

%%

/* this section contains any procedures you might want to declare, anything
 * that the C fragments above might need.  Like the section at the top,
 * the code you put here will be included, verbatim.
 */

void printer(char* str)
{
  printf("      Recognized %s: %s\n", str, yytext);
}
