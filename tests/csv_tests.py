import sys, math, os
sys.path.append('../mypythonlib')
import mycsv

def test():
    test_load_csv_dict()

def test_load_csv_dict():
    data = mycsv.load_csv_dict('videodata.csv')
    print(data)
    
if __name__ == '__main__':
    
        ## Change the current working directory to the script directory
    script_path, script_filename = os.path.split(__file__)
    if os.path.exists(script_path):
        os.chdir(script_path)
    else:
        SystemExit(f'ERROR: Script path "{script_path}" does not exist')
    
    test()
    