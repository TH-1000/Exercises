#This program reads news headlines from an RSS newsfeed source.
#BeautifulSoup Library is used here

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

url = input('Enter rss news-feed source: ')
client = urlopen(url)
reader = client.read()
client.close()

soup_pages = soup(reader,'xml')
news_list = soup_pages.findAll('item')

for news in news_list:
    print(news.title.text)
    print(news.pubDate.text)
    print(news.link.text)
