## VERSION == 1.0.0
from lib import number
import json, zlib, base64

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
    
def vdb_to_json(file: str):
    """Takes a .vdb file and converts it to a .json file which makes it easy
    to view the data, especially if opened with a browser. 

    Args:
        file (str): the file within the current directory to convert
    """
    
    with open(file, mode='rb') as f:
        data = f.read()
        decoded = base64.decodebytes(data)
        decompressed = zlib.decompress(decoded).decode()
        lines = decompressed.split("\n")
        data = ",".join(lines)
        if (data[-1] == ','):
            data = data[:-1]
        data = f'[{data}]'
    with open(f'{file}.json', mode='w') as f:
        f.write(data)
        
    return json.loads(data)[0]