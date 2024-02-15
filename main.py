import discord
from discord.ext import commands
from settings import token

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} is ready and online!")

@client.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond(f"Hey {ctx.author.mention}!")
    
@client.slash_command()
async def say(ctx, 	message = "What do you want me to say?"):
    await ctx.send(f'{message}')

@client.event
async def on_message(ctx,message = "F"):
    await message.channel.send(f"Fk u!")

client.run(token)
