import toml
import rich
import random
from typing import List

class FunctionSettings:

      def __init__(self):
      
          with open("words.txt", "r") as file:
               self.words = file.read().split("\n")

          with open("config.toml") as file:
               config = toml.load(file)["settings"]

          self.min_time: int = config["min_time"]
          self.max_time: int = config["max_time"]
          self.strings: List[str] = config["strings"]
          self.emoji: List[str] = config["emoji"]
                    

      def anti_protection(self, protection: str) -> str:
          if protection:
             with open("insults.txt") as file:
                  self.words = file.read().split("\n")  

      def correct_link(self, link: str) -> str:
          if not "/+" in link:
             if not "/joinchat" in link:
                link = link[13:]

             else:
                 link.replace("/joinchat/", "/+")
          else:
              link = link

          return link
                                
class SessionSettings:

      def __init__(self):
          
          devices: List[str] = ["Samsung galaxy s23 ultra", "Samsung galaxy s23+", "Samsung galaxy s22+", "Samsung galaxy m23", "Samsung a23 4g", "Samsung m13", "Samsung galaxy s21 fe 5g"]

          with open("config.toml") as file:
               config = toml.load(file)["session"]

          self.api_id: int = config["api_id"]
          self.api_hash: str = config["api_hash"]
          self.session_name: str = config["session_name"]
          self.device_model: str = random.choice(devices)                     
      
