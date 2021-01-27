# Bootleg Role Assign
# Created 01/23/21

import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
extensions = ["general", "update"]

TOKEN = os.getenv("DISCORD_TOKEN")

if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)

bot.remove_command("help")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    for guild in bot.guilds:
        print(guild.name + " (id: " + str(guild.id) + ")")

    game = discord.Game("!roleinfo")
    await bot.change_presence(status=discord.Status.online, activity=game)


bot.run(TOKEN)
