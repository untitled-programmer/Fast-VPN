# By using and changing FAST VPN, you agree that you will only use FAST VPN for Ethical hacking only, you are responsible for any damage caused by using the program.


import os
from colorama import Fore
import time
import random

# Numbers and countries!

numb=("0","1","2","3","4","5","6","7","8","9","10","11","12","13")
country=("Russia","Iceland","the USA","Norway","Mexico","Japan")
num = random.choice(numb)
con = random.choice(country)


# INSERT HERE THE CODE YOU WANT TO RUN ON THE OTHER COMPUTER!


#------------------------------------------------------------

# The CLI

def menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "███████  █████  ███████ ████████     ██    ██ ██████  ███    ██ ")
    print("██      ██   ██ ██         ██        ██    ██ ██   ██ ████   ██ ")
    print("█████   ███████ ███████    ██        ██    ██ ██████  ██ ██  ██ ")
    print("██      ██   ██      ██    ██         ██  ██  ██      ██  ██ ██ ")
    print("██      ██   ██ ███████    ██          ████   ██      ██   ████ ")
    input(Fore.RESET + "Press enter to connect. . .")
    os.system("cls" if os.name == "nt" else "clear")
    print("Connecting. . .  (please wait, this may take up to 10 seconds)")
    time.sleep(int(num))
    input(Fore.GREEN + f"\nSuccessfully connected in {num} seconds to {con}! Press enter or close the window to stop the connection!. . .")
    print(Fore.RESET + "")
    os.system("cls" if os.name == "nt" else "clear")

menu()                                                               