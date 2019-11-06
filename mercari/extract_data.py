from bs4 import BeautifulSoup
import json
from pathlib import Path

p = Path('html')
products = []
for x in p.iterdir():
  if x.is_file():
      with x.open() as fp:
        html = fp.read()
        soup = BeautifulSoup(html, "lxml")
        try:
          product_name = soup.find("h1").text
          product_description = soup.find(
              "p", class_="ItemDescription__DescriptionText-sc-1w7qr5f-0").text
          product_brand = soup.find("a", attrs={'class': lambda e: e.startswith(
              'Spec__BrandLink') if e else False}).text
          product_price = soup.find(
              "p", class_="ItemInfo__ProductPrice-ijvfho-0").text
          product_seller = soup.find(
              "p", class_="ProfileBar__Name-sc-2z5a96-0").text
          seller_stats = soup.find_all("span", attrs={'class': lambda e: e.startswith(
              'ProfileBar__Bold') if e else False})
          seller_listed = seller_stats[0].text
          seller_sold = seller_stats[1].text
          product = {'name': product_name,
                    'brand': product_brand, 'price': product_price, 'seller': product_seller, 'seller_listed': seller_listed, 'seller_sold': seller_sold}
          products.append(product)
        except:
          print(product_name + " " + str(x))


with open('mercari_seller.json', 'w') as fp:
    json.dump(products, fp)
