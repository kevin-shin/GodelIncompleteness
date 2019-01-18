# MATH HELPER FUNCTIONS
'''
This is the file which stores all the functions responsible for the encoding to Godel numbers. Essentially, we need
the capacity to generate an arbitrary number of prime numbers, prime factorize a given number, and combine this information
in a useful way so that the GUI can present it.
'''

import math

symbolDict = {'0':1,'s':2,'+':3,'*':4,'=':5,'(':6,')':7,'|':8,'x':9,',':10,'~':11,'&':12,'∃':13}
numDict = {1:'0',2:'s',3:'+',4:'*',5:'=',6:'(',7:')',8:'|',9:'x',10:',',11:'~',12:'&',13:'∃'}

##---------MATH HELPER FUNCTIONS---------##

def isitprime(n):
    '''
    :param n: An integer (n)
    :return: boolean - True if n is prime, False otherwise.
    '''
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
    '''
    :param number: An integer n. Represents the number of prime numbers needed.
    :return: A list of n prime numbers.
    '''
    if number == 1:
        return [2]
    elif number == 2:
        return [2,3]
    else:
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
    '''

    :param number: An integer n.
    :return: Prime factorization of n, in the form of a dictionary where the key is the prime number and the value
             is the number of times it appears in the prime factorization.
    '''

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
    '''
    :param k: A number - the one searched for in a list.
    :param inputList: A list of numbers to be searched.
    :return: An integer representing the number of times k appears in inputList.

    **Note: recursive algorithm, just to practice some recursion. There are definitely more efficient ways of doing this.
            This function will most likely be rewritten after version 1.
    '''

    if len(inputList) == 0:
        return 0
    else:
        if inputList[0] == k:
            return countValues(k, inputList[1:]) + 1
        else:
            return countValues(k, inputList[1:])


def dictToList(dictionary):
    '''
    :param dictionary: A dictionary.
    :return: A sorted list of tuples where the first entry is the key and the second is the value.
    '''

    list = []
    for key in dictionary:
        list.append((key,dictionary[key]))
    list.sort() # Note: Dictionary not guaranteed to be in any particular order, so list is sorted at the end
    return list

