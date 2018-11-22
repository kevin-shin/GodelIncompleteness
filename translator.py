import math
from mathHelperFunctions import *

symbolDict = {'0':1,'s':2,'+':3,'*':4,'=':5,'(':6,')':7,',':8,'x':9,'|':10,'~':11,'&':12,'∃':13}
numDict = {1:'0',2:'s',3:'+',4:'*',5:'=',6:'(',7:')',8:',',9:'x',10:'|',11:'~',12:'&',13:'∃'}

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