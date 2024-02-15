import discord
from settings import token

bot = discord.Bot()

@bot.slash_command()
async def ping(ctx):
    delay = ctx.bot.latency * 1000
    await ctx.reply(f'Ping is {int(delay)} Milliseconds')
    print(f"Pinged In {ctx.guild} -- {ctx.channel}")