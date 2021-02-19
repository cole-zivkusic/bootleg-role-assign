# Update command

import discord
from discord.ext import commands
from discord.utils import get


class Update(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # updates a users roles inside of the discord server Bootleg Scrims
    # this is based on whether or not they are in specific child servers of the parent
    @commands.command()
    async def update(self, ctx):
        # variable for keeping track of roles applied on a per use basis
        count = 0
        # the four server ids that this bot will work out of
        prac = 720914029362675774
        t2t3 = 756216339265224714
        elite = 769244576292536391
        scrims = 756772868888461423
        # check to see that the command was called in Bootleg Scrims
        # send a message and return if it was called outside of Scrims
        if ctx.message.guild.id != scrims:
            embed = discord.Embed(title="This command is only for use in"
                                        " Bootleg Scrims. ❌", color=0xff7b00)
            embed.set_footer(text="developed by goose#4609 · contact a staff member if you have any questions",
                             icon_url="https://cdn.discordapp.com/avatars/"
                                      "293658485210480640/067f4917d73fafde6855e40e79055067.webp?size=1024")
            await ctx.send(embed=embed)
            return

        servers = [prac, t2t3, elite]

        server = self.bot.get_guild(scrims)
        # check to see if the user is in the three servers that have signifigant roles in Scrims
        # if they are, apply the role in question inside Scrims if they do not already have it
        for s in servers:
            serv = self.bot.get_guild(s)
            if serv.get_member(ctx.author.id) is not None:
                if s == prac:
                    role = get(server.roles, name="T1")
                    if ctx.author not in role.members:
                        await ctx.author.add_roles(role)
                        count += 1
                elif s == t2t3:
                    special_case = self.bot.get_guild(s)
                    sc_role2 = get(special_case.roles, name="T2")
                    sc_role3 = get(special_case.roles, name="T3")

                    role2 = get(server.roles, name="T2")
                    role3 = get(server.roles, name="T3")
                    if ctx.author in sc_role2.members and ctx.author not in role2.members:
                        await ctx.author.add_roles(role2)
                        count += 1
                    elif ctx.author in sc_role3.members and ctx.author not in role3.members:
                        await ctx.author.add_roles(role3)
                        count += 1
                elif s == elite:
                    role = get(server.roles, name="Elite")
                    if ctx.author not in role.members:
                        await ctx.author.add_roles(role)
                        count += 1
        # if they were given a role display a message
        if count > 0:
            embed = discord.Embed(title="You have been given ({}) role(s) in"
                                        " Bootleg Scrims! ✅".format(count), color=0xff7b00)
            embed.set_footer(text="developed by goose#4609 · contact a staff member if you have any questions",
                             icon_url="https://cdn.discordapp.com/avatars/"
                                      "293658485210480640/067f4917d73fafde6855e40e79055067.webp?size=1024")
            await ctx.send(embed=embed)
        # if they were not given a role display a message
        else:
            embed = discord.Embed(title="You are not eligible for any new roles in"
                                        " Bootleg Scrims. ❌", color=0xff7b00)
            embed.set_footer(text="developed by goose#4609 · contact a staff member if you have any questions",
                             icon_url="https://cdn.discordapp.com/avatars/"
                                      "293658485210480640/067f4917d73fafde6855e40e79055067.webp?size=1024")
            await ctx.send(embed=embed)

    # an error handler in the case where something goes wrong (ie. an admin has changed a roles name, etc.)
    @update.error
    async def update_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            embed = discord.Embed(title="Error ❌", color=0xff7b00)
            embed.add_field(name="Something Went Wrong...", value="please DM goose#4609 for help")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Update(bot))
