import discord
from discord.ext import commands

class BasicCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        """Sends bot latency to chat"""

        await ctx.send('Pong!')
        await ctx.send(f"{round(self.client.latency * 1000)}ms") # It's now self.bot.latency


def setup(client):
    client.add_cog(BasicCommands(client))