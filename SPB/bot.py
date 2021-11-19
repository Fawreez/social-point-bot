from constants import API_TOKEN
from discord.ext import commands

#Creates a bot object
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is online!')

#Initializes bot
client.run(API_TOKEN)