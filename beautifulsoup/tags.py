import requests
from bs4 import BeautifulSoup

with open("beautifulsoup/sample.html","r") as f:
    html_doc=f.read()


soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())


# print(soup.title.name)

# print(soup.find_all('a'))

# print(soup.head)

# print(soup.select("div.italic"))


# print(soup.select("span.italic"))


# print(soup.find_all(class_="italic"))


