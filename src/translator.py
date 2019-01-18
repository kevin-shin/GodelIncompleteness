from src.mathHelperFunctions import *

def numbertoText(number):
    '''
    Returns text associated with number based on encoding key
    '''

    primes = dictToList(primeFactorization(number))
    string = ''
    for tuple in primes:
        string += str(numDict[tuple[1]])
    return string

def textToNumber(text):
    '''
    Returns Godel number of text
    '''

    length = len(text)
    primes = generatePrimes(length)
    number = 1
    for i in range(length):
        number *= primes[i]**symbolDict[text[i]]
    return number

def GodelNumbertoNumber(number):
    '''
    Helpful debugging tool and decomposition. Input should be the Godel number,
    and the function returns the number without the prime number encoding.
    '''
    primes = dictToList(primeFactorization(number))
    number = ''
    for tuple in primes:
        number += str(tuple[1])
    number = int(number)
    return number


def toPlainNumber(text):
    '''
    Helpful debugging tool, just has translation text
    '''

    string = ''
    for character in text:
        string = string + str(symbolDict[character])
    return string