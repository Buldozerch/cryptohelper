import os
import sys
from pathlib import Path
from loguru import logger


if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

FILES_DIR = os.path.join(ROOT_DIR, 'files')

GENERATOR_PRIVATE_FILE = os.path.join(FILES_DIR, 'generator_private.txt')
GENERATOR_ADDRESS_FILE = os.path.join(FILES_DIR, 'generator_address.txt')

PROXY_FILE = os.path.join(FILES_DIR, 'proxy.txt')
FORMATED_PROXY_FILE = os.path.join(FILES_DIR, 'formated_proxy.txt')

DISPERSE_PRIVATE_FILE = os.path.join(FILES_DIR, 'disperse_private.txt')

SETTINGS_FILE = os.path.join(FILES_DIR, 'settings.json')

LOG_FILE = os.path.join(FILES_DIR, 'log.log')
ERRORS_FILE = os.path.join(FILES_DIR, 'errors.log')

logger.add(ERRORS_FILE, level='ERROR')
logger.add(LOG_FILE, level='INFO')

