# General commands

import discord
from discord.ext import commands
import helper as h


class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # displays the bots command information & the total number of roles applied
    @commands.command()
    async def roleinfo(self, ctx):
        url = self.bot.user.avatar_url
        embed = discord.Embed(title="Available Commands", color=0xff7b00)
        embed.set_thumbnail(url=url)
        embed.add_field(name="!update", value="*Update your roles if you get promoted"
                                              "\nOnly works inside Bootleg Scrims*", inline=False)
        embed.add_field(name="!dev", value="*Displays developer information*", inline=False)
        embed.set_footer(text="developed by goose#4609 · !dev",
                         icon_url="https://cdn.discordapp.com/avatars/"
                                  "293658485210480640/067f4917d73fafde6855e40e79055067.webp?size=1024")
        await ctx.send(embed=embed)

    # displays developer information
    @commands.command()
    async def dev(self, ctx):
        embed = discord.Embed(title="Created by goose", color=0xff7b00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/"
                                "293658485210480640/067f4917d73fafde6855e40e79055067.webp?size=1024")
        embed.add_field(name="GitHub", value="coming soon...")
        embed.add_field(name="Discord", value="goose#4609")
        embed.add_field(name="Inquires", value="DM on discord", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
