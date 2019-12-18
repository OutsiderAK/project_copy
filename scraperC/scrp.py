import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


class WebScraperC:
    # tag --------- ticker  ---   total_price ------ stock_time ------- scrape_time ------- time_delta

    def __init__(self, tag):
        self.body = self.get_body_page(tag)[0]
        if self.get_body_page(tag)[1] == 1:
            raise Exception
        self.name = tag
        self.ticker = self.get_ticker()
        self.price = self.get_price()
        self.real_date = self.get_real_date()
        self.real_time = self.get_real_time()
        self.scrape_date = self.get_scrape_date()
        self.scrape_time = self.get_scrape_time()
        self.delta_time = self.get_time_delta()

    @staticmethod
    def get_body_page(tag):
        url = 'https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=' + str(tag)
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}
        page = requests.get(url, headers=headers)
        error = 0
        if page.status_code == 404:
            error = 1
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup, error

    def get_ticker(self):
        ticker = self.body.find('span', {'class': 'profilTicker'}).get_text()
        ticker = ticker.split('(')
        ticker = ticker[1].split(')')
        ticker = ticker[0]
        return ticker

    def get_price(self):
        int_price = ''
        price = self.body.find('div', {'class': 'profilLast'})
        for char in price.text:
            if char == ' ':
                break
            else:
                int_price = int_price + str(char)
        converted_price = int_price.replace(',', '.')
        converted_price = float(converted_price)
        total_price = "{0:.4f}".format(round(converted_price, 4))
        return total_price

    def get_real_date(self):
        return datetime.strptime(str(self.body.find('form').findNext('time').contents[0]),
                                 '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y')

    def get_real_time(self):
        return datetime.strptime(str(self.body.find('form').findNext('time').contents[0]),
                                 '%Y-%m-%d %H:%M:%S').strftime('%H:%M')

    @staticmethod
    def get_scrape_date():
        return datetime.now().strftime("%d/%m/%Y")

    @staticmethod
    def get_scrape_time():
        return datetime.now().strftime("%H:%M")

    def get_time_delta(self):
        fmt = '%H:%M'
        delta = datetime.strptime(self.scrape_time[0:5], fmt) - datetime.strptime(self.real_time[0:5], fmt)
        if delta.days < 0:
            delta = timedelta(days=0, seconds=delta.seconds, microseconds=delta.microseconds)
        return delta

    def return_tuple(self):
        return self.name, self.ticker, self.price, self.real_date, self.real_time, self.scrape_date, self.scrape_time, \
               str(self.delta_time)

"""
while True:
    try:
        companyName = str(input())
        stock = WebScraperC(companyName)
        print(stock.return_tuple())
    except Exception as e:
        print('No company found')
"""