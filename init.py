import os, requests

def get_dependency(script, path=''):
    webloc = 'https://raw.githubusercontent.com/davidf628/mypythonlib/refs/heads/main/' + script
    if script != '':
        script = os.path.join(path, script)
    if not os.path.exists(script):
        response = requests.get(webloc)
        print(f'webloc == {webloc}')
        if str(response) == '<Response [404]>':
            SystemExit(f'Dependency: {webloc} not found')
        with open(script, mode='wb') as file:
            file.write(response.content)