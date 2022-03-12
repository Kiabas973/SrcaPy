from turtle import title
import requests, time
from bs4 import BeautifulSoup #pip install bs4

target = [
			'https://www.wawacity.blue/?p=manga&id=941-lord-el-melloi-ii-s-case-files-rail-zeppelin-grace-note-saison1',
			'https://www.wawacity.blue/?p=manga&id=902-twin-star-exorcists-saison1',
			'https://www.wawacity.blue/?p=manga&id=520-baki-2018-saison1',
			'https://www.wawacity.blue/?p=manga&id=1914-baki-2018-saison2',
			'https://www.wawacity.blue/?p=manga&id=2419-baki-2018-saison3',
			'https://www.wawacity.blue/?p=manga&id=1046-last-exile-saison1'
		]

def getLink(targetList, sleepingTime=1):
	_links = []
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

print(getLink(target))