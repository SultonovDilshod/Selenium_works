from flask import Flask, jsonify

from bs4 import BeautifulSoup as bs
import requests as rq


def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency.upper()}&to={out_currency.upper()}&amount=1'
    content = rq.get(url=url).text
    soup = bs(content, 'html.parser')
    currency = soup.find("span", class_="ccOutputRslt").get_text()
    return float(currency[0:-4])


app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Current rate API</h1><p>Example URL: /api/v1/usd-aud</p>'


@app.route('/api/v1/<int_cur>-<out_cur>')
def index(int_cur, out_cur):
    cur_rate = get_currency(in_currency=int_cur, out_currency=out_cur)
    text = {'input currency': int_cur, 'output_currency': out_cur, 'rate': cur_rate}
    return jsonify(text)


def home():
    return '<h1>Current rate API</h1><p>Example URL: /api/v1/usd-aud</p>'


app.run(host='0.0.0.0')
