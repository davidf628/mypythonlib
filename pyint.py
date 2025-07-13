# $VERSION = 1.0.0

import math
import os
import sys

import itertools

from operator import attrgetter

######
##
## Available Functions:
##
## isPrime(n) - determines if an integer-value input is a prime number or not
##
## isComposite(n) - returns true if an integer is a non-prime number
##
## getNextPrime(n) - returns the next prime number after a given value
##
## getPrimes([min_val], [max_val]) - returns a list of prime numbers within
##   a specified range
##
## getNumberInfo([min_val], [max_val]) - returns a list of all numbers up to
##   a given maximum and whether it is prime, what it's phi value is, and it's
##   prime factors
##
## getPeriodicContinuedFraction(S) - returns a list of values that represents
##   one period of continued fraction values for a square root
##
## comb(n, r) - returns the number of ways of choosing n objects, r at a time
##   when order is not important
##
## perm(n, r) - return the number of ways of choosing n objects, taken r
##   at a time when order is important
##
## fact(n) - computes the factorial of a given value n, which is defined
##   as n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
##
## gcf(a, b) - determines the greatest common factor among two different
##   numbers
##
## isRelativelyPrime(a, b) - determines if two numbers are relatively prime
##   to one another
##
## phi(n) - Euler's Totient function phi, which returns the number of values
##   that are relatively prime to the given value n
##
## isPermutation(a, b) - checks to see if the number a is a permutation of
##   the digits of b
##
## nDigits(n) - calculates the length of a number (the number of digits it
##   contains)
##
## sortDigits(n) - sorts the digits of a number into a string
##
## primeFactors(n) - returns an array containing all the prime factors of
##   the given value n
##
## listProduct(l) - returns the product of all the values contained in a list
##
## listPhi(l) - calculates Euler's totient function based on a given set of
##   prime factors
##
######

def numberExists(val, numberlist):
    
    if isinstance(val, Number):
        val = val.value

    for n in numberlist:
        if n.value == val:
            return True

    return False


def binarySearch(array, item):
    
    start = 0
    end = len(array) - 1
    found = False

    while (start <= end) and (not found):
        pos = 0
        mid = (start + end) // 2
        if array[mid] == item:
            pos = mid
            found = True
        else:
            if item < array[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return (-1, pos)[found]


def progress_bar(current, total, bar_length = 20):
    percent = float(current) * 100 / total
    arrow   = '-' * int(percent/100 * bar_length - 1) + '>'
    spaces  = ' ' * (bar_length - len(arrow))

    sys.stdout.write('\rProgress: [%s%s] % 5.1f %%' % (arrow, spaces, percent))
    sys.stdout.flush()


def test():

##    from timeit import default_timer as timer
##    from datetime import timedelta
##    
##    start = timer()
##
##
##            
##    print(f'time: {timedelta(seconds=timer()-start)} s.')
##
##    print(f'\nThere are now {len(numbers)} total, and {addedCount} were added this time.')
    None

    
class Number():

    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
            self.factors = primeFactors(value)
            self.prime = len(self.factors) == 1
            self.phi = listPhi(self.factors)
        elif isinstance(value, str):
            terms = value.split(";")
            self.value = int(terms[0])
            self.prime = terms[1].strip() == "True"
            self.phi = int(terms[2])
            l = terms[3].strip()[1:-1].split(",")
            self.factors = []
            for num in l:
                if num != '':
                    self.factors.append(int(num))
        elif isinstance(value, list) or isinstance(value, tuple):
            self.factors = list(value)
            self.prime = len(value) == 1
            self.phi = listPhi(self.factors)
            self.value = listProduct(self.factors)
        elif isinstance(value, dict):
            item = value.popitem()
            self.value = item[0]
            self.factors = list(item[1])
            self.phi = listPhi(self.factors)
            self.prime = len(self.factors) == 1

    def __repr__(self):
        return f'{self.value}; {self.prime}; {self.phi}; {self.factors}'

    def __eq__(self, other):
        if isinstance(other, Number):
            return self.value == other.value
        if isinstance(other, int):
            return self.value == other

    def __ne__(self, other):
        if isinstance(other, Number):
            return self.value != other.value
        if isinstance(other, int):
            return self.value != other

    def __gt__(self, other):
        if isinstance(other, Number):
            return self.value > other.value
        if isinstance(other, int):
            return self.value > other

    def __lt__(self, other):
        if isinstance(other, Number):
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other

    def __ge__(self, other):
        if isinstance(other, Number):
            return self.value >= other.value
        if isinstance(other, int):
            return self.value >= other

    def __le__(self, other):
        if isinstance(other, Number):
            return self.value <= other.value
        if isinstance(other, int):
            return self.value <= other

        
earlyprimes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

######################################
## Determines the greatest common factor among two different numbers a, and b

def gcf(a, b):

    while(b != 0):
        b, a = a % b, b
        
    return a
    

######################################
## Determines whether two numbers are relatively prime to one another or not

def isRelativelyPrime(a, b):
    return gcf(a, b) == 1


######################################
## Euler's Totient function, phi, which determines the number of values that
##   are relatively prime to n

def phi(n):
    
    if isPrime(n):
        return n - 1
    else:
        count = 0
        stop = n // 2 + 1
        for i in range(1, stop):
            if isRelativelyPrime(i, n):
                count += 1
        return  2*count
    
######################################
## Calculates the number of combinations of taking n objects r at a time

def comb(n, r):

    if (r > n):
        raise ArithmeticError('n must be greater than or equal to r for a ' \
                              'combination')
    else:
        return permutation(n, r) // factorial(r)


######################################
## Computes the number of permutations of n objects taken r at a time

def perm(n, r):

    if (r > n):
        raise ArithmeticError('n must be greater than or equal to r for a ' \
                              'permutation.')

    if n == r:
        return factorial(n)
    else:
        d = n - r
        perm = 1

        for i in range(d+1, n+1):
            perm *= i

        return perm
    
######################################
## Calculates a factorial of a given value n.

def fact(n):

    if n < 0:
        return ArithmeticError('Factorial operation not defined for negative ' \
                               'numbers.')

    if not isinstance(n, int):
        return ArithmeticError('Factorial is only defined for integers.')

    if n == 0:
        return 1
    
    return n * factorial(n - 1)


######################################
## Determines the values within the continued fraction of a given square root

def getPeriodicContinuedFraction(S):

    mn = 0
    dn = 1
    a0 = int(math.sqrt(S))
    an = int(math.sqrt(S))
    ilist = [ a0 ]

    if a0 != math.sqrt(S):
        while an != 2 * a0:
            mn = dn * an - mn
            dn = (S - mn ** 2) / dn
            an = int( (a0 + mn) / dn )
            ilist.append(an)
    return ilist


######################################
## Checks to see if a number is prime or not

def isPrime(n):

    if not isinstance(n, int):
        raise TypeError('You can only test an integer value for a prime number.')
    
    if n <= 1:
        return False

    if n > 10:
        c = n % 10
        if (c == 0) or (c == 2) or (c == 4) or (c == 5) or (c == 6) or (c == 8):
            return False

    stop = round(math.sqrt(n)) + 1
    for i in range(2, stop):
        if n % i == 0: 
            return False

    return True


######################################
## Checks to see if a number is factorable

def isComposite(n):

    if not isinstance(n, int):
        raise TypeError('You can only test an integer value for a composite number.')
    
    if n <= 1:
        n = -n

    return not isPrime(n)
    

######################################
## Returns a list containing all of the prime factors of a number

def primeFactors(n):

    if n == 0:
        return []

    l = []

    for i in earlyprimes:
        while (n % i == 0):
            l.append(i)
            n = n // i

    if n != 1:
        for i in range(2, n+1):
            if isPrime(i):
                while (n % i == 0):
                    l.append(i)
                    n = n // i

    return l


######################################
## Returns a list of all the unique prime factors of a number

def uniquePrimeFactors(n):

    l = []

    for i in range(2, n+1):
        if isPrime(i) and (n % i == 0):
            l.append(i)
            n = n // i

    return l

######################################
## Returns the next prime number greater than the given value.

def getNextPrime(n):
    n += 1
    while not isPrime(n):
        n += 1
    return n


#####################################
## Returns a list of prime values between two given values. It pulls
##   these from a file called primes.txt if it exists, but if not it
##   will calculate them. If any values had to be calculated they are
##   written to the file primes.txt afterward for faster computation
##   for the next request.

def getPrimes(min_val=0, max_val=None):

    primes = []
    
    filename = 'primes.txt'
    dirname = os.path.dirname(__file__)
    abspath = os.path.join(dirname, filename)

    file_exists = os.path.exists(abspath)
    if file_exists:
        with open(abspath) as f:
            data = f.readlines()
        primes = [ int(value) for value in data ]

    if len(primes) > 0:
        while primes[0] < min_val:
            primes.pop(0)

    if max_val == None:
        return primes
    else:
        if len(primes) > 0:
            while primes[-1] > max_val:
                primes.pop()

    if len(primes) > 0:
        last_prime = primes[-1] + 1
    else:
        last_prime = 0

    if last_prime < max_val:
        for i in range(last_prime, max_val + 1):
            if isPrime(i):
                primes.append(i)
                with open(abspath, 'a') as f:
                    f.write(str(i) + '\n')         

    return primes


#####################################
## Returns a list of different aspects of numbers that are time consuming
##   to calculate. It writes the data to a file called numbers.txt in order
##   to retrieve it faster the next time it is needed.

def getNumberInfo(min_val=0, max_val=None):

    numbers = []

    filename = 'numbers.txt'
    dirname = os.path.dirname(__file__)
    abspath = os.path.join(dirname, filename)

    file_exists = os.path.exists(abspath)
    if file_exists:
        with open(abspath) as f:
            data = f.readlines()
        numbers = [ Number(value) for value in data ]

    if len(numbers) > 0:
        while numbers[0].value < min_val:
            numbers.pop(0)

    if max_val == None:
        return numbers
    else:
        if len(numbers) > 0:
            while numbers[-1].value > max_val:
                numbers.pop()

    if len(numbers) > 0:
        last_number = numbers[-1].value + 1
    else:
        last_number = 0

    if last_number < max_val:
        for i in range(last_number, max_val + 1):
            n = Number(i)
            numbers.append(n)
            with open(abspath, 'a') as f:
                f.write(str(n) + '\n')       

    return numbers


#####################################
## Returns the length of a number (the number of digits it has)

def nDigits(n):
    #return int(math.log(n, 10)) + 1
    return len(str(n))


#####################################
## Sorts the digits in a number

def sortDigits(n):
    return ''.join(sorted(str(n)))

#####################################
## Returns true if the second number is just a reording of the digits of the
##   first number
     
def isPermutation(a, b):
    
    if nDigits(a) != nDigits(b):
        return False
    else:
        a = sortDigits(a)
        b = sortDigits(b)
        return a == b

#####################################
## Finds the product of all the items contained within a list

def listProduct(l):
    
    product = 1
    for val in l:
        product *= val
    return product


#####################################
## Calculates Euler's totient function based on a list of prime factors

def listPhi(l):
    
    totient = listProduct(l)
    for val in set(l):
        totient *= (1 - 1 / val)
        
    return int(totient)


#####################################
## Determines if a list has duplicated values within it

def listHasDuplicates(l):
    s = set()
    for item in l:
        s.add(item)
    return len(s) != len(l)






if __name__ == '__main__':
    test()
