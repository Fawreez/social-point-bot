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

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason='none'):
        """Kick a guild member"""
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason='none'):
        """Bans a guild member"""
        await member.ban(reason=reason)

def setup(client):
    client.add_cog(BasicCommands(client))