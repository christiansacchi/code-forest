
import requests as req # pip install requests
import xml.etree.ElementTree as tree

import html5lib # pip install html5lib

# -=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=- #

def find(tree, tag):
	for i in tree.iter():
		if (type(i.tag) is str):
			_tag = i.tag[len('{http://www.w3.org/1999/xhtml}'):]
			if _tag == tag:
					return i
def find_byId(tree, tag, id):
	for i in tree.iter():
		if (type(i.tag) is str):
			_tag = i.tag[len('{http://www.w3.org/1999/xhtml}'):]
			if _tag == tag:
				if 'id' in i.attrib:
					if i.attrib['id'] == id:
						return i
def find_byClass(tree, tag, clas):
	for i in tree.iter():
		if (type(i.tag) is str):
			_tag = i.tag[len('{http://www.w3.org/1999/xhtml}'):]
			if _tag == tag:
				if 'class' in i.attrib:
					if i.attrib['class'] == clas:
						return i

# -=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=- #
t = None;
site = 'http://www.wordreference.com/{0}'
sitePos = '{0}/{1}'
land = 'iten'
theWord = 'just'
page = req.get(site.format(sitePos.format(land, theWord)), allow_redirects=False, verify=False)

f = open('lol.html', 'wb')
f.write(page.content)
f.close()

# -=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=- #

htmlf = open('lol.html', 'rb')
html = html5lib.parse(htmlf)

title = find( find(html, 'head'), 'title')
if title.text == 'Object moved':
	sitePos = find( find(html, 'body'), 'a').attrib['href']
	site = 'http://www.wordreference.com/{0}'.format(sitePos)
	page = req.get(site.format(sitePos.format(land, theWord)), allow_redirects=False, verify=False)
	f = open('lol.html', 'wb')
	f.write(page.content)
	f.close()

	htmlf = open('lol.html', 'rb')
	html = html5lib.parse(htmlf)

body = find(html, 'body')
print (body)

table = find_byId(body, 'table', 'contenttable')
print (table)

elmt = find_byId(table, 'td', 'centercolumn')
print (elmt)

elmt = find_byId(elmt, 'div', 'articleWRD')
print (elmt)

elmt = find_byClass(elmt, 'table', 'WRD')
print (elmt)

elmt = find_byClass(elmt, 'tr', 'even')
print (elmt.attrib)
print (elmt)

elmt = find_byClass(elmt, 'td', 'FrWrd')
print (elmt.attrib)
elmt = find(elmt, 'strong')
print(elmt.text)
