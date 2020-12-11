import urllib
import urllib.request
import bs4 as bs
from fake_useragent import UserAgent

URLCaCTuf = 'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=181415'
URLCaCStrix = 'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=181842'
URLMEMTuf = 'https://www.memoryexpress.com/Products/MX00114003'
URLMEMStrix = 'https://www.memoryexpress.com/Products/MX00114092'
URLAMZR9X = 'https://www.amazon.ca/DANIPEW-Sand-Man-Cotton-Performance-T-Shirt/dp/B08164VTWH/ref=pd_rhf_se_p_img_5?_encoding=UTF8&psc=1&refRID=FQGZ0RNY1ZJASGNH1TEQ'
URLAMZTuf = 'https://www.amazon.ca/Graphics-DisplayPort-Bearings-Military-Grade-Certification/dp/B08HH5WF97/ref=sr_1_1?dchild=1&keywords=Asus+3080&qid=1607196059&s=electronics&sr=1-1'
URLAMZStrix = 'https://www.amazon.ca/dp/B08J6F174Z?tag=nowinet-20&linkCode=ogi&th=1&psc=1'
URLBBYPS5 = 'https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185'
URLBBYStrix = 'https://www.bestbuy.ca/en-ca/product/asus-rog-strix-nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/14954116'
URLBBYTuf = 'https://www.bestbuy.ca/en-ca/product/asus-tuf-gaming-nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/14953248'
URLNEEStrix = 'https://www.newegg.ca/asus-geforce-rtx-3080-rog-strix-rtx3080-o10g-gaming/p/N82E16814126457?Description=Asus%203080&cm_re=Asus_3080-_-14-126-457-_-Product'
URLNEETuf = 'https://www.newegg.ca/asus-geforce-rtx-3080-tuf-rtx3080-o10g-gaming/p/N82E16814126452?Description=Asus%203080&cm_re=Asus_3080-_-14-126-452-_-Product'
URLNEER9X = 'https://www.newegg.ca/amd-ryzen-9-5900x/p/N82E16819113664?Description=5800x&cm_re=5800x-_-19-113-664-_-Product'
URLCaCR9X = 'https://www.canadacomputers.com/product_info.php?cPath=4_64_1969&item_id=183430'

class theScraper:

    def __init__(self):
        self

    def getAgent(self):
        BBY_Agent = UserAgent()
        headBBY = {'User-Agent':str(BBY_Agent.random)}
        return headBBY

    def AMZR9XScrape(self):
        Stock = [False, URLAMZR9X, False, 0]
        header = self.getAgent()
        R9X = urllib.request.urlopen(urllib.request.Request(Stock[1], data=None, headers=header)) 
        r9x = bs.BeautifulSoup(R9X, 'lxml')
        div = r9x.find('div', class_='a-button-stack')
        if ('Add to Cart' in div.text): 
            Stock[3] = float(r9x.find(id='priceblock_ourprice').get_text().replace('CDN$','').replace(',',''))
            if Stock[3] > 1000:
                Stock[0]=True
                Stock[2]=False
                return Stock
            else:
                Stock[0]=True
                Stock[2]=True
                return Stock
        else:
            Stock[0] = False
            Stock[2] = False
            return Stock
    
    def CaCR9XScrape(self):
        Stock = [False, URLCaCTuf]
        header = self.getAgent()
        R9X = urllib.request.urlopen(urllib.request.Request(Stock[1], data=None, headers=header))
        r9x = bs.BeautifulSoup(R9X, 'lxml')
        for divR9X in r9x.find_all('div', class_='pi-prod-availability'):
            pass
        if ('In-Store Back Order' in divR9X.text and 'Not Available Online' in divR9X.text) != True: Stock[0] = True
        else: 
            Stock[0] = False
        return Stock

    def CaCTufScrape(self):
        Stock = [False, URLCaCTuf]
        header = self.getAgent()
        Tuf = urllib.request.urlopen(urllib.request.Request(Stock[1], data=None, headers=header))
        tuf = bs.BeautifulSoup(Tuf, 'lxml')
        for divTuf in tuf.find_all('div', class_='pi-prod-availability'):
            pass
        if ('In-Store Back Order' in divTuf.text and 'Not Available Online' in divTuf.text) != True: Stock[0] = True
        else: 
            Stock[0] = False
        return Stock

    def CaCStrixScrape(self):
        Stock = [False, URLCaCStrix]
        header = self.getAgent()
        Strix = urllib.request.urlopen(urllib.request.Request(Stock[1], data=None, headers=header))
        strix = bs.BeautifulSoup(Strix, 'lxml')
        for divStrix in strix.find_all('div', class_='pi-prod-availability'):
            pass
        if ('In-Store Back Order' in divStrix.text and 'Not Available Online' in divStrix.text) != True: Stock[0] = True
        else: 
            Stock[0] = False
        return Stock

    def MEMTufScrape(self):
        Stock = [False, URLMEMTuf]
        header = self.getAgent()
        Tuf = urllib.request.urlopen(urllib.request.Request(Stock[1], data=None, headers=header))
        MEMTuf = bs.BeautifulSoup(Tuf, 'lxml')
        divTuf = MEMTuf.find('div', class_= 'c-capr-inventory__availability')
        if ('Out of Stock' in divTuf.text) != True: Stock[0] = True
        else: Stock[0] = False
        return Stock

    def MEMStrixScrape(self):
        Stock = [False, URLMEMStrix]
        header = self.getAgent()
        Strix = urllib.request.urlopen(urllib.request.Request(Stock[1], data=None, headers=header))
        MEMStrix = bs.BeautifulSoup(Strix, 'lxml')
        divStrix = MEMStrix.find('div', class_= 'c-capr-inventory__availability')
        if ('Out of Stock' in divStrix.text) != True: Stock[0] = True
        else: Stock[0] = False
        return Stock

    def AMZStrixScrape(self):
        Stock = [False, URLAMZStrix, False, 0]
        header = self.getAgent()
        Strix = urllib.request.urlopen(urllib.request.Request(Stock[1], data=None, headers=header)) 
        strix = bs.BeautifulSoup(Strix, 'lxml')
        div = strix.find('div', class_='a-button-stack')
        if ('Add to Cart' in div.text): 
            Stock[3] = float(strix.find(id='priceblock_ourprice').get_text().replace('CDN$','').replace(',',''))
            if Stock[3] > 1300:
                Stock[0]=True
                Stock[2]=False
                return Stock
            else:
                Stock[0]=True
                Stock[2]=True
                return Stock
        else:
            Stock[0] = False
            Stock[2] = False
            return Stock

    def AMZTufScrape(self):
        Stock = [False, URLAMZTuf, False, 0]
        header = self.getAgent()
        TUF = urllib.request.urlopen(urllib.request.Request(Stock[1], data=None, headers=header)) 
        tuf = bs.BeautifulSoup(TUF, 'lxml')
        div = tuf.find('div', class_='a-button-stack')
        if ('Add to Cart' in div.text): 
            Stock[3] = float(tuf.find(id='priceblock_ourprice').get_text().replace('CDN$','').replace(',',''))
            if Stock[3] > 1200:
                Stock[0]=True
                Stock[2]=False
                return Stock
            else:
                Stock[0]=True
                Stock[2]=True
                return Stock
        else:
            Stock[0] = False
            Stock[2] = False
            return Stock

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