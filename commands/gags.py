
async def gags(message):
    if "bye" in message.content:
        bye_str = 'Goodbye <@{}>'.format(message.author.id)
        await message.channel.send(bye_str)
    
    if "hello" in message.content:
        hey_str = 'Hello <@{}>!'.format(message.author.id)
        await message.channel.send(hey_str)
        
    if "kako" in message.content:
        await message.channel.send("https://cdn.discordapp.com/attachments/430798390041903139/783338706789859348/t51.png")