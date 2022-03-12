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

links = []

for url in target:
    r = requests.get(url)
    if r.ok: 
        soup = BeautifulSoup(r.text, "html.parser")
        print(soup.title)
        for links in soup.find_all('a',{'class': 'link'}):
            if 'Télécharger' in str(links) and 'Lien 1:' in str(links):
                print(links.get('href'))

    time.sleep(1)
    print('\n')