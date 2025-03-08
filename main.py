import asyncio
import tasks.logo
import inquirer
from colorama import Fore, Style
from tasks.private_generator import generator 
from tasks.proxy_formater import process_proxy_file
from functions.create_files import create_files
from tasks.disperse import start_disperse, start_withdraw_native



def option_generator():
   generator()

def option_proxy_formater():
    process_proxy_file()

async def option_disperse():
    await start_disperse()

async def option_collect_native():
    await start_withdraw_native()

async def main():
    create_files()
    questions = [
            inquirer.List(
                "action",
                message=Fore.CYAN + "Select the action:" + Style.RESET_ALL, 
                choices=[
                    "Generate Private and Save Addresses",
                    "Formate proxys",
                    "Diperse Native",
                    "Collect Native",
                    "Exit",
                ],
            )
        ]

    answer = inquirer.prompt(questions)["action"]

    if answer == "Generate Private and Save Addresses":
        option_generator()
    elif answer == "Formate proxys":
        option_proxy_formater()
    elif answer == "Diperse Native":
        await option_disperse()
    elif answer == "Collect Native":
        await option_collect_native()
    elif answer == "Exit":
        print("Exiting...")

if __name__ == "__main__":
    asyncio.run(main())
