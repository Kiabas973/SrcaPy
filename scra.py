import requests, time, bs4
from turtle import title
from bs4 import BeautifulSoup #pip install bs4

"""
Name: formatWish()
Input 1: The media name you want : str
Return : The+media+name+you+want : str
"""
def formatWish(wish): # return str(my+wish+is+you)
	return wish.replace(' ', '+')

"""
Name: search()
Input 1: The+media+name+you+want : str
Input 2: Media type : str (by default is 'mangas' but you can use films, series, mangas or musiques)
Return : All Media found : dict{Name:Link,...}
"""
def search(searchName, mediaType='mangas'): #return dict{Name:Link,Name:Link,...}
	target = 'https://www.wawacity.blue/?search='+searchName+'&p='+mediaType
	_searchDict = {}
	r = requests.get(target)
	if r.ok: 
		soup = BeautifulSoup(r.text, "html.parser")
		for links in soup.find_all('div', {'class': 'wa-sub-block-title'}):
			for a in links.a:
				if (type(a) == bs4.element.NavigableString and a != ' '):
					name = a
				elif (type(a) == bs4.element.Tag and (' - VF'in a) or (' - VOSTFR'in a) or (' - VF HD'in a) or (' - VOSTFR HD'in a)):
					name = str(name) + str(a).replace('<i> ', ' ').replace('</i>','')
			for a in links.find_all('a'):
				nameLink = 'https://www.wawacity.blue/' + a.get('href')
			_searchDict[name] = nameLink
		return _searchDict

"""
Name: choose()
Input 1: All Media found : dict{Name:Link,...}
Return : Media you wish url : str
"""
def choose(searchDict): #return str(links)
	_nameList = []
	for x in searchDict:
		_nameList.append(x)
	for _name in _nameList:
		print(str(_nameList.index(_name)) + ': ' + str(_name))
	print('')
	return searchDict[_nameList[int(input('Make a wish: '))]]

"""
Name: choose()
Input 1: Media you wish url : str
Return : Download links of our wish : list
"""
def getLink(target, sleepingTime=1): #return list(links,links,...)
	_cleanLinks = []
	r = requests.get(target)
	if r.ok: 
		soup = BeautifulSoup(r.text, "html.parser")
		for _links in soup.find_all('a',{'class': 'link'}):
			if 'Télécharger' in str(_links) and 'Lien 1:' in str(_links):
				_cleanLinks.append(_links.get('href'))
	time.sleep(sleepingTime)
	return _cleanLinks

for x in getLink(choose(search(formatWish(input('What you wish: ')), input('What type is ? (films, series, mangas or musiques): ')))):
	print(x)