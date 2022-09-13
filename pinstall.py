#Programme By Mr. Beta
#You Can Use It On Your Scrept

import os
from os import system as run
py = 'python3 -m'

def install(module_name):
    run(f'{py} pip install --force-reinstall {module_name}')
"""
Uses:
from pinstall import install as ins
try:import requests
except:ins('requests');import requests
try:import rich
except:ins('rich');import rich

"""
