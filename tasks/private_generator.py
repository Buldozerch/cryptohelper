from loguru import logger
from data.config import GENERATOR_PRIVATE_FILE, GENERATOR_ADDRESS_FILE
from libs.eth_async.client import Client


def generator():
    new_private = GENERATOR_PRIVATE_FILE 
    address_file = GENERATOR_ADDRESS_FILE
    many = int(input("How many wallets to generate? "))
    i = 0
    while i < many:
        client = Client()
        private_key = client.account._private_key.hex()
        i += 1
        with open(new_private,'a') as k:
            k.write(f"{private_key}\n")
        with open(address_file, 'a') as a:
            a.write(f"{client.account.address}\n")
    logger.success(f'Privates saved {new_private}')
    logger.success(f'Addresses saved {address_file}')

