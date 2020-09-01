import json
import random
import discord
from discord.ext import commands, tasks
import time
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()

<<<<<<< HEAD
=======
messageID = None


>>>>>>> 9d1f6c5ad88bad8b8f34014c68613cd44f56fb24
@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))

@client.event
async def on_reaction_add(reaction, user):
    global messageID
    print(str(reaction.emoji))

    if user != client.user:
        if str(reaction.emoji) == "<:valorant:718711817911664650>":
            print(client.user, user.name, user.id)
            users = await reaction.users().flatten()
            await reaction.message.channel.send('<@{0}>'.format(user.id))
            print(users)
<<<<<<< HEAD
        # elif str(reaction.emoji) ==
=======
            print(messageID.id)

>>>>>>> 9d1f6c5ad88bad8b8f34014c68613cd44f56fb24

@ client.event
async def on_message(message):
    global messageID
    if message.content == "!help":
        color = discord.Color.purple()
        embed = discord.Embed(color=color, title="Help on BOT",
                              description="Some useful commands")
        embed.add_field(name="!help", value="Shows Help Menu", inline=False)
        await message.channel.send(content=None, embed=embed)
    elif message.content.startswith('+'):
        # print(message.content)
<<<<<<< HEAD
        await message.channel.send("Moving...")
        
=======
        messageID = await message.channel.send("Moving...")
        print(messageID.id)
>>>>>>> 9d1f6c5ad88bad8b8f34014c68613cd44f56fb24

    elif message.content == "!logoff":
        await client.logout()
        exit()

async def on_reaction_remove(reaction, user):
    if user != client.user:
        if str(reaction.emoji) == "<:valorant:718711817911664650>":
            print( "removed" )
            


client.run(TOKEN)
