import general_config

from commands.pr import pr
from commands.gags import gags
from commands.help import help
from commands.advice import advice
from commands.musicroast import musicroast
from commands.ship import ship




command_list = ["pr", "power-ranking", "help", "advice", "musicroast", "ship"]

# https://cdn.discordapp.com/attachments/430798390041903139/783338706789859348/t51.png
async def command_handler(message):
    
    command = message.content.split(' ')[0].replace(general_config.prefix, '').lower()
    
    if command not in command_list:
        await gags(message)
    
    if command == "pr" or command == "power-ranking":
        await pr(message, general_config.prefix)
        
    if command == "help":
        await help(message, general_config.prefix)
    if command == "advice":
        await advice(message, general_config.prefix)
    if command == "musicroast":
        await musicroast(message, general_config.prefix)
    if command == "ship":
        await ship(message, general_config.prefix)