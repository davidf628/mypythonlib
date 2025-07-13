# $VERSION == 1.0.0

class Fraction():

    def __init__(self, num, denom=1):

        gcf = gcd(num, denom)
        if gcf != 1:
            num //= gcf
            denom //= gcf
        self.num = num
        self.denom = denom

    def __repr__(self):
        if self.denom == 1:
            return f'{self.num}'
        else:
            return f'{self.num}/{self.denom}'

    def numerator(self):
        return self.num

    def denominator(self):
        return self.denom

    def setnumerator(self, num):
        self.num = num
        return self.reduce()

    def setdenom(self, denom):
        self.denom = denom
        return self.reduce()

    def setfrac(self, num, denom):
        self.num = num
        self.denom = denom
        return self.reduce()

    def __neg__(self):
        self.num = -self.num
        return self.reduce()

    # Need ability to compare fractions, isNeg, isPos

    def __pos__(self):
        return self

    def __add__(self, other):

        if self.denom == other.denom:
            num = self.num + other.num
            denom = self.denom
        else:
            self.num *= other.denom
            other.num *= self.denom
            num = self.num + other.num
            denom = self.denom * other.denom
        self.num = num
        self.denom = denom
        return self.reduce()

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)


    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        self.num *= other.num
        self.denom *= other.denom
        return self.reduce()
                    
    def __rmul__(self, other):
        return self * other

    def __div__(self, other):
        return self * other.inverse()

    def __rdiv__(self, other):
        return self.inverse() * other


    def __pow__(self, exp):
        self.num ** exp
        self.denom ** exp
        return self.reduce()

    def inverse(self):
        n = self.num
        self.num = self.denom
        self.denom = n
        return self.reduce()

    def todecimal(self):
        return self.num / self.denom

    def reduce(self):
        gcf = gcd(self.num, self.denom)
        self.num //= gcf
        self.denom //= gcf
        return self

    def __eq__(self, other):
        return (self.num == other.num) and (self.denom == other.denom)

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def getContinuedFractionValue(a, stop=None):

    if stop == None:
        stop = len(a)-1
    if stop == 0:
        return Fraction(a[0])

    intvalue = Fraction(a[0])

    value = Fraction(1, a[stop])

    for i in range(stop-1, 0, -1):
        temp = Fraction(a[i])
        value = (value + temp).inverse()
        
    return value + intvalue;

