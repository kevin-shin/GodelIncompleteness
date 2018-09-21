import math
from mathHelperFunctions import *

symbolDict = {'0':1,'s':2,'+':3,'*':4,'=':5,'(':6,')':7,',':8,'x':9,'|':10,'~':11,'&':12,'∃':13}
'''differs from Crossley symbols because user needs to be able to type in'''


def verifyNumeralForm(number):
    primes = dictToList(primeFactorization(number))
    print(primes)
    flag = True
    if number == 2 or (len(primes) == 1 and primes[0][1] == 1):
        flag = True
    else:
        if not (primes[0][1] == 2 and primes[1][1] == 6 and primes[-1][1] == 7):
            flag = False
        else:
            number = int(number/(primes[0][0]**2*primes[1][0]**6*primes[-1][0]**7))
            print(number)
            verifyNumeralForm(number)
    return flag

#0
#print('0')
#print(2)
#print(verifyNumeralForm(2))
#print('s(0)')
#print(2**2*3**6*5**1*7**7)
#print(verifyNumeralForm(2**2*3**6*5**1*7**7))
print('s(s(0))')
print((2**2)*(3**6)*(5**2)*(7**6)*(11**1)*(13**7)*(17**7))
print(primeFactorization(4607793427337100))

