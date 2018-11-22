

from mathHelperFunctions import *


def isitNegation(formula):
    if formula[0] == '~':
        return True
    else:
        return False

def isitConjunction(formula):
    if formula[0] == '(' and formula[-1] == ')' and '&' in formula[1:-2]:
        return True
    else:
        return False

def isitExistence(formula):
    if formula[0] == '∃' and formula[1] == 'x':
    #too simplistic, variables in this language are x|||||... BUT GOOD START
        return True
    else:
        return False