import rich
from rich.console import Console

console = Console()

def Menu():
    menu = [
        "reply in chat",
        "reply to all chats",
        "reply in pm",
        "join chat/channel",
        "set reactions to messages/posts",
        "bite bot (holey moon/bite-bot)"
    ]

    for index, menu in enumerate(menu, 1):
        console.print(
           "([bold red]{index}[/]) {menu}"
           .format(index=index, menu=menu)
        )
