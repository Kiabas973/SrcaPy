from turtle import title
import requests, time, bs4
from bs4 import BeautifulSoup #pip install bs4


def search(searchName, mediaType='mangas'): #return dict{Name:Link,Name:Link,...}
	target = 'https://www.wawacity.blue/?search='+searchName+'&p='+mediaType
	_searchDict = {}
	r = requests.get(target)
	if r.ok: 
		soup = BeautifulSoup(r.text, "html.parser")
		for links in soup.find_all('div', {'class': 'wa-sub-block-title'}):
			for a in links.a:
				if type(a) == bs4.element.NavigableString and a != ' ':
					name = a
			for a in links.find_all('a'):
				nameLink = 'https://www.wawacity.blue/' + a.get('href')
			_searchDict[name] = nameLink
		return _searchDict


def getLink(targetList, sleepingTime=1): #return list(links,links,...)
	_cleanLinks = []
	for url in targetList:
	    r = requests.get(url)
	    if r.ok: 
	        soup = BeautifulSoup(r.text, "html.parser")
	        for _links in soup.find_all('a',{'class': 'link'}):
	            if 'Télécharger' in str(_links) and 'Lien 1:' in str(_links):
	                _cleanLinks.append(_links.get('href'))
	        print(str(soup.title) + ' -----> Finish')
	time.sleep(sleepingTime)
	return _cleanLinks

print(search('https://www.wawacity.blue/?search=one&p=mangas'))