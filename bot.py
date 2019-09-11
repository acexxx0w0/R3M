import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='o')

@bot.event
async def on_ready():
     print("bot is online")

bot.run('NjIwOTQwMzMzMTM1NDI5Njcy.XXkc4w.7hA1GHQU1tUuG_xAD1dIKL-aP6o')