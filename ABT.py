import discord
from spreadsheet import *
discord_log = [1306264092578943026]  # List of allowed channel IDs
ABT_Spreadsheet = "1w353ypmPGK1s3y1k0zm0RaLMbi2BXktVKWQXwosZIGo"
ABT_log_sheet = 1525863672

def air_regiment_fob(tree, guildID):
    @tree.command(name="fob", description="Used to log any FOB supply/build to 200k", guild=discord.Object(id=int(guildID)))
    async def log(interaction: discord.Interaction,
                  steamid: str):

        full_nickname = interaction.user.nick
        if "|" in full_nickname:
            nickname = full_nickname.split("|")[0].split()[2]
        else:
            nickname = full_nickname.split()[2]

        if interaction.channel_id not in discord_log:
            await interaction.response.send_message("This command is not available in this channel. Please contact server administrator.", ephemeral=True)
            return

        await interaction.response.send_message("Request has been sent", ephemeral=True)
        print(f"{nickname} ({steamid}) has requested a log for FOB quota/n")
        send_request(steamID=steamid, spreadsheet_ID=ABT_Spreadsheet, sheet_ID=ABT_log_sheet)

