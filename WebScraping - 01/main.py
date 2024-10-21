# from bs4 import BeautifulSoup
# # import lxml
#
#
# with open(file="website.html") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup)
# # print(soup.prettify())
#
# # Searching for lists of specific information
#
# all_tags = soup.find_all(name="a")
#
# for tag in all_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading.getText())
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# # Selecting items
# # company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
from bs4 import BeautifulSoup
import requests

news_response = requests.get(url="https://news.ycombinator.com")

web_page = news_response.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup.prettify())

all_news = soup.select(selector=".titleline > a")

article_texts = []
article_links = []
for news in all_news:
    article_texts.append(news.getText())
    article_links.append(news.get("href"))

all_votes = soup.find_all(name = "span", class_="score")
article_votes = []
for news in all_votes:
    article_votes.append(int(news.getText().split()[0]))

# print(article_texts)
# print(article_links)
# print(article_votes)

most_votes = max(article_votes)

articles_dicts = [{"text": text, "link": link, "votes": votes} for text, link, votes in zip(article_texts, article_links, article_votes)]

for article in articles_dicts:
    if most_votes == article["votes"]:
        print(f"The article with the most votes: \n {article}")
