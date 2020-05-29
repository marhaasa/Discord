import discord
import random
import config

from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Response time: {round(client.latency * 1000)}ms')

@client.command(aliases=["8ball", "eightball", "Eightball"])
async def _8ball(ctx, *, question):
    response = [
        "Yes.",
        "No.",
        "Maybe.",
        "Absolutely not.",
        "Shut up."
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(response)}')


client.run(config.bot_token)