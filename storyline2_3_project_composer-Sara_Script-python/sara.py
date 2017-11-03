# -*- coding: utf-8 -*-

from tool import Tool
from Gid import Gid
from SLPrefabs import SLPrefabs
from WbtStoryLine import WbtStoryLine
from WbtEvo import WbtEvo

class Sara (object):
	def __init__ (self, nomePorgetto, nomeUnita, numUnita, stile='paper', f="exemple.sara"):
		# Tools
		self.t = Tool()
		# Attrib ENV
		self.env = "C:\\christian_lavoro\\wbt\\__development__\\__SARA__\\"
		self.projcFol = self.env + "progetti\\"
		self.asset = self.env + "asset\\"
		self.base = self.asset + "base\\"
		# Attrib
		self.wbt = None
		self.projc = None

		# Body -=-=-=-
		self.projc = self.creaProjc(nomePorgetto)
		self.wbt = WbtEvo(self.projc, stile)
		self.wbt.initVar(nomePorgetto, numUnita, nomeUnita)
		#self.wbt.initBase1()

		# Footer
		self.wbt.close()

	def creaProjc (self, nomeWBT):
		# CREATE FOLDER - RANAME LOOP
		c = 2
		nome = "{0}".format(nomeWBT)
		while (True):
			try:
				self.t.ctrlC_ctrlV(self.base, self.projcFol+nome)
			except WindowsError as winErr:
				nome = "{1} ({0})".format(c, nomeWBT)
				c += 1
				continue
			else:
				self.t.printINFO("Creato progetto {0}".format(nome))
				break
		return self.projcFol+nome

	def proJGID_ID (self):
		projc = self.creaProjc("proJGID_ID")
		GID_ID = WbtEvo(projc, 'paper')
		GID_ID.initVar("proJGID_ID", "1", "proJGID_ID___proJGID_ID")

		GID_ID.wbt.selectMasterSlide("paper") # Selezione layout

		scena = GID_ID.wbt.addScene("MAIN")

		print "-="*50

		listatooo = []
		for n in range(10):
			faf = GID_ID.wbt.g.make(n, 1, 333, 7777, mid2=10)
			listatooo.append( faf[0] )
			GID_ID.mainLst.append(GID_ID.wbt.addSlide(scena, "FOOTER", faf=faf))
		for n in range(11, 20):
			faf = GID_ID.wbt.g.make(n, 1, 999, 7777, mid2=20)
			listatooo.append( faf[0] )
			GID_ID.mainLst.append(GID_ID.wbt.addSlide(scena, "MID 3", faf=faf))
		for n in range(21, 30):
			faf = GID_ID.wbt.g.make(n, 2, 1022, 7777, mid2=30)
			listatooo.append( faf[0] )
			GID_ID.mainLst.append(GID_ID.wbt.addSlide(scena, "MID 1", faf=faf))
		for n in range(31, 40):
			faf = GID_ID.wbt.g.make(n, 0, 1044, 7777, mid2=40)
			listatooo.append( faf[0] )
			GID_ID.mainLst.append(GID_ID.wbt.addSlide(scena, "HEAD", faf=faf))

		for g in listatooo:
			print g

		print "-="*50

		GID_ID.close()
		return GID_ID

import datetime
print datetime.datetime.now()

s = Sara('Polizza Protezione Immobile', 'Contratto di Assicurazione Incendio dei Fabbricati', '1')
s.wbt.initBase2()

s.wbt.addSlide('Cover')
s.wbt.addSlide('Copertina')

sld = s.wbt.addSlide('introduzione')
s.wbt.insertVideo('meidainfo/uniqua/esperto_01.mov', sld)
s.wbt.insertVideo('meidainfo/uniqua/friend_01.mov', sld, 'sx')

sld = s.wbt.addSlide('Finalita del prodotto')
s.wbt.insertVideo('meidainfo/uniqua/esperto_02.mov', sld)
s.wbt.insertVideo('meidainfo/uniqua/friend_02.mov', sld, 'sx')

sld = s.wbt.addSlide('Fabbricati')
s.wbt.insertVideo('meidainfo/uniqua/esperto_03.mov', sld)
s.wbt.insertVideo('meidainfo/uniqua/friend_03.mov', sld, 'sx')

s.wbt.addSlide('JOBSTOP')

sld = s.wbt.addSlide('Le coperture offerte')
s.wbt.insertVideo('meidainfo/uniqua/esperto_04.mov', sld)
s.wbt.insertVideo('meidainfo/uniqua/friend_04.mov', sld, 'sx')
s.wbt.insertVideo('meidainfo/uniqua/esperto_04PP.mov', sld, 'sx')

sld = s.wbt.addSlide('La franchigia')
s.wbt.insertVideo('meidainfo/uniqua/esperto_05.mov', sld)
s.wbt.insertVideo('meidainfo/uniqua/friend_05.mov', sld, 'sx')

s.wbt.addSlide('JOBSTOP')

sld = s.wbt.addSlide('Spese di demolizione e sgombero')
s.wbt.insertVideo('meidainfo/uniqua/esperto_06.mov', sld)
#s.wbt.insertVideo('meidainfo/uniqua/friend_06.mov', sld, 'sx')

sld = s.wbt.addSlide('Garanzia Incendio')
s.wbt.insertVideo('meidainfo/uniqua/esperto_07.mov', sld)
#s.wbt.insertVideo('meidainfo/uniqua/friend_07.mov', sld, 'sx')

s.wbt.addSlide('JOBSTOP')

sld = s.wbt.addSlide('Valore assicurato')
s.wbt.insertVideo('meidainfo/uniqua/esperto_08.mov', sld)
s.wbt.insertVideo('meidainfo/uniqua/friend_08.mov', sld, 'sx')
s.wbt.insertVideo('meidainfo/uniqua/esperto_08_finale.mov', sld)
s.wbt.insertVideo('meidainfo/uniqua/friend_08_finale.mov', sld, 'sx')

sld = s.wbt.addSlide('Anticipo indennizzi')
s.wbt.insertVideo('meidainfo/uniqua/esperto_09.mov', sld)
s.wbt.insertVideo('meidainfo/uniqua/friend_09.mov', sld, 'sx')

sld = s.wbt.addSlide('Metodo di pagamento')
s.wbt.insertVideo('meidainfo/uniqua/esperto_10.mov', sld)
s.wbt.insertVideo('meidainfo/uniqua/friend_10.mov', sld, 'sx')

sld = s.wbt.addSlide('Mutamenti del rischio')
s.wbt.insertVideo('meidainfo/uniqua/esperto_11.mov', sld)
s.wbt.insertVideo('meidainfo/uniqua/friend_11.mov', sld, 'sx')

sld = s.wbt.addSlide('Il recesso')
s.wbt.insertVideo('meidainfo/uniqua/esperto_12.mov', sld)
s.wbt.insertVideo('meidainfo/uniqua/friend_12.mov', sld, 'sx')
s.wbt.insertVideo('meidainfo/uniqua/esperto_12_finale.mov', sld)
s.wbt.insertVideo('meidainfo/uniqua/friend_12_finale.mov', sld, 'sx')
s.wbt.insertVideo('meidainfo/uniqua/friend_12PP.mov', sld, 'sx')


s.wbt.addSlide('JOBSTOP - TEST FINALE')

s.wbt.addSlide('FIN')

s.wbt.linkSlide()

s.wbt.close()

print datetime.datetime.now()

t = Tool()
t.pressToContinue()