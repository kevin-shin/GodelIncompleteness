import math

symbolDict = {'0':1,'s':2,'+':3,'*':4,'=':5,'(':6,')':7,'|':8,'x':9,',':10,'~':11,'&':12,'∃':13}
numDict = {1:'0',2:'s',3:'+',4:'*',5:'=',6:'(',7:')',8:'|',9:'x',10:',',11:'~',12:'&',13:'∃'}

##---------MATH HELPER FUNCTIONS---------##

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
    while start != 0:
        if isitprime(starter):
            primes.append(starter)
            starter += 1
            start -= 1
        else:
            starter += 1
    return primes


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
        myDict[i] = countValues(i,factors)
    return myDict


def countValues(k, inputList):
    if len(inputList) == 0:
        return 0
    else:
        if inputList[0] == k:
            return countValues(k, inputList[1:]) + 1
        else:
            return countValues(k, inputList[1:])


def dictToList(dictionary):
    list = []
    for key in dictionary:
        list.append((key,dictionary[key]))
    list.sort()
    return list


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
