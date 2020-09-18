 
import json
import random
import discord
from discord.ext import commands, tasks
import time
import asyncio
import os
import glob
import base64
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()

messageID = None
iconFiles = None
iconFilesidx = 0
iconFilesnum = 0


@client.event
async def on_ready():
    global iconFiles
    global iconFilesidx
    global iconFilesnum
    print('Logged on as {0}!'.format(client.user))
    # iconFiles = glob.glob("icon/*")
    # iconFilesnum = len(iconFiles)
    # iconFilesidx = 0
    # change_avatar.start()


# @tasks.loop(seconds=2)
# async def change_avatar():

#     global iconFiles
#     global iconFilesidx
#     global iconFilesnum
#     icon = iconFiles[iconFilesidx]
#     iconFilesidx = (iconFilesidx+1) % iconFilesnum
#     with open(icon, "rb") as image:
#         f = image.read()
#         b = bytearray(f)
#         await client.user.edit(avatar=b,)
#     print("changed to %s", icon)


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
        # elif str(reaction.emoji) == "<:Valorant:737828322444050442>":
            print(reaction.emoji)


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
        await message.channel.send("Moving...")

        messageID = await message.channel.send("Moving...")
        print(messageID)
        msg = await message.channel.fetch_message(messageID.id)#.add_reaction("<:Valorant:737828322444050442>")
        print(msg)
        await msg.add_reaction("<:Valorant:737828322444050442>")

    elif message.content == "!logoff":
        await client.logout()
        exit()


async def on_reaction_remove(reaction, user):
    if user != client.user:
        if str(reaction.emoji) == "<:valorant:718711817911664650>":
            print("removed")


client.run(TOKEN)
