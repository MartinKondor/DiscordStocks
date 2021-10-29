import os
import discord
from dotenv import load_dotenv
from discord.ext.commands import Bot
from commands import *


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
bot = Bot(command_prefix="/")


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break


    print(f"{bot.user} is connected to the following guild:")
    print(f"{guild.name}(id: {guild.id})")


bot.add_command(price_cmd)
bot.add_command(open_cmd)
bot.add_command(low_cmd)
bot.add_command(high_cmd)
bot.add_command(volume_cmd)
bot.add_command(date_cmd)
bot.add_command(prev_cmd)
bot.add_command(change_cmd)
bot.add_command(cp_cmd)
bot.run(TOKEN)
