import requests
import discord
import json
import aiohttp
import random
import sys as s
from discord.ext import commands
import logging
#creating the bot obj with the log level of error
logging.basicConfig(level=logging.ERROR, format="[\033[33;1mpyt\033[36;1mhon\033[m] [%(asctime)s] [\033[32;1m%(levelname)s]\033[m] %(name)s: %(message)s")
token = 'BOT-TOKEN-HERE'
client = commands.Bot(command_prefix='', owner_id=666317117154525185)
hid = 666317117154525185
#change hid and owner_id to your id

#the ready event, sets the status and prints in the console when the bot is logged in
@client.event
async def on_ready():
    print(f'We have logged in as {client.user} with a latency of {round(client.latency*1000,2)}ms')
    global startlat
    tmplat = str(round(client.latency*1000,0))
    startlat = f'{tmplat[0:len(tmplat)-2]}ms'
    await client.change_presence(activity=discord.Game(name='insert status here'), status=discord.Status('idle'))

#this is the on_message event, this is what tells the bot to respond to messages
@client.event
async def on_message(message):
    if message.content.startswith('ping--'):
        msg = discord.Embed(title="Pong",description='*python*', color=0x592630)
        msg.set_thumbnail(url=client.user.avatar_url)
        msg.set_footer(text=f'created by @{client.get_user(hid)} <{hid}>', icon_url=client.get_user(hid).avatar_url)
        tmplat = str(round(client.latency*1000,0))
        msg.add_field(name='Latency Now',value=f'{tmplat[0:len(tmplat)-2]}ms',inline=False)
        msg.add_field(name='Latency At Startup',value=startlat,inline=False)
        await message.channel.send(embed=msg)
    #displays latency when a message starting with ping-- is sent

    #this is where the owner-only commands are
    if message.author.id == hid:
        if message.content.startswith('kys--') or message.content.startswith('stoppy--'):
            message.content = 'jsk--shutdown'
        if message.content.startswith('print--'): #prints in the console
            msgcont=message.content[7:len(message.content)]
            if msgcont.startswith(' '):
                msgcont = msgcont[1:len(msgcont)]
            print(msgcont)
            await message.add_reaction('\U00002705')
            return
        if message.content.startswith('echo--'): #sends a message then deletes the original msg
            msgcont=message.content[6:len(message.content)]
            await message.channel.send(content=msgcont)
            await message.delete()
            return
    #hacky command renames
    if message.content != '':
        if message.content.startswith('jsk-- help'):
            message.content = message.content.replace('jsk-- help', 'help jsk')
        if message.content.startswith('jsk--help'):
            message.content = message.content.replace('jsk--help', 'help jsk')
        if message.content.startswith('jsk-- '):
            message.content = message.content.replace('jsk-- ', 'jsk')
        if message.content.startswith('jsk--'):
            message.content = message.content.replace('jsk--', 'jsk ')
        if message.content[len(message.content)-1] == ' ':
            message.content = message.content.replace('jsk', 'jsk ')
            message.content = message.content[0:len(message.content)-1]
            if message.content[len(message.content)-1] == ' ':
                message.content = message.content[0:len(message.content)-1]
        await client.process_commands(message)
#an error handler
@client.event
async def on_command_error(ctx, error):
    if hasattr(error, 'original'):
        error = error.original
    if isinstance(error, commands.CommandNotFound):
        return
    await ctx.send(str(error))
#more hacky command renames and loads jsk devtools
client.load_extension('jishaku')
client.remove_command("jsk shutdown")
jsk = client.get_command("jsk")
@client.command(name="shutdown", aliases=["logout"])
async def jsk_shutdown(self, ctx: commands.Context):
    await ctx.send("Bye! ***-python***")
    await ctx.bot.logout()
#runs the bot
client.run(token)
