from logging import error
import os
import asyncio
import time
import discord
import random
from URLscrape import theScraper
from ColorsWow import colors
from discord.ext.commands.core import has_permissions
from discord.ext import commands
from dotenv import load_dotenv

async def scraping(scrape):
    while True:
        MEMStrix = scrape.MEMStrixScrape()
        if MEMStrix[0]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(MEMStrix[1]))
        else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} MemoryExpress.com{colors.END}  Asus ROG Strix  {colors.RED} OUT OF STOCK{colors.END}')
        AMZStrix = scrape.AMZStrixScrape()
        if AMZStrix[0] and AMZStrix[2]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(AMZStrix[1]))
        elif (AMZStrix[2] != True) and AMZStrix[0]: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Amazon.ca        {colors.END}  Asus ROG Strix  {colors.YELLOW} OVERPRICED {AMZStrix[3]}{colors.END}')
        else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Amazon.ca        {colors.END}  Asus ROG Strix  {colors.RED} OUT OF STOCK{colors.END}')        
        NEEStrix = scrape.NEEStrixScrape()
        if NEEStrix[0]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(NEEStrix[1]))
        else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Newegg.ca        {colors.END}  Asus ROG Strix  {colors.RED} OUT OF STOCK{colors.END}')
        BBYStrix = scrape.BBYStrixScrape()
        if BBYStrix[0]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(BBYStrix[1]))
        else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} BestBuy.ca       {colors.END}  Asus ROG Strix  {colors.RED} OUT OF STOCK{colors.END}')
        MEMTuf = scrape.MEMTufScrape()
        if MEMTuf[0]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(MEMTuf[1]))
        else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} MemoryExpress.com{colors.END}  Asus TUF Gaming {colors.RED} OUT OF STOCK{colors.END}')
        NEETuf = scrape.NEETufScrape()
        if NEETuf[0]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(NEETuf[1]))
        else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Newegg.ca        {colors.END}  Asus TUF Gaming {colors.RED} OUT OF STOCK{colors.END}')
        BBYTuf = scrape.BBYTufScrape()
        if BBYTuf[0]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(BBYTuf[1]))
        else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} BestBuy.ca       {colors.END}  Asus TUF Gaming {colors.RED} OUT OF STOCK{colors.END}')
        AMZTuf = scrape.AMZTufScrape()
        if AMZTuf[0] and AMZTuf[2]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(AMZTuf[1]))
        elif (AMZTuf[2] != True) and AMZTuf[0]: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Amazon.ca        {colors.END}  Asus TUF Gaming {colors.YELLOW} OVERPRICED {AMZTuf[3]}{colors.END}')
        else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Amazon.ca        {colors.END}  Asus TUF Gaming {colors.RED} OUT OF STOCK{colors.END}')
        NEER9X = scrape.NEER9XScrape()
        if NEER9X[0]: await bot.get_channel(783206568111767583).send('<@!267055271556284426> <@!219274149007196161> {}'.format(NEER9X[1]))
        else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Newegg.ca        {colors.END}  Ryzen 9 5900x   {colors.RED} OUT OF STOCK{colors.END}')
        await asyncio.sleep(180)

async def PS5Scrape(scrape, ctx):
    id = ctx.author.id
    await bot.get_channel(784691793978720276).send('<@!{}> Ill ping you here for the PS5'.format(str(id)))
    while True:
        BBYPS5 = scrape.BBYPS5Scrape()
        if BBYPS5[0]: await bot.get_channel(784691793978720276).send('<@!{}> {}'.format(str(id), BBYPS5[1]))
        else: await bot.get_channel(784691793978720276).send('PS5 Out of Stock on BestBuy.ca')
        await asyncio.sleep(60)

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
    await bot.get_channel(697974751989203074).send('Bot is Running!')
    bot.bg_task = bot.loop.create_task(scraping(scrape))

@bot.command(name='PS5')
@has_permissions(administrator=True)
async def PS5_Stock(ctx):
    scrape = theScraper()
    await ctx.send('Alright I will track the PS5 for you!')
    bot.bg_task = bot.loop.create_task(PS5Scrape(scrape, ctx))

@bot.command(name='AddQuote')
@has_permissions(administrator=True)
async def addQuote(ctx, *quote):
    quotes = open('WarzoneQuotes.txt',"a+")
    quotes.write('\n{}'.format(' '.join(quote)))
    quotes.close()
    await ctx.send('Added!')

bot.run(TOKEN)