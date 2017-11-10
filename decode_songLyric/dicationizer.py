# -*- coding: utf-8 -*-

import io

class dicationizer (object):

	def __init__ (self):
		self.n = None



	def word2dictpage (self, w):
		n = 'dizion.txt'

		for ch in (' ', '\n'):
			w = w.strip(ch)

		# GENERAZIONE NOME SEZIONE DIZIONARIO DA PAROLA...
		w_len = len(w)

		#if w_len != 6:
		#	continue

		if w_len <= 4:
			n = "123.txt"

		elif w_len == 5:
			n = "5_gen.txt"

		elif w_len == 6:
			n = "6_gen.txt"

		elif w[0] in ('j', 'k', 'y', 'w', 'x', 'z'):
			n = "jkywxz.txt"

		#elif w_len >= 11 and w[0] in ('a', 'c', 'd', 'i', 'p', 'r', 's', 't'):
		#	n = "11over_acdiprst.txt"

		elif 9 <= w_len <= 15 and w[0] in ('s', 'r', 'a', 'i', 'd', 'c', 'p', 't'):
			n = "{0}_{1}.txt".format(w[0], w_len)

		elif w_len == 12 and w[0] not in ('s', 'r', 'a', 'i', 'd', 'c', 'p', 't'):
			n = "notCommon_12.txt"

		elif w_len == 13 and w[0] not in ('s', 'r', 'a', 'i', 'd', 'c', 'p', 't'):
			n = "notCommon_13.txt"

		elif 14 <= w_len <= 15 and w[0] not in ('s', 'r', 'a', 'i', 'd', 'c', 'p', 't'):
			n = "notCommon_14to15.txt"

		elif w_len >= 16:
			n = "{0}_16over.txt".format(w[0])

		else:
			n = "{0}_{1}.txt".format(w[0], w_len)

		self.n = n
		return n



	def dicationizer (self, _f):
		dic = io.open(_f, mode='r', encoding='utf-8')

		fls = {}
		f = None
		n = None

		for w in dic:
			n = self.word2dictpage(w)

			if n in fls:
				f = fls[n]
			else:
				fls[n] = io.open(n, mode='a', encoding='utf-8')
				f = fls[n]

			f.write("{0}\n".format(w))

		for k, d in fls.items():
			d.close()
		dic.close()


#dicationizer('___280-000___.txt')
#dicationizer('___10-000_eng___.txt')