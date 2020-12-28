

async def help(message, prefix):
    help_menu = """
Command Prefix: **{0}**
Commands:
**{0}pr / {0}power-ranking**:
    Usage: {0}pr name rank (Change the rank of a teacher)
           {0}pr (Show the ranking)
Gag commands:
**{0}hello**
    Replies Hello!
**{0}bye**
    Replies Bye!
**{0}kako**
    *We don't talk about that one!*
**{0}advice**
    *Gives useless advice*
                """.format(prefix)
    
    await message.channel.send(help_menu)