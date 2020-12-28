import general_config
import discord
from command_handler import command_handler

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(general_config.prefix):
        await command_handler(message)


client.run(general_config.bot_token)
