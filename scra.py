import requests, time, bs4, sys
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
				if type(a) == bs4.element.NavigableString and a != ' ':
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
Name: getLink()
Input 1: Media you wish url : str
Return : Download links of our wish : list
"""
def getLink(target): #return list(links,links,...)
	_cleanLinks = []
	r = requests.get(target)
	if r.ok: 
		soup = BeautifulSoup(r.text, "html.parser")
		for _links in soup.find_all('a',{'class': 'link'}):
			if 'Télécharger' in str(_links) and 'Lien 1:' in str(_links):
				_cleanLinks.append(_links.get('href'))
	return _cleanLinks

"""
Name: SysArg()
Return : Parameter : list(mediaName, mediaType, targetSite)
"""
def sysArg():
	_arg = ['one', 'mangas', '', '.htx']
	for arg in range(len(sys.argv)-1):

		if sys.argv[arg+1] == '-n' or sys.argv[arg+1] == '--name':
			_arg[0] = sys.argv[arg+2]
		if sys.argv[arg+1] == '-m' or sys.argv[arg+1] == '--media':
			_arg[1] = sys.argv[arg+2]
		if sys.argv[arg+1] == '-s' or sys.argv[arg+1] == '--site':
			_arg[2] = sys.argv[arg+2]		
		if sys.argv[arg+1] == '-o' or sys.argv[arg+1] == '--output':
			_arg[3] = sys.argv[arg+2]
		if sys.argv[arg+1] == '-h' or sys.argv[arg+1] == '--help':
			print('------------------------------------------------------------------')
			print('Parameter    | Description                                        ')
			print('------------------------------------------------------------------')
			print('-n --name    | Media name                                         ')
			print('-m --media   | Media type (films, series, mangas or musiques)     ')
			print('-s --site    | Target site (wawacity)                             ')
			print('-o --output  | Output file name                                   ')
			print('-h --help    | Show this page                                     ')
			print('------------------------------------------------------------------')
			quit()
	return _arg

"""
Name: setup()
Return : Full Parameter for all fonction : list(mediaName, mediaType, targetSite)
"""
def setup():
	sysChoose = sysArg()
	if sysChoose[0] == '':
		sysChoose[0] = input('What you wish: ')
	return sysChoose

"""
Name: outputFile()
Input 1: Download links of our wish : list
Input 2: File name 
(if not output file) return : Download links of our wish : list
"""
def outputFile(links, fileName = '.htx'):
	if fileName == '.htx':
		return links
	else:
		with open(fileName, 'w') as f:
		    f.write(str(links))
		quit()





parameter = setup()
print(parameter[3])
for x in outputFile(getLink(choose(search(formatWish(parameter[0]), parameter[1]))),parameter[3]):
	print(x)