import secrets
from data.config import PRIVATE_FILE, ADDRESS_FILE
from libs.eth_async.client import Client


def generator():
    new_private = PRIVATE_FILE 
    many = int(input("How many wallets to generate? "))
    i = 0
    while i < many:
        client = Client()
        private_key = client.account._private_key.hex()
        print(private_key)
        i += 1
        with open(new_private,'a') as k:
            k.write(f"{private_key}\n")

def accounts_address():
    wallets = PRIVATE_FILE 
    address = ADDRESS_FILE 
    with open(wallets) as f:
        f = f.readlines()
        f = [line.rstrip() for line in f]
    for i in f:
        client = Client(private_key=i)
        with open(address, 'a') as k:
            print(client.account.address)
            k.write(f'{client.account.address}\n')
