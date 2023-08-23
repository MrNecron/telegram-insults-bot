import rich
import random
import asyncio

from pyrogram import Client, filters, enums

from rich.console import Console

from function_settings.storage_session import session
from function_settings.settings import FunctionSettings

console = Console()

class BiteBot(FunctionSettings):

    def __init__(self):
        super().__init__()

        self.bot()  
	    
    def bot(self):
        @session.on_message(filters.all)
        async def bite(session, message):

              msg = message.text
              user = message.from_user
              
              try: 
                 if not "/+" in msg:
                    if not "/joinchat" in msg:
                       await session.join_chat(msg[13:])

                    else:
                        msg.replace("/joinchat/", "/+")
                        await session.join_chat(msg)
                 else:
                     await session.join_chat(msg)

              except:
                    Ellipsis

              else:
                  await session.send_message(user.id, "✅ Я успешно зашел, и начал оскорблять всех")
                  
              await asyncio.sleep(6)
              await session.send_chat_action(
                    message.chat.id, 
                    enums.ChatAction.TYPING
              )

              try:
                  await message.reply(random.choice(self.words))
              except Exception as error:
                     print(error)

              else:       
                  console.print(f"[+] [{message.chat.title}] {user.first_name} [{user.id}]")
              
        session.run()
      
