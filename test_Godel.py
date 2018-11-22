import math
from mathHelperFunctions import *

symbolDict = {'0':1,'s':2,'+':3,'*':4,'=':5,'(':6,')':7,',':8,'x':9,'|':10,'~':11,'&':12,'∃':13}
'''differs from Crossley symbols because user needs to be able to type in'''


def isNumeral(number):
    primes = dictToList(primeFactorization(number))
    flag = True
    if number == 2 or (len(primes) == 1 and primes[0][1] == 1):
        flag = True
    else:
        if not (primes[0][1] == 2 and primes[1][1] == 6 and primes[-1][1] == 7):
            flag = False
        else:
            number = int(number/(primes[0][0]**2*primes[1][0]**6*primes[-1][0]**7))
            isNumeral(number)
    return flag


def isVariable(number):
    primes = dictToList(primeFactorization(number))
    if number == 2**9:
        return True
    else:
        for tuple in primes:
            if tuple[1] != 10:
                return False
    return True

