import math
from mathHelperFunctions import *

symbolDict = {'0':1,'s':2,'+':3,'*':4,'=':5,'(':6,')':7,',':8,'x':9,'|':10,'~':11,'&':12,'∃':13}
'''differs from Crossley symbols because user needs to be able to type in'''


<<<<<<< HEAD
def isNumeral(number):
    primes = dictToList(primeFactorization(number))
=======
def verifyNumeralForm(number):
    primes = dictToList(primeFactorization(number))
    print(primes)
>>>>>>> ca00c4028ff8bc124a063da59195ded7845ba981
    flag = True
    if number == 2 or (len(primes) == 1 and primes[0][1] == 1):
        flag = True
    else:
        if not (primes[0][1] == 2 and primes[1][1] == 6 and primes[-1][1] == 7):
            flag = False
        else:
            number = int(number/(primes[0][0]**2*primes[1][0]**6*primes[-1][0]**7))
<<<<<<< HEAD
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

=======
            print(number)
            verifyNumeralForm(number)
    return flag


def primeFactorization(number):
    a = 2
    factors = []
    myDict = {}
    while a <= math.ceil(math.sqrt(number)):
        if number%a != 0:
            a += 1
        else:
            number = number//a
            factors.append(a)
    if number != 1:
        factors.append(number)
    for i in factors:
        myDict[i] = CountValues(i,factors)
    return myDict

print(primeFactorization(20))



#0
#print('0')
#print(2)
#print(verifyNumeralForm(2))
#print('s(0)')
#print(2**2*3**6*5**1*7**7)
#print(verifyNumeralForm(2**2*3**6*5**1*7**7))
print('s(s(0))')
print((2**2)*(3**6)*(5**2)*(7**6)*(11**1)*(13**7)*(17**7))
print(primeFactorization(2429150201596471568662547100))

print(verifyNumeralForm(2429150201596471568662547100))
>>>>>>> ca00c4028ff8bc124a063da59195ded7845ba981
