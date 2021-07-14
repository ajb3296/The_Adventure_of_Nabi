import os
import sys
from distutils.core import setup

import py2exe

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
    dlls = ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll")
    if os.path.basename(pathname).lower() in dlls:
        return 0
    return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL

sys.argv.append('py2exe')

setup(
    name =    'The Adventure of Nabi',
    version = '1.0',
    author =  'An Jaebeom',
    options = {
        'py2exe': {
            'bundle_files': 1, # doesn't work on win64
            'compressed': True,
        }
    },

    windows = [{
        'script': "nabi.py",
        'icon_resources': [
            (1, 'icon.ico')
        ]
    }],

    zipfile=None,
)
