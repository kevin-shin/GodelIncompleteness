symbolDict = {'0':1,'s':2,'+':3,'*':4,'=':5,'(':6,')':7,',':8,'x':9,'|':10,'~':11,'&':12,'∃':13}
numDict = {1:'0',2:'s',3:'+',4:'*',5:'=',6:'(',7:')',8:',',9:'x',10:'|',11:'~',12:'&',13:'∃'}

from mathHelperFunctions import *


def verifyNumeralForm(number):
    primes = dictToList(primeFactorization(number))
    if number == 2:
        return True
    if len(primes) == 1 and primes[0][1] == 1:
        return True
    else:
        if not (primes[0][1] == 2 and primes[1][1] == 6 and primes[-1][1] == 7):
            return False
        else:
            number = number//primes[0]**2*primes[1]**6*primes[-1]**7
            verifyNumeralForm(number)

print(verifyNumeralForm())