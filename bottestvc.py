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

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))

@client.event
async def on_reaction_add(reaction, user):
    print(str(reaction.emoji))

    if user != client.user:
        if str(reaction.emoji) == "<:valorant:718711817911664650>":
            print(client.user, user.name, user.id)
            users = await reaction.users().flatten()
            await reaction.message.channel.send('<@{0}>'.format(user.id))
            print(users)
        # elif str(reaction.emoji) ==

@ client.event
async def on_message(message):
    if message.content == "!help":
        color = discord.Color.purple()
        embed = discord.Embed(color=color, title="Help on BOT",
                              description="Some useful commands")
        embed.add_field(name="!help", value="Shows Help Menu", inline=False)
        await message.channel.send(content=None, embed=embed)
    elif message.content.startswith('+'):
        # print(message.content)
        await message.channel.send("Moving...")
        

    elif message.content == "!logoff":
        await client.logout()
        exit()

async def on_reaction_remove(reaction, user):
    if user != client.user:
        if str(reaction.emoji) == "<:valorant:718711817911664650>":
            print( "removed" )
            


client.run(TOKEN)
