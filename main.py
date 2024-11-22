from ABT import *
from KGB import *
from discord.ext import commands
from discord import app_commands


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
guildID = 1070636380687978496

class abot(discord.Client):
    def __init__(self):  # __init__
        super().__init__(intents=discord.Intents.all())

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=int(guildID)))
        print("Bot has connected and started successfully")

bot = abot()
tree = app_commands.CommandTree(bot)

air_regiment_fob(tree, guildID)
police_regiment_bunk(tree, guildID)

with open('secret/secret_key.txt', 'r') as file:
    TOKEN = file.readline().strip()
bot.run(TOKEN)
