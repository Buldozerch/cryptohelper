import os
import csv

from libs.eth_async.utils.utils import update_dict
from libs.eth_async.utils.files import touch, write_json, read_json

from data import config


def create_files():
    touch(path=config.FILES_DIR)
    if not os.path.exists(config.GENERATOR_PRIVATE_FILE):
        with open(config.GENERATOR_PRIVATE_FILE, 'w') as f:
            pass
    if not os.path.exists(config.GENERATOR_ADDRESS_FILE):
        with open(config.GENERATOR_ADDRESS_FILE, 'w') as f:
            pass

    if not os.path.exists(config.PROXY_FILE):
        with open(config.PROXY_FILE, 'w') as f:
            pass

    if not os.path.exists(config.FORMATED_PROXY_FILE):
        with open(config.FORMATED_PROXY_FILE, 'w') as f:
            pass

    if not os.path.exists(config.DISPERSE_PRIVATE_FILE):
        with open(config.DISPERSE_PRIVATE_FILE, 'w') as f:
            pass

    try:
        current_settings: dict | None = read_json(path=config.SETTINGS_FILE)
    except Exception:
        current_settings = {}

    settings = {
        'disperse_private_key': '',
        'network_name': 'Sepolia',
        'network_rpc': 'https://sepolia.drpc.org',
        'disperse_value': 0.0001,
    }
    write_json(path=config.SETTINGS_FILE, obj=update_dict(modifiable=current_settings, template=settings), indent=2)
create_files()

