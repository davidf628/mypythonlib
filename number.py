## $VERSION == 1.1.0

import re, math

###############################################################################
##
## Functions:
##   - isNumber
##   - isInt
##   - isFloat
##   - parseInt
##   - rnd

###############################################################################
##
##  Returns true if the input value represents a numerical value, it can
##    be a string that contains a number, or an integer or float. Otherwise
##    this returns false

def isNumber(val):

    try:
        a = float(val)
        return True
    except (ValueError, TypeError):
        return False
    

###############################################################################
# Returns true if the input value is an integer represented by a string
    
def isInt(val):
    # check to make sure a value has the expected form of an integer
    ismatch = re.match('^[+-]?\d+$', str(val)) != None
    if ismatch:
        return True
    else:
        # if an expression can evaluate to an integer, we need to also
        #  count that as a possibility
        try:
            return int(val) == float(val)
        except:
            return False
        

###############################################################################
# Checks to see if a value is a floating point value or not    
    
def isFloat(val):
    return isNumber(val) and not isInt(val)


###############################################################################
## Converts a string to an integer, if the string does not represent an integer
##  it will return None.

def parseInt(value):
    try:
        return int(value)
    except ValueError:
        return None
    

def rnd(n, decimals=0):
    """Replaces Python's rounding system and uses the basic rounding
    rule of 0.5 or higher, round up. Also allows for rounding an
    entire array all at once
    """
    
    def round_half_up(n, decimals=0):
        multiplier = 10 ** decimals
        return math.floor(n*multiplier + 0.5) / multiplier
    
    def round_val(n, decimals=0):
        if decimals == 0:
            rounded_abs = int(round_half_up(abs(n), decimals))
            return int(math.copysign(rounded_abs, n))
        else:
            rounded_abs = round_half_up(abs(n), decimals)
            return math.copysign(rounded_abs, n)      
    
    # if a list of numbers is provided, round all values
    if type(n) == 'list':
        rounded_values = []
        for v in n:
            rounded_values.append(round_val(v), decimals)
        return rounded_values
    else:
        return round_val(n, decimals)
