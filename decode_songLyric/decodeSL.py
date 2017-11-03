# -*- coding: utf-8 -*-

# decode_songLyric.py - 2017 

import io
import sys
from wordreference_request import WordReference_word_validation


lyrc = io.open('caparezza_01.txt', mode='r', encoding='utf-8')
wrdref_wrd_val = WordReference_word_validation ()


wordRef = {}

for l in lyrc:
	_l = l.split()

	for w in _l:
		
		if (w == '---'):
			continue

		#w = unicode(w)
		w = w.lower()
		for ch in [' ', '\n', '\"', '\'', ',', '(', ')', ':', ';', '.', '!', '?']:
			w = w.strip(ch)

		if '\'' in w:
			w = w.split('\'')[1]

		try:
			w = wrdref_wrd_val.isword(w)
		except:
			print("FALLITO! Fallito sulla parola: {0}".format(w))
			sys.exit("FALLITO! Fallito sulla parola: {0}".format(w))

		if w in wordRef:
			wordRef[w] += 1
		else:
			wordRef[w] = 1

# c.execute('''INSERT INTO 'autore' ('nome', 'cognome', 'anno') VALUES ('Caparezza', NULL, );''')

for w, c in wordRef.items():
	#w = unicode(w)
	print(u"{0}: {1}".format(w, c))

