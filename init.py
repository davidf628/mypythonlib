import os, requests

def get_dependency(script, path=''):
    website = 'https://raw.githubusercontent.com/davidf628/mypythonlib/refs/heads/main/'
    if script != '':
        script = os.path.join(path, script)
    website += script
    if not os.path.exists(script):
        response = requests.get(website)
        with open(script, mode='wb') as file:
            file.write(response.content)