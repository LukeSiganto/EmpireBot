# Work with Python 3.6
import discord
import random
import string

client = discord.Client()

def randomLine():
    global QuoteSend
    QuoteSend = (random.choice(list(open('Quotes.txt'))))
    

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('-Quote') or message.content.startswith('-quote') or message.content.startswith('-QUOTE'):
        randomLine()
        global QuoteSend
        msg = QuoteSend.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('my') or message.content.startswith('My') or message.content.startswith('MY') or message.content.startswith('mY'):
        UsrMSG = message.content
        msg = str('YOUR NEW '+(UsrMSG[3:]).upper()+'?').format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_server_join(ser):
    await bot.send_message(ser.default_channel, 'A surprise to be sure but a welcome one!'.format(ser.name))

client.run('Bot Token')
