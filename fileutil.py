import os, tomli

###############################################################################
## Loads a config file into a dictonary structure based on the toml format
##

def load_tomli(config_filename):

    if os.path.exists(config_filename):
        with open(config_filename, 'rb') as f:
            cfg = tomli.load(f)
        return cfg
    else:
        raise SystemExit(f'Configuration file "{config_filename}" not located.')
 

###############################################################################
## Tests a set of paths that are directories and checks to see if any of them
##   are valid. This is especially useful for finding a base directory (like
##   a one-drive folder) on different systems
##  
    
def get_valid_path(paths):

    if isinstance(paths, str):
        paths = [ paths ]

    for loc in paths:
        if os.path.isdir(loc):
            return loc
    return None


###############################################################################
## Tests a set of filepaths and checks to see if any of them are valid.
##  
    
def get_valid_file(filepaths):

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

