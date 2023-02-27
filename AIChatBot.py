#Author: BinaryBills
#Creation Date: January 8, 2022
#Date Modified: January 17, 2022
#Purpose: C-3PO is a discord chatbot powered by the OpenAI API. 
#It uses the DaVinci 003 language model. It possesses the 
#ability to remember up to 100 messages. 

import os
import asyncio
import discord
from discord.ext import commands
from config import settings

#Assigns the bot's prefix for commands, permissions, and disables the default help command. 
client = commands.Bot(command_prefix = '!', intents=discord.Intents.all(), help_command = None)

async def load():
  """Loads the classes in the cog folder which encapsulates all the bot functionalities"""
  for filename in os.listdir('./cogs'):
     if filename.endswith('.py'):
         await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    """Calls the load function then launches the discord bot"""
    await load()
    await client.start(settings.TOKEN)

asyncio.run(main())