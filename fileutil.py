# VERSION = 1.0.1

import os, sys
from pathlib import Path
 

###############################################################################
## Tests a set of paths that are directories and checks to see if any of them
##   are valid. This is especially useful for finding a base directory (like
##   a one-drive folder) on different systems
##  
    
def select_valid_path(paths):

    if isinstance(paths, str):
        paths = [ paths ]

    for loc in paths:
        if os.path.isdir(loc):
            return loc
    return None


###############################################################################
## Tests a set of filepaths and checks to see if any of them are valid.
##  
    
def select_valid_file(filepaths):

    if isinstance(filepaths, str):
        filepaths = [ filepaths ]

    for loc in filepaths:
        if os.path.exists(loc):
            return loc
    return None


###############################################################################
## Tests to see if a file exists within a given root path that is known 
##   already to exist. The filename can contain subdirectories, and it the 
##   function will adjust for the platform

def file_exists_in_path(path, filename):

    filepath = make_filepath(path, filename)

    if os.path.exists(filepath):
        return filepath
    else:
        return None


###############################################################################
## Get a reference to a file path which is operating system independent. 

def make_filepath(path, filename):

    path_parts = filename.split('/')
    filepath = os.path.join(path, *path_parts)

    return filepath

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