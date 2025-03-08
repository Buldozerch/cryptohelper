import asyncio
from tenacity import retry, stop_after_attempt, wait_fixed
from loguru import logger
import os
from libs.eth_async.client import Client
from libs.eth_async.data.models import Network
from libs.eth_async.data.models import  TokenAmount 
from libs.eth_async.transactions import Tx
from data.config import DISPERSE_PRIVATE_FILE
from data.models import Settings
from web3.types import TxParams


private_file = DISPERSE_PRIVATE_FILE 
if os.path.exists(private_file):
    with open(private_file, 'r') as private_file:
        disperse_private = [line.strip() for line in private_file if line.strip()]

class Disperse():
    def __init__(self, disperse_private_key: str, name_network: str, rpc: str,value: float | None = None, proxy: str | None = None) -> None:
        self.disperse_private_key = disperse_private_key
        self.name_network = name_network
        self.rpc = rpc
        self.proxy = proxy
        self.value = value

    async def create_client_network(self, private_key: str | None = None):
        try:
            network = Network(name=self.name_network, rpc=self.rpc)
            client = Client(private_key=self.disperse_private_key if not private_key else private_key, network=network, proxy=self.proxy)
            return network, client
        except Exception as e:
            logger.error(f'Error with Network. Change RPC {e}')
            return False, False


    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    async def disperse_native(self):
        network, client = await self.create_client_network()
        if not network or not client: return
        if not self.value: return logger.error(f'Please put value')
        i = 0
        for _ in disperse_private:
            try:
                value = int(TokenAmount(self.value).Wei)
                address_for_dep = Client(private_key=_, network=network)
                tx_params = TxParams(to=address_for_dep.account.address, data="0x", value=value)
                tx = await client.transactions.sign_and_send(tx_params=tx_params)
                receipt = await tx.wait_for_receipt(client=client, timeout=300)
                if receipt:
                    i += 1
                    logger.success(f'[{i}/{len(disperse_private)}] Success send Native from {client.account.address} Hash: {tx.hash.hex()}')
                else:
                    logger.error(f'Cannot send Native {client.account.address}')

            except Exception as e:
                logger.error(f'Error with dispearse {e}')


    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    async def withdraw_native_balance(self, private_key):
        try:
            network, client = await self.create_client_network(private_key=private_key)
            if not network or not client: return
            check_balance = await client.wallet.balance()
            if check_balance:
                logger.success(f'Success found Native from {client.account.address}')
                balance = float(check_balance.Ether) * 0.99
                disperse_client = Client(private_key=self.disperse_private_key)
                tx_params = TxParams(
                    to=disperse_client.account.address,
                    value=int(TokenAmount(balance).Wei)
                )
                tx = await client.transactions.sign_and_send(tx_params=tx_params)
                receipt = await tx.wait_for_receipt(client=client, timeout=300)
                if receipt:
                    logger.success(f'Success send Native from {client.account.address} Hash: {tx.hash.hex()}')
                    return True
                else:
                    logger.error(f'Cannot send Native {client.account.address}')
                    return True
            else:
                logger.warning(f'Not Native for wallet {client.account.address}')
                return None 
        except Exception as e:
            logger.error(f'Error preparing transaction: {e}')

def create_network_info():
    settings = Settings()
    disperse_private_key = settings.disperse_private_key
    if len(disperse_private_key) < 64:
        logger.error(f'Please put correct private key')
        return False, False, False, False
    name = settings.network_name
    rpc = settings.network_rpc
    value = settings.disperse_value
    return disperse_private_key, name, rpc, value

async def start_disperse():
    start_disperse = str(input('Start disperse? y/n '))
    if start_disperse not in ['y', 'Y', 'н', 'Н']: return
    disperse_private_key, name, rpc, value = create_network_info()
    if not disperse_private_key or not name or not rpc or not value: return
    disperse = Disperse(disperse_private_key=disperse_private_key,name_network=name, rpc=rpc, value=value)
    await disperse.disperse_native()
    return

async def start_withdraw_native():
    start_disperse = str(input('Start disperse? y/n '))
    if start_disperse not in ['y', 'Y', 'н', 'Н']: return
    disperse_private_key, name, rpc, value = create_network_info()
    if not disperse_private_key or not name or not rpc or not value: return
    tasks = [handle_withdraw_native(disperse_private_key, name, rpc, private) for private in disperse_private]

    task_gathering = asyncio.gather(*tasks)
    await task_gathering

async def handle_withdraw_native(disperse_private_key, name, rpc, private):
    disperse = Disperse(disperse_private_key=disperse_private_key,name_network=name, rpc=rpc)
    await disperse.withdraw_native_balance(private)
    return


