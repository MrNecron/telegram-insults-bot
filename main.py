#маин говно - Исправления будут

from files.reply_chat import ReplyChat
from files.reply_pm import ReplyPM
from files.join import Joiner
from files.reply_all import ReplyAll
from files.reaction import SetReactions
from files.bite_bot import BiteBot

from sys import platform
from rich.console import Console

from menu import Menu
 
console = Console()

if platform == "win32":
   console.print("You have Windows installed, some functions may not work. (I recommend installing Linux or Termux)", style="bold red")
   
def main():

    Menu()
    
    try:
        option = int(console.input("\n[bold]#> "))

        if option == 1:
           ReplyChat()

        elif option == 2:
             ReplyAll()

        elif option == 3:
             ReplyPM()

        elif option == 4:
             Joiner()

        elif option == 5:
             SetReactions()

        elif option == 6:
             BiteBot()
                                    
    except KeyboardInterrupt:
        console.print("https://t.me/vesron_xx")   
                     
if __name__ == "__main__":
   main()
    

       
