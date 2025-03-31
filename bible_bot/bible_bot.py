import discord
from discord.ext import commands, tasks
import os
import datetime

with open(os.path.join(os.path.dirname(__file__), "messages.txt"), "r") as f:
    messages = f.readlines()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@tasks.loop(hours=24)
async def sunday_message():
    now = datetime.datetime.now()

    if now.weekday() == 6:
        channel = bot.get_channel(1234567890123456789)
        if channel:
            await channel.send(f"@everyone here is the plan for week {now.isocalendar().week}:" + "\n" + messages[now.isocalendar().week - 1].replace("\\n", "\n"))

@bot.event
async def on_ready():
    sunday_message.start()

bot.run("YOUR_BOT_TOKEN")
