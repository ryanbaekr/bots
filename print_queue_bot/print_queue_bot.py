import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    for attachment in message.attachments:
        if attachment.filename.endswith('.pdf'):
            await attachment.save(os.path.join(os.path.dirname(__file__), 'temp.pdf'))
            
            os.system('lp "' + os.path.join(os.path.dirname(__file__), 'temp.pdf') + '"')

bot.run('YOUR_BOT_TOKEN')
