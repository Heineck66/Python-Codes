import requests
from bs4 import BeautifulSoup
import random

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

titles_tags = soup.find_all("picture")

titles = []
for alt in titles_tags:
    img_tag = alt.findChild("img")
    titles.append(img_tag.get("alt"))

titles = titles[:12:-1]

for pos, title in enumerate(titles, start=1):
    print(f"{pos}: {title}")


print(f"\n\n{random.choice(titles)}")
