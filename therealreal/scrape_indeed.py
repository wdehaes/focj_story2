import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/cmp/The-Realreal/reviews?fcountry=ALL'

html = requests.get(url).text

with open('indeed_reviews.html', 'w') as f:
    f.write(html)
