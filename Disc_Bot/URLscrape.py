import urllib
import urllib.request
import bs4 as bs
from fake_useragent import UserAgent


URLBBYStrix = 'https://www.bestbuy.ca/en-ca/product/asus-rog-strix-nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/14954116'
URLBBYTuf = 'https://www.bestbuy.ca/en-ca/product/asus-tuf-gaming-nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/14953248'
URLNEEStrix = 'https://www.newegg.ca/asus-geforce-rtx-3080-rog-strix-rtx3080-o10g-gaming/p/N82E16814126457?Description=Asus%203080&cm_re=Asus_3080-_-14-126-457-_-Product'
URLNEETuf = 'https://www.newegg.ca/asus-geforce-rtx-3080-tuf-rtx3080-o10g-gaming/p/N82E16814126452?Description=Asus%203080&cm_re=Asus_3080-_-14-126-452-_-Product'
URLNEER9X = 'https://www.newegg.ca/amd-ryzen-9-5900x/p/N82E16819113664?Description=5800x&cm_re=5800x-_-19-113-664-_-Product'
#URLBBYStrix = 'https://www.bestbuy.ca/en-ca/product/msi-nvidia-geforce-gtx-1660-ti-6gb-gddr6-video-card/13785580'

class theScraper:

    def __init__(self):
        self

    def getAgent(self):
        BBY_Agent = UserAgent()
        headBBY = {'User-Agent':str(BBY_Agent.random)}
        return headBBY

    def BBYStrixScrape(self):
        Stock = [False, URLBBYStrix]
        header = self.getAgent()
        Strix = urllib.request.urlopen(urllib.request.Request(Stock[1], data=None, headers=header))
        BBYStrix = bs.BeautifulSoup(Strix, 'lxml')
        divStrix = BBYStrix.find('div', class_= 'availabilityMessageProduct_29UPa')
        if ('Sold out' in divStrix.text) != True: Stock[0] = True
        else: Stock[0] = False
        return Stock

    def BBYTufScrape(self):
        Stock = [False, URLBBYTuf]
        header = self.getAgent()
        TUF = urllib.request.urlopen(urllib.request.Request(Stock[1], data=None, headers=header))
        BBYTuf = bs.BeautifulSoup(TUF, 'lxml')
        divTuf = BBYTuf.find('div', class_= 'availabilityMessageProduct_29UPa')
        if ('Sold out' in divTuf.text) != True: Stock[0] = True
        else: Stock[0] = False
        return Stock

    def NEEStrixScrape(self):
        Stock = [False, URLNEEStrix]
        header = self.getAgent()
        Strix = urllib.request.urlopen(urllib.request.Request(Stock[1], data=None, headers=header))
        NEEStrix = bs.BeautifulSoup(Strix, 'lxml')
        divStrix = NEEStrix.find('div', class_='nav-col')
        if ('Sold Out' in divStrix.text) != True: Stock[0] = True
        else: Stock[0] = False
        return Stock

    def NEETufScrape(self):
        Stock = [False, URLNEEStrix]
        header = self.getAgent()
        Tuf = urllib.request.urlopen(urllib.request.Request(Stock[1], data=None, headers=header))
        NEETuf = bs.BeautifulSoup(Tuf, 'lxml')
        divTuf = NEETuf.find('div', class_='nav-col')
        if ('Sold Out' in divTuf.text) != True: Stock[0] = True
        else: Stock[0] = False
        return Stock

    def NEER9XScrape(self):
        Stock = [False, URLNEER9X]
        header = self.getAgent()
        R9X = urllib.request.urlopen(urllib.request.Request(Stock[1], data=None, headers=header))
        NEER9X = bs.BeautifulSoup(R9X, 'lxml')
        divR9X = NEER9X.find('div', class_='nav-col')
        if ('Sold Out' in divR9X.text) != True: Stock[0] = True
        else: Stock[0] = False
        return Stock