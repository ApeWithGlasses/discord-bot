from dotenv import dotenv_values
import discord
from discord.ext import commands

sc = dotenv_values(".env")

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("----------------------------")
    print("The bot is now ready for use")
    print("----------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am ApeWithGlasses Bot")

client.run(sc["BOT_TOKEN"])
