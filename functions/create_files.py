import os
import csv

from libs.eth_async.utils.utils import update_dict
from libs.eth_async.utils.files import touch, write_json, read_json

from data import config


def create_files():
    touch(path=config.FILES_DIR)

    if not os.path.exists(config.PRIVATE_FILE):
        with open(config.PRIVATE_FILE, 'w') as f:
            pass
    if not os.path.exists(config.ADDRESS_FILE):
        with open(config.ADDRESS_FILE, 'w') as f:
            pass

create_files()
