# --- Scrape the website for information about apartments ---

import requests
from bs4 import BeautifulSoup
import re

URL = ("https://www.olx.pl/warszawa/q-%C5%82%C3%B3%C5%BCeczko-160/?search%5Bdist%5D=5&search%5Bfilter_float_price"
       "%3Afrom%5D=100&search%5Border%5D=filter_float_price%3Aasc")


class Data:
    def __init__(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
            "Accept-Language": "pl,en-US;q=0.7,en;q=0.3"
        }
        response = requests.get(URL, headers=header)
        self.beds = BeautifulSoup(response.text, "html.parser")
        # print(self.apartments.prettify())

    def find_data(self):
        # find addresses of the apartments
        infos = self.beds.select(selector='.css-z3gu2d')
        info = [i.text for i in infos[1:]]
        info = list(filter(None, info))
        # print(info)

        # find prices of the apartments
        prices = self.beds.select(selector='.css-u2ayx9 p')  # select by class name
        price = [p.text for p in prices]
        # print(price)

        # find urls of the apartments
        urls = self.beds.select(selector='.css-u2ayx9 a')  # select by class name
        url = ["www.olx.pl" + u.get("href") for u in urls]
        # print(url)

        print(len(info),len(price), len(url))
        return info, price, url
#
# Data().find_data()
