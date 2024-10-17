import sys, os
sys.path.append('../mypythonlib')
import excelfile

def test():
    test_load_csv_dict()

def test_load_csv_dict():
    data = excelfile.load_dictarray('/Users/flennerdr/Library/CloudStorage/OneDrive-CollegeofCharleston/2024fa/math-120-01/MATH-120-01 Progress Report (2024fa).xlsx')
    print(data[0])
    
if __name__ == '__main__':
    
        ## Change the current working directory to the script directory
    script_path, script_filename = os.path.split(__file__)
    if os.path.exists(script_path):
        os.chdir(script_path)
    else:
        SystemExit(f'ERROR: Script path "{script_path}" does not exist')
    
    test()
    