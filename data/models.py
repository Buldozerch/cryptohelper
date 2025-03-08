
from libs.eth_async.utils.files import read_json
from libs.eth_async.classes import AutoRepr, Singleton
from data.config import SETTINGS_FILE 

class Settings(Singleton, AutoRepr):
    def __init__(self):
        json_data = read_json(path=SETTINGS_FILE)

        self.disperse_private_key: str = json_data['disperse_private_key']
        self.network_name: str = json_data['network_name']
        self.network_rpc: str = json_data['network_rpc']
        self.disperse_value: float = json_data['disperse_value']
