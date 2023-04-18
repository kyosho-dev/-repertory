import discord
from discord.ext import commands
import os

TOKEN = 'MTAzNzgwODAyODM2NTM2NTMwOA.G9HZdZ.O-ZZ2oCv9iYDHLtKrLmcJQUZSQPXUR_JukEQqA'
intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix='!', intents=intents)




@client.event
async def on_ready():
    print('bot ready')
    channel = client.get_channel(749987945469182022)
    
    
# @client.event
# async def on_message(message):
#     channel = client.get_channel(749987945469182022)
#     print(message.author, message.content, message.channel.id)



@client.command(name="Regras")
async def hello(ctx):
    channel = client.get_channel(749987945469182022)
    await ctx.channel.send(f'As regras do servidor são:{os.linesep}1-Se comporte{os.linesep}2-Proibido links soutos{os.linesep}3- se divirta{os.linesep}4-bam e permanente')
    
    
client.run(TOKEN)