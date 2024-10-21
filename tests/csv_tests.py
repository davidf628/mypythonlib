import sys, os
sys.path.append('../mypythonlib')
import csvfile

def test():
    test_csvdiff()

def test_load_csv_dict():
    data = csvfile.load_csv_dict('videodata.csv')
    print(data)
    
def test_csvdiff():
    csvfile.csvdiff('videodata.csv', 'videodata2.csv', 'd2l_name')

if __name__ == '__main__':
    
        ## Change the current working directory to the script directory
    script_path, script_filename = os.path.split(__file__)
    if os.path.exists(script_path):
        os.chdir(script_path)
    else:
        SystemExit(f'ERROR: Script path "{script_path}" does not exist')
    
    test()
    