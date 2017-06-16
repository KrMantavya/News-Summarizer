import urllib2
from bs4 import BeautifulSoup

def get_only_text_washingtonpost_url(url):
    page=urllib2.urlopen(url).read().decode('utf8')
    soup=BeautifulSoup(page)
    text=' '.join(map(lambda p: p.text, soup.find_all('article')))
    soup2=BeautifulSoup(text)
    text=' '.join(map(lambda p:p.text, soup2.find_all('p')))
    return soup.title.text,text
