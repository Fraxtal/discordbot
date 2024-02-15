import discord
from discord.ext import commands
from settings import token

client = commands.Bot(command_prefix=os.getenv("command_prefix"), case_insensitive=True)

@client.event
async def on_connect():
    print(f"{bot.user} is ready and online!")

@client.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond(f"Hey {ctx.author.mention}!")
    
@client.slash_command()
async def say(ctx, 	message = "What do you want me to say?"):
    await ctx.send(f'{message}')

client.run(token)
