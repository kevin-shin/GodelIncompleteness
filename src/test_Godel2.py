import math

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
