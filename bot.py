import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='o')

@bot.event
async def on_ready():
     print("bot is online")

bot.run('NjIwOTQwMzMzMTM1NDI5Njcy.XXooSg.E5ZFw9Ikt556HeC2E89lMiFfihc')