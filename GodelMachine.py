from mathHelperFunctions import *

symbolDict = {'0':1,'s':2,'+':3,'*':4,'=':5,'(':6,')':7,'|':8,'x':9,',':10,'~':11,'&':12,'∃':13}
numDict = {1:'0',2:'s',3:'+',4:'*',5:'=',6:'(',7:')',8:'|',9:'x',10:',',11:'~',12:'&',13:'∃'}

from mathHelperFunctions import *

def numberToText(number):
    primes = dictToList(primeFactorization(number))
    text =''
    for prime in primes:
        text = text + numDict[prime[1]]
    return text

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