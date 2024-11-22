import discord
from spreadsheet import *
discord_log = [1306264126481367050]  # List of allowed channel IDs
KGB_Spreadsheet = "1ASCwTHJ-jXTlWC8tVfEqxAb5bwW-32W6DcpAzOoZWQc"
KGB_log_sheet = 893212261

def police_regiment_bunk(tree, guildID):
    @tree.command(name="bunk", description="Used to log any bunk inspections", guild=discord.Object(id=int(guildID)))
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
        print(f"{nickname} ({steamid}) has requested a log for bunk quota/n")
        send_request(steamID=steamid, spreadsheet_ID=KGB_Spreadsheet, sheet_ID=KGB_log_sheet)

