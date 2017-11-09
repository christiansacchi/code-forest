# -*- coding: utf-8 -*-

# decode_songLyric.py - 2017 

import io
import sys
from wordreference_request import WordReference_word_validation
from createDB import Wordb



class DecodeSL (object):

	def __init__ (self):
		self.wr = WordReference_word_validation ()
		self.db = Wordb ('decodeSL_prova_1')

		self.id_autore = 0
		self.id_raccolta = 0
		self.id_testo = 0
		self.id_parola = 0
		self.wordRef = {}

		self.db.create()
		self.db.end()

	def word_linearize (self, w):
		w = w.lower()
		for ch in [' ', '\n', '\"', '\'', ',', '(', ')', ':', ';', '.', '!', '?']:
			w = w.strip(ch)
		if '\'' in w:
			w = w.split('\'')[1]

		return w

	def word_validate (self):
		pass

	def decode (self, f):
		lyrc = io.open(f, mode='r', encoding='utf-8')

		for l in lyrc:
			_l = l.strip('\n')
			_l = _l.split('|')

			w = _l[0]

			if (w == '-=[a]=-'): # AUTORE
				w = _l[1].split(',')
				#print(*w)
				self.id_autore = self.db.add_autore(*w)
				continue

			if (w == '-=[r]=-'): # RACCOLTA
				w = _l[1].split(',')
				#print(*w)
				self.id_raccolta = self.db.add_raccolta(*w)
				continue

			if (w == '-=[t]=-'): # TESTO
				w = _l[1].split(',')
				#print(*w, self.id_autore, self.id_raccolta)
				try:
					self.id_testo = self.db.add_testo(*w, self.id_autore, self.id_raccolta)
				except Exception as e:
					print ("-=- sqlite3.IntegrityError -=-")
					print ("dsl.db.CONTs: {0}".format(dsl.db.CONTs))
					print ("id_testo: {0}".format(self.id_testo))
					dsl.db.c.execute('SELECT * FROM idcounter')
					print (*dsl.db.c.fetchall())


					dsl.db.c.execute('SELECT * FROM testo')
					print (dsl.db.c.fetchone())
					print (dsl.db.c.fetchone())

					raise e
				
				continue

			_l = _l[0].split()
			for w in _l:
				if (w == '-=[FIN]=-'):
					#print('-=[FIN]=-')
					break
				if (len(w) < 1):
					continue

				w = self.word_linearize(w)

				# def add_parola (self, word, lingua, iniziale, _len, isbad):
				if w in self.wordRef:
					self.wordRef[w][0] += 1
				else:
					self.wordRef[w] = [1, 'ita', w[0], len(w), False, None]

		#for w, inf in self.wordRef.items():
		#	print (w, inf)
			

	def decode_start (self):
		self.db.start()
	def decode_end (self):
		self.db.end()




dsl = DecodeSL ()
dsl.decode_start()

dsl.decode('caparezza_01.txt')

dsl.db.c.execute('SELECT * FROM autore')
print (dsl.db.c.fetchone())
dsl.db.c.execute('SELECT * FROM raccolta')
print (dsl.db.c.fetchone())
print (dsl.db.c.fetchone())
dsl.db.c.execute('SELECT * FROM testo')
print (dsl.db.c.fetchone())
print (dsl.db.c.fetchone())


dsl.db.c.execute("""UPDATE 'idcounter' SET 'cont'=100 WHERE 'id'=1;""")

dsl.db.c.execute('SELECT * FROM idcounter')
print (*dsl.db.c.fetchall())


dsl.decode_end()





"""
for l in lyrc:
	_l = l.split('|')

	for w in _l:
		
		if (w == '-=[FIN]=-'):
			continue

		#w = unicode(w)
		w = w.lower()
		for ch in [' ', '\n', '\"', '\'', ',', '(', ')', ':', ';', '.', '!', '?']:
			w = w.strip(ch)

		if '\'' in w:
			w = w.split('\'')[1]

		try:
			w = wr.isword(w)
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
"""
