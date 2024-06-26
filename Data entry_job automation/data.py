# --- Scrape the website for information about bikes ---

import requests
from bs4 import BeautifulSoup
import re

URL = ("https://www.olx.pl/warszawa/q-rowerek-dzieci%C4%99cy/?search%5Border%5D=filter_float_price:asc&search"
       "%5Bfilter_float_price:from%5D=50")


class Data:
    def __init__(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/123.0.0.0 Safari/537.36",
            "Accept-Language": "pl-PL,pl;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"
        }
        response = requests.get(URL, headers=header)
        self.beds = BeautifulSoup(response.text, "html.parser")
        # print(self.apartments.prettify())

    def find_data(self):
        # Find info about the bikes
        infos = self.beds.select(selector='.css-z3gu2d h6')
        info = [i.text for i in infos]
        info = list(filter(None, info))

        # find prices of the bikes
        prices = self.beds.select(selector='.css-u2ayx9 p')
        price = [p.text for p in prices]

        # find urls of the bikes
        urls = self.beds.select(selector='.css-u2ayx9 a')
        url = ["www.olx.pl" + u.get("href") for u in urls]

        return info, price, url
