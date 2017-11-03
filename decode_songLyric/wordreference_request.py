
import requests as req # pip install requests
import xml.etree.ElementTree as tree

import html5lib # pip install html5lib

class WordReference_word_validation (object):

	def __init__ (self):
		pass

	def find(self, tree, tag):
		for i in tree.iter():
			if (type(i.tag) is str):
				_tag = i.tag[len('{http://www.w3.org/1999/xhtml}'):]
				if _tag == tag:
						return i
	def find_byId(self, tree, tag, id):
		for i in tree.iter():
			if (type(i.tag) is str):
				_tag = i.tag[len('{http://www.w3.org/1999/xhtml}'):]
				if _tag == tag:
					if 'id' in i.attrib:
						if i.attrib['id'] == id:
							return i
	def find_byClass(self, tree, tag, clas):
		for i in tree.iter():
			if (type(i.tag) is str):
				_tag = i.tag[len('{http://www.w3.org/1999/xhtml}'):]
				if _tag == tag:
					if 'class' in i.attrib:
						if i.attrib['class'] == clas:
							return i

	def isword (self, word):

		_OUT = None

		t = None;
		site = 'http://www.wordreference.com/{0}'
		sitePos = '{0}/{1}'
		land = 'iten'
		textPag = "lol.html"
		page = req.get(site.format(sitePos.format(land, word)), allow_redirects=False, verify=False)

		f = open(textPag, 'wb')
		f.write(page.content)
		f.close()

		htmlf = open(textPag, 'rb')
		html = html5lib.parse(htmlf)

		title = self.find( self.find(html, 'head'), 'title')
		if title.text == 'Object moved':
			sitePos = self.find( self.find(html, 'body'), 'a').attrib['href']
			site = 'http://www.wordreference.com/{0}'.format(sitePos)
			page = req.get(site.format(sitePos.format(land, word)), allow_redirects=False, verify=False)

			f = open(textPag, 'wb')
			f.write(page.content)
			f.close()

			htmlf = open(textPag, 'rb')
			html = html5lib.parse(htmlf)

		body = self.find(html, 'body')
		table = self.find_byId(body, 'table', 'contenttable')
		elmt = self.find_byId(table, 'td', 'centercolumn')

		noEntryFound = self.find_byId(elmt, 'p', 'noEntryFound')
		if noEntryFound is not None:
			return word

		elmt = self.find_byId(elmt, 'div', 'articleWRD')
		if len(elmt) == 0:
			'''sitePos = '{0}/reverse/{1}'
			page = req.get(site.format(sitePos.format(land, word)), allow_redirects=False, verify=False)'''
			return word

		elmt = self.find_byClass(elmt, 'table', 'WRD')
		elmt = self.find_byClass(elmt, 'tr', 'even')
		elmt = self.find_byClass(elmt, 'td', 'FrWrd')
		elmt = self.find(elmt, 'strong')

		return elmt.text
