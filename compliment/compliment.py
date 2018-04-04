import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from random import choice as randchoice
import os


class Compliment:

    """Rion's Compliment Cog"""
    def __init__(self, bot):
        self.bot = bot
        self.compliments = fileIO("data/compliment/data/compliments.json","load")

    @commands.command(pass_context=True, no_pm=True)
    async def compliment(self, ctx, user : discord.Member=None):
        """compliment the user"""

        msg = ' '
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = "Oh, no need for that! You go on ahead. I will stay behind, to gaze at the sun... The sun is a wondrous body. Like a magnificent father! If only I could be so grossly incandescent!"
                await self.bot.say(user.mention + msg)
            else:
                await self.bot.say(user.mention + msg + randchoice(self.compliments))
        else:
            await self.bot.say(ctx.message.author.mention + msg + randchoice(self.compliments))


def setup(bot):
bot.add_cog(Compliment(bot))