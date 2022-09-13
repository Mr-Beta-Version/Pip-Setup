#Programme By Mr. Beta
#You Can Use It On Your Scrept
import os
from os import system as run
py = 'python3 -m'

def b_install(module):
    while True:
        try:
            import module
            break
        except:
            run(f'{py} pip install {module}')

"""
Uses:
from pinstall import b_install as m_install
m_install('requests')
m_install('rich')

"""
