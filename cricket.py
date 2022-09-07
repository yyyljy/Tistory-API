import requests
from bs4 import BeautifulSoup
import urls
import tistory

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
            ti = tistory.Tistory()
            ti.writeBlog('peta',title,link,0,1040605,cb,0)
            if ti.chkArticleList('peta',link):
                pass
            else:
                ti.writeBlog('peta',title,link,0,1040605,cb,0)
        except:
            pass


# writeCricketNews('cricbuzz')
