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
    while start != 0:
        if isitprime(starter):
            primes.append(starter)
            starter += 1
            start -= 1
        else:
            starter += 1
    return primes

def primeFactorization(n):
    if isitprime(n):
        return [1,n]
    else:
        a = 2
        factors = []
        while a <= n/2:
            if n%a == 0:
                b = n/a
                factors.append(a)
                factors.append(b)
                a+=1
            else:
                a += 1
        return factors


print(primeFactorization(15))