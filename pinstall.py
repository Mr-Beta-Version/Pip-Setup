#Programme By Mr. Beta
#You Can Use It On Your Scrept

import os
from os import system as run
py = 'python3 -m'

def install(module_name):
    run(f'{py} pip install --force-reinstall {module_name}')
"""
Uses:
from pinstall import install as m_install
try:import requests
except:m_install('requests')
try:import rich
except:m_install('rich')

"""
