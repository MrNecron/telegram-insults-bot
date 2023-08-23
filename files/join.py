import rich
import asyncio

from pyrogram import Client

from rich.console import Console
from rich.prompt import Confirm

from function_settings.storage_session import session
from function_settings.settings import FunctionSettings

console = Console()

class Joiner(FunctionSettings):

      def __init__(self):
          super().__init__()
          
          link = self.correct_link(console.input("[bold red]link to chat: "))
          self.join(link)
                       
      def join(self, link):
          session.start()
          
          try:
              with console.status("Joining."):                  
                   session.join_chat(link)
                      
          except Exception as error:
                 console.print(f"ERROR: {error}")

          else:
              console.print("[green][+][/] Joined")
 
