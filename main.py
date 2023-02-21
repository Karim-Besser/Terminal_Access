import os
import getpass

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()


user_name=getpass.getuser()
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
print(color.BOLD+color.BLUE+"Welcome to "+color.YELLOW+"Terminal access V1"+color.END+color.BOLD+color.BLUE+" created by "+color.CYAN+"Karim Besser"+color.END)
print("")

while True:
    try:
        user_input=input(color.BOLD+color.YELLOW+user_name+"> "+color.END+color.DARKCYAN+color.BOLD)
        if user_input == "exit" or user_input == "Exit" or user_input == "EXIT" or user_input == "quit" or user_input == "Quit" or user_input == "QUIT":
            break
        os.system(user_input)
    except KeyboardInterrupt:
        clear()
        print(color.BOLD+color.YELLOW+"Exiting!"+color.END)
        break