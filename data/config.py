import os
import sys
from pathlib import Path



if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

FILES_DIR = os.path.join(ROOT_DIR, 'files')

PRIVATE_FILE = os.path.join(FILES_DIR, 'private.txt')
ADDRESS_FILE = os.path.join(FILES_DIR, 'address.txt')

