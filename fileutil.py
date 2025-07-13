# $VERSION = 1.1.0

import os, sys
from pathlib import Path

# 12/14/24 - changed name from 'select_valid_path'    
def select_valid_folder(folder_options: (list | str)) -> (str | None):
    '''
    Checks to see if any folder_options are valid folders on the current
    machine. This is especially useful for finding a root one-drive folder.
    
    folder_options -- An array of string containing paths to the different 
      folders to check. This can also be a single string.
    
    returns -- A string that is the first valid folder within folder_options,
      or None if no valid folders existed.
    '''

    if isinstance(folder_options, str):
        folder_options = [ folder_options ]

    for folder in folder_options:
        if os.path.isdir(folder):
            return folder
        
    return None

    
def select_valid_file(file_options):
    '''
    Checks to see if any file_options are valid files on the current
    machine.
    
    file_options -- An array of string containing paths to the different
      files to check. This can also be a single string.
    
    returns -- A string that is the first valid file within file_options,
      or None if no valid files existed.
    '''
    if isinstance(file_options, str):
        file_options = [ file_options ]

    for file in file_options:
        if os.path.exists(file):
            return file
        
    return None


# deprecated on 12/14/24 since this is basically the same function as get_file_path

###############################################################################
## Tests to see if a file exists within a given root path that is known 
##   already to exist. The filename can contain subdirectories, and it the 
##   function will adjust for the platform

# def file_exists_in_path(path, filename):

#     filepath = get_file_path(path, filename)

#     if os.path.exists(filepath):
#         return filepath
#     else:
#         return None


# 12/14/2024 - renamed from 'make_filepath'
def get_file_path(base_path: str, file_loc: str, check_exists=True) -> (str | None):
    '''
    Takes a base_path such as /usr/person and another file_loc, which might 
    look like /subfolder/file.txt, and creates a string that is an operating 
    system independent path to the file. 

    base_path -- a folder location on the current machine that is valid.
    file_loc -- a path to a file within the base_path.
    check_exists -- tests to see if the path exists or not, if it doesn't
      then None is returned

    returns -- a string with base_path and file_loc joined into a single path
      if the file exists, otherwise it will return None; if check_exists is
      set to False, then it will return the path regardless of existence
    '''
    path_parts = file_loc.split('/')
    file_path = os.path.join(base_path, *path_parts)

    if not check_exists:
        return file_path
    
    if os.path.exists(file_path):
        return file_path
    else:
        return None
    

def makepath(basepath: str, target: str, create :bool=False, folder :bool=True) -> str:
    """Creates a path as a string, for a file or folder. If the file or folder
    needs to be created, then a flag can be sent indicating this, but this 
    function will not create a file or folder by default. If creation is desired
    then another flag indicating whether the output should be a file or folder
    is required."""
    
    newpath = os.path.join(basepath, target)
    if os.path.exists(newpath):
        return newpath
    elif create == True:
        if folder == True:
            ogpath = os.getcwd()
            os.chdir(basepath)
            os.mkdir(target)
            os.chdir(ogpath)
            return newpath
        else:
            ogpath = os.getcwd()
            os.chdir(basepath)
            Path(target).touch()
            os.chdir(ogpath)
            return newpath
    else:
        sys.exit(f'The path {newpath} does not exist.')


###############################################################################
# Deletes a file no longer needed from disk

def remove_file(dir, filename):
    path = os.path.join(dir, filename)
    if os.path.exists(path):
        os.remove(path)


def file_is_open(filename):

    if os.path.exists(filename):
        try:
            os.rename(filename, filename)
            return False
        except OSError:
            return True