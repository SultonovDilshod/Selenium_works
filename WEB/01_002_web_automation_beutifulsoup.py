from bs4 import BeautifulSoup as bs
import requests as rq


def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency.upper()}&to={out_currency.upper()}&amount=1'
    content = rq.get(url=url).text
    soup = bs(content, 'html.parser')
    currency = soup.find("span", class_="ccOutputRslt").get_text()
    return float(currency[0:-4])


print(get_currency('usd', 'aud'))
