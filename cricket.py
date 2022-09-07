import requests
from bs4 import BeautifulSoup
import urls

def writeCricketNews(site):
    url = urls.newsUrls[site]
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        if site == 'cricbuzz':
            cricbuzzNews(soup)

    else : 
        print(response.status_code)

def cricbuzzNews(soup):
    soup = soup.find('div', id='news-list')
    child = soup.findChildren('div', recursive=False)
    for ch in child:
        try:
            cb = ch.find('div','cb-nws-time').text
            title = ch.find('a')['title']
            link = ch.find('a')['href']
            print(cb)
            print(title)
            print(link)
        except:
            pass


writeCricketNews('cricbuzz')
