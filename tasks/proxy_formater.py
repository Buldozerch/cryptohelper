from loguru import logger
import re
from data.config import PROXY_FILE, FORMATED_PROXY_FILE

class Proxy():
    def __init__(self, proxy, format) -> None:
       self.proxy = proxy 
       self.format = format

    def parse_proxy(self):
        proxy = self.proxy.strip()

        proxy_type = "unknown"
        if proxy.lower().startswith("http://"):
            proxy_type = "http"
        elif proxy.lower().startswith("https://"):
            proxy_type = "https"
        elif proxy.lower().startswith("socks5://"):
            proxy_type = "socks5"
        elif proxy.lower().startswith("socks4://"):
            proxy_type = "socks4"

        proxy = re.sub(r'^(https?|socks[45])://', '', proxy, flags=re.IGNORECASE)

        parts = re.split(r'[:@\s]+', proxy)

        ip, port, login, password = None, None, None, None

        for part in parts:
            if re.match(r'^(\d{1,3}\.){3}\d{1,3}$|^\[[\da-fA-F:]+\]$', part):  
                ip = part
            elif part.isdigit() and 0 < int(part) < 65536:  
                port = int(part)
            elif login is None:  
                login = part
            else:
                password = part

        login = None if login and login.lower() == "none" else login
        password = None if password and password.lower() == "none" else password

        if not ip:
            raise ValueError(f"Не удалось найти IP в строке: {proxy}")

        return {
            "type": proxy_type,
            "ip": ip,
            "port": port,
            "login": login,
            "password": password
        }

    def format_proxy(self):
        parsed = self.parse_proxy()

        ip, port, login, password, proxy_type = parsed["ip"], parsed["port"], parsed["login"], parsed["password"], parsed["type"]

        if not port:
            raise ValueError(f"Не указан порт для прокси: {self.proxy}")

        # Форматы
        if self.format == "ip:port":
            return f"{ip}:{port}"
        
        elif self.format == "login:pass:ip:port":
            return f"{login}:{password}:{ip}:{port}" if login and password else f"{ip}:{port}"

        elif self.format == "ip:port:login:pass":
            return f"{ip}:{port}:{login}:{password}" if login and password else f"{ip}:{port}"
        
        elif self.format == "login:pass@ip:port":
            return f"{login}:{password}@{ip}:{port}" if login and password else f"{ip}:{port}"

        elif self.format == "ip:port@login:pass":
            return f"{ip}:{port}@{login}:{password}" if login and password else f"{ip}:{port}"

        elif self.format == "http://ip:port:login:pass":
            return f"http://{ip}:{port}:{login}:{password}" 

        elif self.format == "http://ip:port@login:pass":
            return f"http://{ip}:{port}@{login}:{password}" 

        elif self.format == "http://login:pass@ip:port":
            return f"http://{ip}:{port}@{login}:{password}" 

        elif self.format == "http://login:pass:ip:port":
            return f"http://{ip}:{port}@{login}:{password}" 

        elif self.format == "http://ip:port":
            return f"http://{ip}:{port}" 

        elif self.format == "socks5://ip:port:login:pass":
            return f"socks5://{ip}:{port}:{login}:{password}" 

        elif self.format == "socks5://ip:port@login:pass":
            return f"socks5://{ip}:{port}@{login}:{password}" 

        elif self.format == "socks5://login:pass@ip:port":
            return f"socks5://{ip}:{port}@{login}:{password}" 

        elif self.format == "socks5://login:pass:ip:port":
            return f"socks5://{ip}:{port}@{login}:{password}" 

        elif self.format == "socks5://ip:port":
            return f"socks5://{ip}:{port}" 
       
        else:
            raise ValueError(f"Unknown format: {format}")

def process_proxy_file():
    formatted_proxies = []

    with open(PROXY_FILE, "r", encoding="utf-8") as f:
        proxies = f.readlines()

    if not len(proxies):
        logger.warning(f'Please fill proxy file {PROXY_FILE}')
        return False

    formats = [
        "ip:port",
        "login:pass:ip:port",
        "ip:port:login:pass",
        "login:pass@ip:port",
        "ip:port@login:pass",
        "http://ip:port:login:pass",
        "http://ip:port@login:pass",
        "http://login:pass@ip:port",
        "http://login:pass:ip:port",
        "http://ip:port",
        "socks5://ip:port:login:pass",
        "socks5://ip:port@login:pass",
        "socks5://login:pass@ip:port",
        "socks5://login:pass:ip:port",
        "socks5://ip:port",
    ]
    for i, fmt in enumerate(formats, 1):
        print(f"{i}. {fmt}")

    choice = int(input("Choose format: ")) - 1
    format_type = formats[choice] if 0 <= choice < len(formats) else None 
    if not format_type: return logger.warning('Choose correct format')
    logger.info(format_type)

    for proxy in proxies:
        proxy = proxy.strip()
        if not proxy:
            continue  # Пропускаем пустые строки

        try:
            parser = Proxy(proxy=proxy, format=format_type)  # Используем твой парсер
            formatted_proxies.append(parser.format_proxy())
        except ValueError as e:
            logger.error(f"Wrong with proxy {proxy}: {e}")

    with open(FORMATED_PROXY_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(formatted_proxies))

    logger.success(f"File save: {FORMATED_PROXY_FILE}")

