import math

symbolDict = {'0':1,'s':2,'+':3,'*':4,'=':5,'(':6,')':7,',':8,'x':9,'|':10,'~':11,'&':12,'∃':13}
'''differs from Crossley symbols because user needs to be able to type in'''



def isitprime(n):
    a = 2
    flag = True
    while a <= n/2:
        if n%a == 0:
            flag = False
            break
        else:
            a += 1
    return flag


def generatePrimes(number):
    start = number-2
    primes = [2,3]
    starter = 5
    if number == 1:
        return [2]
    elif number == 2:
        return primes
    else:
        while start != 0:
            if isitprime(starter):
                primes.append(starter)
                starter += 1
                start -= 1
            else:
                starter += 1
    return primes


def convertToGodelFactors(formula):
    '''takes in formula as a string, prints prime encoding and Godel Number'''
    length = len(formula)
    primes = generatePrimes(length)
    i = 0
    godelFormula = ''
    for char in formula:
        godelFormula = godelFormula + str(primes[i]) + "**" + str(symbolDict[char])+'.'
        i +=1
    return godelFormula[:-1]

def converttoGodelNumber(formula):
    length = len(formula)
    primes = generatePrimes(length)
    i = 0
    number = 1
    for char in formula:
        number = number * primes[i]**symbolDict[char]
        i +=1
    return number


def getPrimeFactorization(number):
    a = 2
    factors = []
    while a <= math.ceil(math.sqrt(number)):
        if number%a != 0:
            a += 1
        else:
            number = number/a
            factors.append(a)
    if number != 1:
        factors.append(number)
    return factors

