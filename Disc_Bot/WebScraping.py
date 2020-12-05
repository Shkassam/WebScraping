from logging import error
import os
import asyncio
import urllib.request
import bs4 as bs
import time
import discord
import random
from URLscrape import theScraper
from discord.ext.commands.core import has_permissions
from discord.ext import commands
from dotenv import load_dotenv


async def scraping(scrape):
    while True:
        NEEStrix = scrape.NEEStrixScrape()
        if NEEStrix[0]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(NEEStrix[1]))
        else: print(time.strftime("[%H:%M:%S] ",time.localtime()), ' Newegg.ca   The Asus ROG Strix is sold out')
        BBYTuf = scrape.BBYTufScrape()
        if BBYTuf[0]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(BBYTuf[1]))
        else: print(time.strftime("[%H:%M:%S] ",time.localtime()), ' BestBuy.ca  The Asus TUF Gaming is sold out')
        NEETuf = scrape.NEETufScrape()
        if NEETuf[0]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(NEETuf[1]))
        else:print(time.strftime("[%H:%M:%S] ",time.localtime()), ' Newegg.ca   The Asus TUF Gaming is sold out')
        BBYStrix = scrape.BBYStrixScrape()
        if BBYStrix[0]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(BBYStrix[1]))
        else: print(time.strftime("[%H:%M:%S] ",time.localtime()),' BestBuy.ca  The Asus ROG Strix is sold out')        
        NEER9X = scrape.NEER9XScrape()
        if NEER9X[0]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(NEER9X[1]))
        else: print(time.strftime("[%H:%M:%S] ",time.localtime()), ' Newegg.ca   The Ryzen 9 5900x is sold out')
        await asyncio.sleep(180)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='*')
client = discord.Client()


@bot.event
async def on_command_error(ctx, error):
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
    await bot.get_channel(697974751989203074).send('Bot is Running!')
    bot.bg_task = bot.loop.create_task(scraping(scrape))

@bot.command(name='AddQuote')
@has_permissions(administrator=True)
async def addQuote(ctx, *quote):
    quotes = open('WarzoneQuotes.txt',"a+")
    quotes.write('\n{}'.format(' '.join(quote)))
    quotes.close()
    await ctx.send('Added!')

bot.run(TOKEN)