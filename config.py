# $VERSION == 1.0.0

import os, tomli

###############################################################################
## Loads a config file into a dictonary structure based on the toml format
##

def load_config(config_filename):
  
    if os.path.exists(config_filename):
        with open(config_filename, 'rb') as f:
            cfg = tomli.load(f)
        return cfg
    else:
        raise SystemExit(f'Configuration file "{config_filename}" not located.')