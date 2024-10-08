import re

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