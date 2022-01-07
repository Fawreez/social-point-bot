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

    @commands.command()
    async def unban(self, ctx, *, member):
        """Unbans a member"""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
    
    @commands.command()
    async def banlist(self, ctx):
        """Shows list of  banned members and the reason if available"""
        banned_users = await ctx.guild.bans()
        ban_list = []
        count = 0

        for ban_entry in banned_users:
            count += 1

            user = ban_entry.user
            reason = ban_entry.reason

            # Append string of banned member and their reason to a list
            # ban_list is used to create tidy output
            ban_list.append(f'{count}. Member: {user.name}#{user.discriminator}, Reason: {reason}')
        
        # Join each items in ban_list into a multiline string
        output = '\n'.join(item for item in ban_list)
        
        await ctx.send(output)


def setup(client):
    client.add_cog(BasicCommands(client))