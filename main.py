from tasks.generator import generator, accounts_address 
from functions.create_files import create_files



def option_generator():
   generator()


def option_address():
    accounts_address()


def main():
    create_files()
    print('''  Select the action:
    1) Generate Private 
    2) Save Address 
    3) Exit.''')

    try:
        action = int(input('> '))
        if action == 1:
            option_generator()
        elif action == 2:
            option_address()
    except KeyboardInterrupt:
        print()

main()
