# $VERSION = 2.0.2

import os, requests, re

###############################################################################
# First looks for the script online, if it cannot find it, then an error is
#  printed and the script quits. Next, it looks for the script within the
#  folder stated (or the current folder) and if that is not found, then the
#  online file is downloaded and saved. Lastly, the version numbers are
#  compared between the files and if the online version is newer, then it is
#  downloaded and saved. If the versions are equal, then nothing is done, but
#  if the online version is earlier then a warning is printed to the console

def get_dependency(script: str, path: str='') -> None:
    
    online_version = None
    local_version = None
    webpath = 'https://raw.githubusercontent.com/davidf628/mypythonlib/refs/heads/main/'

    # try to get the online version number
    webloc = webpath + script
    try:
        response = requests.get(webloc)
        response.raise_for_status()
        online_version = get_script_version(webpath, script)
    except requests.exceptions.HTTPError:
        print(f'\n\n -- WARNING: Resource URL {webloc} not found.')
    except requests.exceptions.RequestException:
        exit() # just assume there is no internet connection

    # try to get the local version number
    scriptloc = os.path.join(path, script)
    if os.path.exists(scriptloc):

        local_version = get_script_version(path, script)

        if online_version > local_version:
            download_online_resource(webloc, scriptloc)
            print(f' - \nUpdating local library {scriptloc} - \n')
        elif online_version < local_version:
            print(f'\n\n-- WARNING: Local script {scriptloc} has a higher version number than online')
    
    else:
        download_online_resource(webloc, scriptloc)
        print(f' - \nUpdating local library {scriptloc} - \n')


###############################################################################
# Looks through a script for a line that contains $VERSION = a.b.c and
#  returns the tuple (a,b,c). If no version information is found, then version
#  (0,0,0) is returned. You can look for this in an online file if path is a 
#  URL, or you can check a file on the computer if path is a directory

def get_script_version(path: str, script: str) -> tuple:
    web_resource = path.startswith('http')

    # get data from file online
    if web_resource:
        webloc = f'{path}{script}' if path.endswith('/') else f'{path}/{script}'
        response = requests.get(webloc)
        if str(response) == '<Response [404]>':
            SystemExit(f'Dependency: {webloc} not found')
        # convert output from bytes to string
        payload = str(response.content)
        data = payload.splitlines()

    # get data from file on computer
    else:
        scriptloc = os.path.join(path, script)
        try:
            with open(scriptloc, 'r') as file:
                data = file.readlines()
        except OSError:
            SystemExit(f'Dependency: {scriptloc} not found')

    # go through data looking for version information        
    for line in data:
        version = extract_version(line)
        if version != None:
            return version
        
    # if no version was found, just send back (0,0,0) as a default
    # so no comparisons against None are made
    return (0,0,0)

def extract_version(line: str) -> tuple | None:
    pattern = r'\$VERSION\s*==\s*(\d+)\.(\d+)\.(\d+)'
    match = re.search(pattern, line)
    if match:
        return tuple(map(int, match.groups()))
    return None

def download_online_resource(webloc, scriptloc):
    response = requests.get(webloc)
    with open(scriptloc, mode='wb') as file:
        file.write(response.content)
    