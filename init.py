import os, requests

def set_script_path(dir):
    save_path = os.getcwd()

    ## Change the current working directory to the script directory
    script_path, script_filename = os.path.split(__file__)
    if os.path.exists(script_path):
        os.chdir(script_path)
    else:
        SystemExit(f'ERROR: Script path "{script_path}" does not exist')
    
    return save_path

def get_dependency(script, path=''):
    website = 'https://raw.githubusercontent.com/davidf628/mypythonlib/refs/heads/main/'
    if script != '':
        script = os.path.join(path, script)
    website += script
    if not os.path.exists(script):
        response = requests.get(website)
        with open(script, mode='wb') as file:
            file.write(response.content)