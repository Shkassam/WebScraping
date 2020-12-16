from logging import error
import os
import discord
import random
from URLscrape import theScraper
from WebScraping import scraping
from discord.ext.commands.core import has_permissions
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='*')
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    await ctx.send('I do not know what that is')
    print (error)

@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)
    if ctx.author == bot.user:
        return
    msg = ctx.content.lower()
    if 'warzone' in ctx.channel.name:
        if 'Warzone' in msg or 'warzone' in msg:
            f = open('WarzoneQuotes.txt', "r")
            quotes = f.read().splitlines()
            random.seed(a=None)
            quote = random.choice(quotes)
            f.close()
            await ctx.channel.send(quote)

@bot.event
async def on_ready():
    scrape = theScraper()
    bot.bg_task = bot.loop.create_task(scraping(scrape, bot))

@bot.command(name='AddQuote')
@has_permissions(administrator=True)
async def addQuote(ctx, *quote):
    quotes = open('WarzoneQuotes.txt',"a+")
    quotes.write('\n{}'.format(' '.join(quote)))
    quotes.close()
    await ctx.send('Added!')

@bot.command(name='Poll')
async def thePolls(ctx, *quote):
    message = await bot.get_channel(787175932808658954).send(' '.join(quote))
    await message.add_reaction('✔️')
    await message.add_reaction('❌')


bot.run(TOKEN)