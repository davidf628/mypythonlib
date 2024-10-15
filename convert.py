## VERSION == 1.0.0
from lib import number

###############################################################################
## Converts a time in the mm:ss format to seconds, if the value is a integer
##  it will return the integer, otherwise it will return None

def hhmmss_to_seconds(time):
    if time.count(':') == 2:
        (hr, min, sec) = time.split(':')
        return int(hr) * 3600 + int(min) * 60 + int(sec)
    elif time.count(':') == 1:
        (min, sec) = time.split(':')
        return int(min) * 60 + int(sec)
    else:
        return number.parseInt(time)