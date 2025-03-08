# Crypto Helper Bot

## EN:
## About  
Crypto Helper Bot is a simple tool for managing cryptocurrency wallets efficiently.  
It allows you to generate private keys, format proxies, and automate fund distribution and collection with ease.  
## Key Features  
- Generate wallets and private keys  
- Formatting proxies from any format
- Disperse funds across multiple wallets  
- Collect funds back to a single wallet  
## Installation & Setup  

### Windows  
```
py -3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
### Linux/MacOS
```
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
## How to Use
### First Launch
Run main.py for the first time—it will create a files/ directory where all data will be stored.

### Available Options
1. Generate Wallets
Creates private keys and wallet addresses.\
Data is saved in:

files/generator_private.txt\
files/generator_addresses.txt

2. Format Proxies
Place your proxies inside files/proxy.txt.\
Run main.py, choose your preferred format.\
Formatted proxies will be saved in files/formated_proxy.txt.

3. Disperse Native (Send from One Wallet to Many)
Open files/settings.json and configure your dispersing settings.\
Add private keys for dispersing in files/disperse_private.txt.
Start main.py and select this mode.

4. Collect Native (Gather from Many Wallets to One)
The bot will collect funds from all wallets listed in files/disperse_private.txt.\
Funds will be transferred to the disperser wallet set in settings.json.

#### Example Configuration (settings.json)
{
  "disperse_private_key":"private_key",\
  "network_name": "Sepolia",\
  "network_rpc": "https://sepolia.drpc.org", \
  "disperse_value": 0.0001
}

### My links
TG Channel https://t.me/buldozercode

### Support
#### Donate EVM:
0x7AE96311BEd9Fc1a32Eb99f1d62E9C2aA088bb38

#### Donate TRX:
TD6JnRN94C4sm313t7xDS9JKQkCypLhcJo

#### Donate SOL:
HgoYUmW6T6JFPCJjUvA21F5UmJ64dmWozVvcYGaxhENu

## RU:
## О софте 
Crypto Helper Bot простой инструмент для мелких задач.  
Он позволяет генерировать приватные ключи, форматировать прокси, а также автоматизировать распределение и сбор нативного баланса.    
## Главные особенности  
- Генерация приватных ключей 
- Форматирует прокси из любого формата  
- Disperse нативки из одного кошелька на множество других 
- Собирает со всех кошельков нативку на один 
## Установка 

### Windows  
```
py -3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
### Linux/MacOS
```
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
## Как использовать
### Первый запуск
Запустите в первый раз main.py для создания директории files/ и файлов в ней

### Доступные опции
1. Генерация кошельков
Создает приватные ключи и адресса кошельков.\
Сохраняет в:

files/generator_private.txt\
files/generator_addresses.txt

2. Форматирование прокси
Вставьте свои прокси любого формата в files/proxy.txt.\
Запустите main.py, выберите предпочитаемый формат.\
Форматированные прокси сохраняются в files/formated_proxy.txt.

3. Disperse Нативки (Отправляет с одного кошелька на множество других)
Откройте files/settings.json и заполните своими настройками.\
Добавьте приватные ключи для дисперса в files/disperse_private.txt.
Запустите main.py и выберите эту опцию.

4. Сбор Нативки (Отправляет с множества кошельков нативку на один)
Бот отправит весь нативный баланс с кошельков в files/disperse_private.txt.\
Нативка будет отправлена на кошелек указанный в settings.json.

#### Пример конфигурации (settings.json)
{
  "disperse_private_key":"private_key",\
  "network_name": "Sepolia",\
  "network_rpc": "https://sepolia.drpc.org", \
  "disperse_value": 0.0001
}
### Мои ссылки
TG канал https://t.me/buldozercode

### Support
#### Donate EVM:
0x7AE96311BEd9Fc1a32Eb99f1d62E9C2aA088bb38

#### Donate TRX:
TD6JnRN94C4sm313t7xDS9JKQkCypLhcJo

#### Donate SOL:
HgoYUmW6T6JFPCJjUvA21F5UmJ64dmWozVvcYGaxhENu
