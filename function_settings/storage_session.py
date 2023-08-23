import rich
import toml

from pyrogram import Client
from rich.console import Console

console = Console()

with open("config.toml") as file:
     config = toml.load(file)["session"]

api_id = config["api_id"]
api_hash = config["api_hash"]
session_name = config["session_name"]

app = Client(session_name, api_id, api_hash)

with app:
     acc = app.get_me()
     string_session = app.export_session_string()
               
session = Client(session_name, session_string=string_session)
console.print(f"CONNECTED: {acc.first_name}/{session_name}.session\n")
