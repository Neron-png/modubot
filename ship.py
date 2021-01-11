import random

async def ship(message, prefix):

    # message.content == !ship <@!209403862736437248> <@!209403862736437248>

    # Split message params
    params = message.content.split(" ")
    params = list(filter(None, params))


    if len(params) != 3:
        await message.channel.send("Invalid arguments, correct usage:\n`!ship @name#xxxx @name2#xxxx`")
        return

    if params[1] == params[2]:
        sendString = "Yeah, yeah.. you may believe in self-love and all that, but I can't ship a person with themselves! :stuck_out_tongue_winking_eye:"
        await message.channel.send(sendString)
        return


    user_IDs = message.raw_mentions
    user_names = [message.mentions[0].name, message.mentions[1].name]



    seed = user_IDs[0] + user_IDs[1]
    random.seed(seed)

    shipName = str(user_names[0][0:len(user_names[0]) // 2] + user_names[1][len(user_names[1]) // 2:len(user_names[1])])

    if random.randrange(0, 2) == 1:

        sendString = ":heart: I Ship it, **{}**! These two were meant to be together :heart:".format(shipName)

    else:
        sendString = ":broken_heart: *{}* doesn't sound right.. It just wasn't meant to be :broken_heart:".format(shipName)

    await message.channel.send(sendString)



    #await message.channel.send("test")