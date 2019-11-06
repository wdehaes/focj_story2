from bs4 import BeautifulSoup
import requests

url = 'https://www.mercari.com/search/?categoryIds=22&facets=2&itemConditions=2-3-4-5&length=30&minPrice=20000'

html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
print(soup.prettify())
