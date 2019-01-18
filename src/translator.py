from src.mathHelperFunctions import *

'''
Returns text associated with number based on encoding key
'''

def numbertoText(number):
    primes = dictToList(primeFactorization(number))
    string = ''
    for tuple in primes:
        string += str(numDict[tuple[1]])
    return string
'''
Returns Godel number of text'''

def textToNumber(text):
    length = len(text)
    primes = generatePrimes(length)
    number = 1
    for i in range(length):
        number *= primes[i]**symbolDict[text[i]]
    return number

'''helpful debugging tool, just has translation text'''

def toPlainNumber(text):
    string = ''
    for character in text:
        string = string + str(symbolDict[character])
    return string

def GodelNumbertoNumber(number):
    primes = dictToList(primeFactorization(number))
    number = ''
    for tuple in primes:
        number += str(tuple[1])
    number = int(number)
    return number