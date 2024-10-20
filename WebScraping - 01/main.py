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

news_response = requests.get(url="https://news.ycombinator.com/news")

web_page = news_response.text

soup = BeautifulSoup(web_page, "html.parser")
print(soup.prettify())

all_news = soup.select(selector=".titleline a")
print(all_news)
# count = 0
#
# for news in all_news:
#     print(news.getText())
#     count +=1
#
# print(count)