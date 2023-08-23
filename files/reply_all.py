import rich
import random
import asyncio

from pyrogram import Client, filters

from rich.console import Console
from rich.prompt import Confirm

from function_settings.settings import FunctionSettings
from function_settings.storage_session import session

console = Console()

class ReplyAll(FunctionSettings):

      def __init__(self):
          super().__init__()

          self.delay = console.input(f"[bold red]delay[/] ({self.min_time}-{self.max_time}): ")
          self.reaction = Confirm.ask("[bold red]set reactions?[/]")
          
          if not self.delay:
             self.delay = random.randint(self.min_time, self.max_time)
                                    
          self.reply_all()
          
      def reply_all(self):
          @session.on_message(filters.all)
          async def helloall(session, message):
                               
                user = message.from_user
                
                try:
                   await message.reply(random.choice(self.words))
                   await asyncio.sleep(int(self.delay))

                   console.print(f"[+] {message.chat.title} [{user.first_name}] [{user.id}]")
                   
                except Exception as error:
                       console.print("ERROR:", error, style='bold')

                if self.reaction:
                   reaction = random.choice(self.emoji)
                   
                   try:
                       await session.send_reaction(
                             message.chat.id,
                             message.id,
                             reaction  
                       )

                   except Exception as error:
                          console.print("ERROR:", error, style="bold")

                   else:
                       console.print(
                         "[bold][+] successfully delivered {reaction}[/]"
                         .format(reaction=reaction)
                       )
                       
          session.run()

