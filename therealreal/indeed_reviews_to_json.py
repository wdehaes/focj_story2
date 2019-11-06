from bs4 import BeautifulSoup
import json
from pathlib import Path
import re

structured_reviews = []
filepath = "indeed_reviews.html"
with open(filepath) as fp:
  html = fp.read()
  soup = BeautifulSoup(html, "lxml")
  reviews = soup.find_all("div", class_="cmp-review-container")
  for review in reviews:
    rating = float(review.find("div", class_="cmp-ratingNumber").text)
    stars = review.find_all("td", class_="cmp-star-cell")
    work_life = stars[0].find("span")['style'][]
    comp = stars[1].find("span")['style'][]
    security = stars[2].find("span")['style'][]
    management = stars[3].find("span")['style'][]
    culture = stars[4].find("span")['style'][]
    title = review.find("div", class_="cmp-review-title").find("span").text
    jot_title = review.find("span", class_="cmp-reviewer").text
    date = review.find("span", class_="cmp-review-date-created").text
    text = review.find("span", class_="cmp-review-text").text.replace("\n")
    text = re.sub(' +', ' ', text)
    structured_review = {
        "rating": rating,
        "work_life": work_life,
        "comp": comp,
        "security": security,
        "management": management,
        "culture": culture,
        "title": title,
        "jot_title": jot_title,
        "date": date,
        "text": text
    }
    structured_reviews.append(structured_review)

with open('indeed_reviews.json', 'w') as fp:
    json.dump(structured_reviews, fp)


