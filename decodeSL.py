# -*- coding: utf-8 -*-

# decode_songLyric.py - 2017

import io

lyrc = io.open('caparezza_01.txt', mode='r', encoding='utf-8')

wordRef = {}

for l in lyrc:
	_l = l.split()

	for w in _l:
		
		if (w == '---'):
			continue

		w = unicode(w)
		w = w.lower()
		for ch in [' ', '\n', '\"', '\'', ',', '(', ')', ':', ';', '.', '!', '?']:
			w = w.strip(ch)

		if '\'' in w:
			w = w.split('\'')[1]

		if w in wordRef:
			wordRef[w] += 1
		else:
			wordRef[w] = 1

for w, c in wordRef.items():
	w = unicode(w)
	print(u"{0}: {1}".format(w, c))
