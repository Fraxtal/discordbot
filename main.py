import discord
from settings import token
from commands import ping

bot = discord.Bot()

# @bot.event
# async def on_ready():
#     print(f"Logged into discord api as: {bot.user}")

# @bot.slash_command()
# async def hello(ctx, name: str = None):
#     name = name or ctx.author.name	
#     await ctx.respond(f"Hello {name}!")

# @bot.user_command(name="Say Hello")
# async def hi(ctx, user):
#     await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

@bot.event
async def on_connect():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond(f"Hey {ctx.author.mention}!")
    
@bot.slash_command()
async def say(ctx, 	message = "What do you want me to say?"):
    await ctx.send(f'{message}')


bot.add_command(ping)
bot.run(token)
