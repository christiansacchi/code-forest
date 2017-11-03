# -*- coding: utf-8 -*-

from tool import Tool
from Gid import Gid

from WbtStoryLine import WbtStoryLine

class WbtEvo (object):
	def __init__ (self, projc, grafica):
		# Tools
		self.t = Tool()
		self.wbt = WbtStoryLine(projc)

		# Attrib
		self.grafica = grafica
		self.main = None
		self.mainLst = []
		self.indice = None

		self.pageNumberGid = None
		self.titoloSlideGid = None
		self.titCounter = 1;

	def initVar (self, titolo, numUd, titoloUd):
		# SET BASE VARs
		try:
			self.wbt.setVariable("continue", False)
			self.wbt.setVariable("debug", True)
			self.wbt.setVariable("item00P", 0)
			self.wbt.setVariable("item00T", titolo)
			self.wbt.setVariable("maxPage", 1)
			self.wbt.setVariable("maxQuiz", 0)
			self.wbt.setVariable("numPages", 99999)
			self.wbt.setVariable("num_unita", numUd)
			self.wbt.setVariable("onPageNext", 0)
			self.wbt.setVariable("onPagePrev", 0)
			self.pageNumberGid = self.wbt.setVariable("pageNumber", 0); self.pageNumberGid = self.pageNumberGid[3]
			self.wbt.setVariable("titolo_corso", titolo)
			self.titoloSlideGid = self.wbt.setVariable("titolo_slide", "titolo slide"); self.titoloSlideGid = self.titoloSlideGid[3]
			self.wbt.setVariable("titolo_unita", titoloUd)
			self.wbt.setVariable("versione_corso", "1.0.0")
			self.wbt.setVariable("javascript_enabled", False)
		except WbtE_varE_badName as badName:
			self.t.printERR(badName) # è partito il trigger, ma non lo vede e quindi parte un secondo errore. SISTEMARE!!!!!
		except WbtE_varE_wrongVarType as varType:
			self.t.printERR(varType)

	def initBase1 (self):
		self.wbt.selectMasterSlide(self.grafica)

		# CREATING MAIN SCENEs OF PROJECT
		self.main = self.wbt.addScene("MAIN")
		self.indice = self.wbt.addScene("INDICE")
		assetSCN = self.wbt.addScene("ASSETs")

		self.mainLst.append(self.wbt.addSlide(self.main, "Cover", layout='cover'))
		self.mainLst.append(self.wbt.addSlide(self.main, "Copertina", layout='copertina'))
		self.mainLst.append(self.wbt.addSlide(self.main, "Slide1"))
		self.mainLst.append(self.wbt.addSlide(self.main, "Slide2"))
		self.mainLst.append(self.wbt.addSlide(self.main, "Slide3"))
		self.mainLst.append(self.wbt.addSlide(self.main, "Slide4"))
		self.mainLst.append(self.wbt.addSlide(self.main, "FIN", layout='fin')) # , layout='fin'
		# STARTING LINK SLIDE
		i = 0
		while i < (len(self.mainLst)-1):
			self.linkSlides(self.mainLst[i], self.mainLst[i+1])
			self.setPageNumber(self.mainLst[i], i+1)
			i += 1
		self.setPageNumber(self.mainLst[i], i+1)
		# END LINK SLIDE

		self.addVideo("meidainfo/conduzione_01.mov", self.mainLst[2])
		self.addVideo("meidainfo/conduzione_01.mov", self.mainLst[3])
		self.addVideo("meidainfo/conduzione_01.mov", self.mainLst[4])
		self.addVideo("meidainfo/conduzione_01.mov", self.mainLst[5])

		self.wbt.addSlide(self.indice, "Indice")
		self.wbt.addSlide(self.indice, "Help")

		self.wbt.addSlide(assetSCN, "tmp1")
		self.wbt.addSlide(assetSCN, "tmp2")
		self.wbt.addSlide(assetSCN, "tmp3")

	def initBase2 (self):
		self.wbt.selectMasterSlide(self.grafica)

		self.main = self.wbt.addScene("MAIN")
		self.indice = self.wbt.addScene("INDICE")
		assetSCN = self.wbt.addScene("ASSETs")

		self.indicePage = self.wbt.addSlide('indice', 'indice')
		self.wbt.addSlide('help', 'indice')

	def linkSlide (self):
		# STARTING LINK SLIDE
		i = 0
		while i < (len(self.mainLst)-1):
			self.linkSlides(self.mainLst[i], self.mainLst[i+1])
			self.setPageNumber(self.mainLst[i], i+1)
			i += 1
		self.setPageNumber(self.mainLst[i], i+1)
		# END LINK SLIDE

	def close (self):
		self.wbt.close()

	def addTit (self, val, offset=2):
		var = None
		item = 'item{0:02d}'.format(self.titCounter)

		try:
			tit1 = self.wbt.setVariable(item+"P", self.titCounter+offset)
			tit2 = self.wbt.setVariable(item+"T", val)

		except WbtE_varE_badName as badName:
			self.t.printERR(badName)
		except WbtE_varE_wrongVarType as varType:
			self.t.printERR(varType)
		
		'''if self.grafica != 'paper': # add titolo in INDICE
			# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #	AGGIUNTA A INDICE
			# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
			gids = self.gidRatio.generateGIDverG(self.titoliCounter[1])

			# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
			# <loc l="24" t="78" r="696" b="122" />
			self.baseRadio.attrib['g'] = gids[0]
			self.baseRadio.attrib['verG'] = gids[1]
			self.baseRadio.attrib['id'] = str(self.titoliCounter[1]+2)
			self.baseRadio.attrib['zOrder'] = str(self.titoliCounter[1]+2)
			for r in self.baseRadio.find('stateLst').iter('state'):
				r.find('shapeLst').find('radio').find('plain').text = "%{0}%".format(attrib['name'])
			# print self.baseRadio
			self.baseRadio.find('stateLst').find('state').find('shapeLst').find('radio').find('text').text = self.textRatio.format(attrib['name'])
			self.baseRadio.find('loc').attrib['t'] = str(78+(45*(self.titoliCounter[1]-1)))
			self.baseRadio.find('loc').attrib['b'] = str(78+(45*(self.titoliCounter[1]-1))+44)
			# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
			self.baseTriggerRadio.attrib['g'] = gids[2]
			self.baseTriggerRadio.attrib['verG'] = gids[3]
			self.baseTriggerRadio.find('data').find('shape').attrib['setStateG'] = gids[0]
			self.baseTriggerRadio.find('condLst').find('trigCond').attrib['varG2'] = itemP_Attrib['g']
			# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
			g = tree.Element("g")
			g.text = gids[0]
			# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- # '''

		self.dragDropPnl_lst.append(g)
		self.shapeLst.append(copy.deepcopy(self.baseRadio))
		self.indiceTriggers.append(copy.deepcopy(self.baseTriggerRadio))
		# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
		# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #	AGGIUNTA A INDICE - FINE
		
		self.titCounter += 1
		return tit2

	def addSlide (self, titolo="slide", scena='main'):

		if scena == 'main':
			sldGid = self.wbt.addSlide(self.main, titolo)
			self.mainLst.append(sldGid)

			varGid = self.addTit(titolo)
			self.wbt.addTrig_assingToVar(sldGid, self.titoloSlideGid, 0, varGid[3])

		elif scena == 'indice':
			sldGid = self.wbt.addSlide(self.indice, titolo)

		print "Creata Slide {0} in scena {1}".format( titolo, scena )
		return sldGid

	def linkSlides (self, sld1, sld2):
		self.wbt.addTrig_jumpToSlide(sld1, sld2)
		self.wbt.addTrig_jumpToSlide(sld2, sld1, False)
	def setPageNumber (self, sld, val):
		self.wbt.addTrig_assingToVar(sld, self.pageNumberGid, val)

	def addJobstop (self):
		pass
	def addFin (self):
		pass

	def insertVideo (self, video, sldGid, dxsx='dx'):
		info = self.wbt.importVideo( video )

		pos = None
		if dxsx == 'sx':
			pos = (35, 55, 200, 400)
		elif dxsx == 'dx':
			pos = (450, 55, 200, 400)

		self.wbt.addVideo( 'video1', sldGid, info, pos=pos)
		print "Inserito Video {0} in slide {1}".format( video, sldGid )

	def addVideo (self, video, sldGid):
		# self, nome, assetName, sldGid, pos=(0,0,100,100)):
		if self.grafica == 'paper':
			shps = []
			shps.append( self.wbt.linkImg( 'immagine_1', 'bgVideo', sldGid,  pos=(485, 50, 235, 440)) )
			# shps.append( self.wbt.addVideo() )
			info = self.wbt.importVideo( video )
			shps.append( self.wbt.addVideo( 'video1', sldGid, info, pos=(485, 50, 235, 440))  )
			# self.t.videoInfo("meidainfo/conduzione_01.mov")
			#shps.append( self.wbt.linkImg( 'immagine_2', 'bgVideo', sldGid,  pos=(485, 50, 235, 440)) )
			#shps.append( self.wbt.linkImg( 'immagine_3', 'bgVideo', sldGid,  pos=(100, 100, 235, 440)) )
			#shps.append( self.wbt.linkImg( 'immagine_4', 'bgVideo', sldGid,  pos=(300, 300, 235, 440)) )
			
			self.wbt.formGroup(sldGid, 'video', shps)	