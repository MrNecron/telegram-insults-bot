import rich
import random
import asyncio

from pyrogram import Client, filters

from rich.console import Console
from rich.prompt import Confirm

from function_settings.storage_session import session
from function_settings.settings import FunctionSettings

console = Console()

class SetReactions(FunctionSettings):

      def __init__(self):
          super().__init__()
             
          self.delay = console.input(f"[bold red]delay[/] ({self.min_time}-{self.max_time}): ")
          self.set_reaction()
                  
      def set_reaction(self):
          @session.on_message(filters.all)
          async def reaction(session, message):
              
                if not self.delay:
                   self.delay = random.randint(self.min_time, self.max_time)

                reactions = random.choice(self.emoji)
                                        
                try:
                    await session.send_reaction(
                        message.chat.id,
                        message.id,
                        reactions
                    )
                                  
                    await asyncio.sleep(int(self.delay))
                    
                    console.log(f"successfully delivered: {reactions}")
                    
                except Exception as error:
                       console.print("ERROR:", error, style='bold')
                            
          session.run()
