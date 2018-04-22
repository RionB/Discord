import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from random import choice as randchoice
import os


class Praise:

    """Rion's Praise Cog"""
    def __init__(self, bot):
        self.bot = bot
        self.praises = fileIO("data/praise/praises.json","load")

    @commands.command(pass_context=True, no_pm=True)
    async def praise(self, ctx, user : discord.Member=None):
        """praise with the user"""

        msg = ' '
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = " Y'ALL FUCKS WANT ME TO PRAISE THE SUN WITH MYSELF, HUH? DON'T HAVE ENOUGH FUCKIN' GUTS TO STEP UP AND PRAISE THIS SHIT TOO? GET INCANDESCENT, FUUUUCKIN I LOVE THE SUN, PRAISE IT"
                await self.bot.say(user.mention + msg)
            else:
                await self.bot.say(user.mention + msg + randchoice(self.praises))
        else:
            await self.bot.say(ctx.message.author.mention + msg + randchoice(self.praises))


def setup(bot):
    bot.add_cog(Praise(bot))