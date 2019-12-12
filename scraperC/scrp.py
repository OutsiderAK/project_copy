import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep

# response = get('https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=CDPROJEKT')

flag = True



def get_price(tag):
    global flag
    scrape_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    url = 'https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=' + str(tag)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    int_price = ''
    try:
        price = soup.find('div', {'class': 'profilLast'})
        ticker = soup.find('span', {'class': 'profilTicker'}).get_text()
        ticker = ticker.split('(')
        ticker = ticker[1].split(')')
        ticker = ticker[0]
        stock_time = datetime.strptime(str(soup.find('form').findNext('time').contents[0]), '%Y-%m-%d %H:%M:%S')\
            .strftime('%d/%m/%Y %H:%M:%S')
        fmt = '%H:%M:%S'
        time_delta = datetime.strptime(scrape_time[11:19], fmt) - datetime.strptime(stock_time[11:19], fmt)
        # print(time_delta)
        # this loop takes only the price, without the currency info or other crap
        for char in price.text:
            if char == ' ':
                break
            else:
                int_price = int_price + str(char)

        converted_price = int_price.replace(',', '.')
        converted_price = float(converted_price)
        # 4 decimal
        # swap this V ^ probably
        f = open('price', 'a')
        total_price = "{0:.4f}".format(round(converted_price, 4))
        f.write(f"{tag} --- {ticker} --- {total_price} --- {str(stock_time)} --- {str(scrape_time)} "
                f"--- Time Delta is {time_delta} \n")
        f.close()
        print('Added a line to file          ' + str(scrape_time))
        return True
    except AttributeError:
        print(f'Company {tag} not found')
        return False


tagger = str(input('Company name: '))


while flag:
    if not get_price(tagger):
        break
    else:
        sleep(1)

# print('Exiting program')
