import discord
from ABT import *
from KGB import *
from discord.ext import commands
from discord import app_commands


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
guildID = 1070636380687978496  # Guild ID where the command is registered

class abot(discord.Client):
    def __init__(self):  # __init__
        super().__init__(intents=discord.Intents.all())

    async def on_ready(self):
        # Register commands in a specific guild (server)
        await tree.sync(guild=discord.Object(id=int(guildID)))
        print("Bot has connected and started successfully")

bot = abot()
tree = app_commands.CommandTree(bot)

air_regiment_fob(tree, guildID)
police_regiment_bunk(tree, guildID)

# Read the bot token from a file and run the bot
with open('secret/secret_key.txt', 'r') as file:
    TOKEN = file.readline().strip()
bot.run(TOKEN)
