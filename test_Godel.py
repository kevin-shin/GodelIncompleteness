import math
from mathHelperFunctions import *
from translator import *


def isNumeral(number):
    newNumber = GodelNumbertoNumber(number)
    return numeralWrapper(newNumber)


def numeralWrapper(number):
    flag = True
    newNumber = str(number)
    if newNumber == '1':
        return True
    else:
        if not (newNumber[0] == '2' and newNumber[1] == '6' and newNumber[-1] == '7'):
            flag = False
        else:
            numeralWrapper(int(newNumber[2:-1]))
    return flag

def isVariable(number):
    newNumber = str(GodelNumbertoNumber(number))
    if newNumber[0] != '9':
        return False
    else:
        for i in range(1,len(newNumber)-1):
            if newNumber[i] != '8':
                return False
        return True

def isAddition(number):
    newNumber = GodelNumbertoNumber(number)
    return additionWrapper(newNumber)

def additionWrapper(number):
    flag = True
    newNumber = str(number)
    if not ((newNumber[0] == '3' and newNumber[1] == '6' and newNumber[-1] == '7')
            and ',' not in newNumber):
        return False
    else:
        if not (isNumeral(int(newNumber[2:newNumber.find(',')])) and
                    isNumeral(int(newNumber[newNumber.find(','):]))
            or isNumeral(int(newNumber[2:newNumber.find(',')])) and
                    isVariable(int(newNumber[newNumber.find(','):]))
            or isVariable(int(newNumber[2:newNumber.find(',')])) and
                    isVariable(int(newNumber[newNumber.find(','):]))
            or isVariable(int(newNumber[2:newNumber.find(',')])) and
                    isNumeral(int(newNumber[newNumber.find(','):]))
                ):
            return False
