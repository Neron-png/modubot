

async def advice(message, prefix):
    import urllib.request, json 
    with urllib.request.urlopen("https://api.adviceslip.com/advice") as url:
        data = json.loads(url.read().decode())
    await message.channel.send(data['slip']['advice'])