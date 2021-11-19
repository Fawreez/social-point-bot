from constants import API_TOKEN
from discord.ext import commands
import os

#Creates a bot object
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is online!')

#loads all cogs in the cogs/ folder
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Initializes bot
client.run(API_TOKEN)