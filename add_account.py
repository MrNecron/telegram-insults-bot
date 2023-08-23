import os
import rich
import glob
import random

from pyrogram import Client

from rich.console import Console
from rich.prompt import Confirm

from function_settings.settings import SessionSettings

console = Console()

class AddAccount(SessionSettings):
        
      def __init__(self):
          super().__init__()

          self.choice = None
          self.functions()
             
      def functions(self):
          function = ["Add account", "Delete session"]
            
          for index, function in enumerate(function, 1):
              console.print(
                 "[bold white]({index}) {function}[/]"
                 .format(index=index, function=function)
              )

          self.choice = console.input(">> ")

          if self.choice == "1":
             self.add_session()

          elif self.choice == "2":
               self.delete_session()
                  
      def add_session(self):                              
          app = Client(
             self.session_name,
             api_id=self.api_id,
             api_hash=self.api_hash,
             device_model=self.device_model
          )

          with app:
               acc = app.get_me()
         
          console.print(f"[bold green][+][/] {acc.first_name} -> {acc.id}")
                   
      def delete_session(self):
          delete = Confirm.ask("[bold red]delete all sessions?")

          try:
             if not delete:
                name_session = console.input("[bold magenta]session name> ")
                  
                os.remove(f"{name_session}.session")
                console.print(f"[+] {name_session}.session - Deleted")
        
             else:
                 for sessions in glob.glob("*.session"):
                     os.remove(sessions)
                     console.print(f"[+] {sessions} - Deleted")

          except FileNotFoundError:
                 console.print(
                    f"Session not found: '{name_session}.session'",
                    style="bold"
                  )  
                      
AddAccount()
