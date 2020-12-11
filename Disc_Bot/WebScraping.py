from logging import error
import asyncio
import time
from ColorsWow import colors

GEN = 783206568111767583

async def scraping(scrape, bot):
    while True:
        try: 
            CaCStrix = scrape.CaCStrixScrape()
            if CaCStrix[0]: await bot.get_channel(GEN).send('<@!267055271556284426> <@!219274149007196161> {}'.format(CaCStrix[1]))
            else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} CanadaComputers.com{colors.END}  Asus ROG Strix  {colors.RED} OUT OF STOCK{colors.END}')
        except Exception: 
            print(error)
            pass
        try: 
            MEMStrix = scrape.MEMStrixScrape()
            if MEMStrix[0]: await bot.get_channel(GEN).send('<@!267055271556284426> <@!219274149007196161> {}'.format(MEMStrix[1]))
            else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} MemoryExpress.com  {colors.END}  Asus ROG Strix  {colors.RED} OUT OF STOCK{colors.END}')
        except Exception: 
            print (error)
            pass
        try: 
            AMZStrix = scrape.AMZStrixScrape()
            if AMZStrix[0] and AMZStrix[2]: await bot.get_channel(GEN).send('<@!267055271556284426> <@!219274149007196161> {}'.format(AMZStrix[1]))
            elif (AMZStrix[2] != True) and AMZStrix[0]: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Amazon.ca          {colors.END}  Asus ROG Strix  {colors.YELLOW} OVERPRICED {AMZStrix[3]}{colors.END}')
            else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Amazon.ca          {colors.END}  Asus ROG Strix  {colors.RED} OUT OF STOCK{colors.END}')        
        except Exception: 
            print(error)
            pass
        try: 
            NEEStrix = scrape.NEEStrixScrape()
            if NEEStrix[0]: await bot.get_channel(GEN).send('<@!267055271556284426> <@!219274149007196161> {}'.format(NEEStrix[1]))
            else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Newegg.ca          {colors.END}  Asus ROG Strix  {colors.RED} OUT OF STOCK{colors.END}')
        except Exception: 
            print(error)
            pass
        try: 
            BBYStrix = scrape.BBYStrixScrape()
            if BBYStrix[0]: await bot.get_channel(GEN).send('<@!267055271556284426> <@!219274149007196161> {}'.format(BBYStrix[1]))
            else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} BestBuy.ca         {colors.END}  Asus ROG Strix  {colors.RED} OUT OF STOCK{colors.END}')
        except Exception: 
            print(error)
            pass
        try: 
            CaCTuf = scrape.CaCTufScrape()
            if CaCTuf[0]: await bot.get_channel(GEN).send('<@!267055271556284426> <@!219274149007196161> {}'.format(CaCTuf[1]))
            else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} CanadaComputers.com{colors.END}  Asus TUF Gaming {colors.RED} OUT OF STOCK{colors.END}')
        except Exception: 
            print(error)
            pass
        try: 
            MEMTuf = scrape.MEMTufScrape()
            if MEMTuf[0]: await bot.get_channel(GEN).send('<@!267055271556284426> <@!219274149007196161> {}'.format(MEMTuf[1]))
            else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} MemoryExpress.com  {colors.END}  Asus TUF Gaming {colors.RED} OUT OF STOCK{colors.END}')
        except Exception: 
            print(error)
            pass
        try: 
            NEETuf = scrape.NEETufScrape()
            if NEETuf[0]: await bot.get_channel(GEN).send('<@!267055271556284426> <@!219274149007196161> {}'.format(NEETuf[1]))
            else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Newegg.ca          {colors.END}  Asus TUF Gaming {colors.RED} OUT OF STOCK{colors.END}')
        except Exception: 
            print(error)
            pass
        try: 
            BBYTuf = scrape.BBYTufScrape()
            if BBYTuf[0]: await bot.get_channel(GEN).send('<@!267055271556284426> <@!219274149007196161> {}'.format(BBYTuf[1]))
            else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} BestBuy.ca         {colors.END}  Asus TUF Gaming {colors.RED} OUT OF STOCK{colors.END}')
        except Exception: 
            print(error)
            pass
        try: 
            AMZTuf = scrape.AMZTufScrape()
            if AMZTuf[0] and AMZTuf[2]: await bot.get_channel(GEN).send('<@!267055271556284426> <@!219274149007196161> {}'.format(AMZTuf[1]))
            elif (AMZTuf[2] != True) and AMZTuf[0]: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Amazon.ca          {colors.END}  Asus TUF Gaming {colors.YELLOW} OVERPRICED {AMZTuf[3]}{colors.END}')
            else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Amazon.ca          {colors.END}  Asus TUF Gaming {colors.RED} OUT OF STOCK{colors.END}')
        except Exception: 
            print(error)
            pass
        try: 
            NEER9X = scrape.NEER9XScrape()
            if NEER9X[0]: await bot.get_channel(GEN).send('<@!267055271556284426> <@!219274149007196161> {}'.format(NEER9X[1]))
            else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Newegg.ca          {colors.END}  Ryzen 9 5900x   {colors.RED} OUT OF STOCK{colors.END}')
        except Exception: 
            print(error)
            pass
        try: 
            CaCR9X = scrape.CaCR9XScrape()
            if CaCR9X[0]: await bot.get_channel(GEN).send('<@!267055271556284426> <@!219274149007196161> {}'.format(CaCR9X[1]))
            else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} CanadaComputers.com{colors.END}  Ryzen 9 5900x   {colors.RED} OUT OF STOCK{colors.END}')
        except Exception: 
            print(error)
            pass
        try: 
            AMZR9X = scrape.AMZR9XScrape()
            if AMZR9X[0] and AMZR9X[2]: await bot.get_channel(GEN).send('<@!267055271556284426> <@!219274149007196161> {}'.format(AMZR9X[1]))
            elif (AMZR9X[2] != True) and AMZR9X[0]: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Amazon.ca          {colors.END}  Ryzen 9 5900x   {colors.YELLOW} OVERPRICED {AMZR9X[3]}{colors.END}')
            else: print(time.strftime(f"{colors.GREY}[%H:%M:%S]{colors.END}",time.localtime()), f'{colors.CYAN} Amazon.ca          {colors.END}  Ryzen 9 5900x   {colors.RED} OUT OF STOCK{colors.END}')        
        except Exception: 
            print(error)
            pass
        await asyncio.sleep(150)