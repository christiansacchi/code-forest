# -*- coding: utf-8 -*-

from tool import Tool
from Gid import Gid
from SLPrefabs import SLPrefabs

class WbtError (Exception):
	def __str__(self):
		return "WbtError"

class WbtE_sceneError (WbtError):
	def __str__(self):
		return "WbtE_sceneError"
class WbtE_sceneE_sceneNotFound (WbtE_sceneError):
	def __str__(self):
		return "WbtE_sceneE_sceneNotFound"

class WbtE_varError (WbtError):
	def __str__(self):
		return "WbtE_varError"
class WbtE_varE_wrongVarType (WbtE_varError):
	def __str__(self):
		return "WbtE_varE_wrongVarType"
class WbtE_varE_badName (WbtE_varError):
	def __str__(self):
		return "WbtE_varE_badName"

class WbtStoryLine (object):
	def __init__ (self, projc):
		# Tools
		self.t = Tool()
		self.g = Gid()
		self.p = SLPrefabs()

		# Attrib
		self.projc = projc
		self.file = self.t.xmlOpen("{0}/story/story.xml".format(projc))
		self.fileRels = self.t.xmlOpen("{0}/story/_rels/story.xml.rels".format(projc))
		self.story = self.t.xmlGetRoot(self.file)
		self.attrib = {
			"id":"", "pG":"", "defChkStyle":"", "defRadStyle":""
		}

		self.totSlide = 0
		self.varList = self.story.find('varLst')
		self.mediaLst = self.story.find('mediaLst').find('mediaLst')
		self.sceneLst = self.story.find('sceneLst')

		self.slideList = {}
		self.layoutLst = {} # Deprecato, da sostituirlo con elementLst !!!
		self.elementLst = {}
		self.assetName = {}

		# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
		self.inportedVideo = 0
		videoCensimentoF = open('asset/prefabs/assetG_ansG_Target_Id.txt', 'r')
		self.videoCensimento = []
		for l in videoCensimentoF.xreadlines():
			self.videoCensimento.append( l.split() )
		# -=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

	def close (self):
		# SAVING STORY FILE ...
		self.t.xmlClose(self.file, "{0}/story/story.xml".format(self.projc))
		self.t.xmlClose(self.fileRels, "{0}/story/_rels/story.xml.rels".format(self.projc), isRels=False)

		self.t.printINFO("{0} PROJECT CLOSED !!!".format(self.projc))

	def save (self, nome):
		# SAVING STORY FILE ...
		self.t.xmlClose(self.file, "{0}/story/{1}.xml".format(self.projc, nome))
		self.t.xmlClose(self.fileRels, "{0}/story/_rels/{1}.xml.rels".format(self.projc, nome), isRels=True)
		
		#self.t.printINFO("PROJECT SAVED !!!")
	def saveSlide (self, nome, f, r):
		# SAVING STORY FILE ...
		self.t.xmlClose(f, "{0}/story/slides/{1}".format(self.projc, nome))

		if r is not None:
			self.t.xmlClose(r, "{0}/story/slides/_rels/{1}.rels".format(self.projc, nome), isRels=True)
		
		#self.t.printINFO("PROJECT.SLIDE SAVED !!!")

	def selectMasterSlide(self, masterSlide):
		# PARTE 1: CONTROLLO SULL'ESISTENZA DELLO SLIDE MASTER INDICATO

		# PARTE 2 DELLA FUNZIONE
		f = open('content\\{0}.style'.format(masterSlide), 'r')
		for l in f:
			l = l.rstrip('\n')
			if l == '': continue
			if l.upper() == 'FIN': break
			l = l.split(' ')
			if l[0] == '//': continue
			self.layoutLst[l[0]] = l[2] # Deprecato, da sostituirlo con elementLst !!!
			self.elementLst[l[0]] = { 'file':l[1], 'gid':l[2], 'info':tuple(l[3:]) }
		f.close()
		#self.t.printINFO(self.elementLst)

		# PARTE 3 DELLA FUNZIONE
		self.t.ctrlC_ctrlV('content\\{0}\\theme\\'.format(masterSlide), "{0}\\story\\theme".format(self.projc))
		self.t.ctrlC_ctrlV('content\\{0}\\slideMasters\\'.format(masterSlide), "{0}\\story\\slideMasters".format(self.projc))
		self.t.ctrlC_ctrlV('content\\{0}\\slideLayouts\\'.format(masterSlide), "{0}\\story\\slideLayouts".format(self.projc))

		for f in self.t.dir('content\\{0}\\media\\'.format(masterSlide)):
			self.t.ctrlC_ctrlV_file(f, "{0}\\story\\media".format(self.projc))

		theme = self.t.xmlOpen("{0}/story/theme/theme.xml".format(self.projc))
		themeFile = self.t.xmlGetRoot(theme)
		themeMedia = themeFile.find('assetLst').find('mediaLst')
		for m in themeMedia:
			self.mediaLst.append(m)
		self.save('story')

	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- VAR -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
	def setVariable (self, nome, val):
		for c in ['.', ',', '-']:
			if c in nome:
				raise WbtE_varE_badName

		tipo = None

		if type(val) is int or type(val) is float or type(val) is long:
			tipo = 'num'
			# val: non troppo lunghi, val: convertire in str
		elif type(val) is str:
			tipo = 'text'
		elif type(val) is bool:
			tipo = 'bool'
			# val: convertire in str
		else:
			raise WbtE_varE_wrongVarType

		faf = self.g.get("var")
		'''attrib = {	"name":nome, "dataType":tipo, "val":str(val),
					"g":faf[0], "verG":faf[1],
					"type":"user", "propPath":"" }
		var = self.t.xmlTag("var", attrib)'''
		var = self.p.var(tipo, nome, val, faf)
		self.varList.append(var)

		return (nome, tipo, val, faf[0])
	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- VAR -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #



	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SCENE -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SCENE -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SCENE -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
	def addScene (self, nome, isMain=False):
		faf = self.g.get("scene") # "g":faf[0], "verG":faf[1]
		attrib = {	"name":nome, "desc":"",
					"g":faf[0], "verG":faf[1], "primaryId":self.g.get()[0],
					"sceneType":"scene", "collapse":"false" }

		scene = self.t.xmlTag("scene", attrib)
		scene.append(  self.t.xmlTag("sldIdLst", {} )  )

		self.sceneLst.append(scene)

		if isMain:
			self.story.attrib['pG'] = attrib['g']

		#self.t.printLOG('<scena:{0}, gid:{1}>'.format(nome, attrib['g']))
		return attrib['g']
	def getScene (self, gid="main"):
		g = gid
		if gid.lower() == "main":
			g = self.story.attrib["pG"]

		for scene in self.sceneLst:
			if scene.attrib['g'] == g:
				return scene
		return None
	def printScenes (self):
		for scene in self.sceneLst:
			print "<{0} nome:{1}, g:{2}, verG:{3}>".format(scene.tag, scene.attrib['name'], scene.attrib['g'], scene.attrib['verG'])
	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SCENE -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SCENE -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SCENE -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #



	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SLIDE -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SLIDE -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SLIDE -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
	def getSlideNames (self, sceneG):
		#s = self.getScene(sceneG)
		#if s is None:
		#	s = self.getScene("main")

		l = self.totSlide
		#l = len(s.find("sldIdLst"));
		l += 1 

		nomeFile = "slide"
		if (l > 1):
			nomeFile += "{0:x}".format(l)

		t = ( "{0}.xml".format(nomeFile), "{0}.xml.rels".format(nomeFile), "R5{0:010x}".format(l).upper() )
		return t
	def addSlide (self, sceneG, nome, layout="titolo", faf=None):
		# SELEZIONA DELLA SCENE
		s = self.getScene(sceneG)
		if s is None:
			s = self.getScene("main")
		sldIdLst = s.find("sldIdLst")

		# GENERAZIONE DELLO SPAZIO DEI NOMI DELLA SLIDE
		names = self.getSlideNames('main')

		# CREAZIONE FILE DI SLIDE
		# modifica di nome, g, verG, layoutG
		sldRoot = self.t.xmlOpen("asset\\prefabs\\slide.xml")
		relRoot = self.t.xmlOpen("asset\\prefabs\\slide.xml.rels")
		sld = self.t.getAsset(sldRoot)
		# rel = self.t.getAsset(relRoot) # non serve prendere la root

		if faf is None:
			faf = self.g.get("slide") # "g":faf[0], "verG":faf[1]

		sld.attrib['name'] = nome
		sld.attrib['id'] = '0'
		sld.attrib['g'] = faf[0]
		sld.attrib['verG'] = faf[1]
		sld.attrib['layoutG'] = self.elementLst[layout]['gid'] # !!!!!!!!!!!!!!!!!!!!!!!

		# ADD SLIDE _ID IN story.xml.rels
		storyRel = self.t.getAsset(self.fileRels)
		attrib = { "Type":"slide", "Target":"/story/slides/{0}".format(names[0]), "Id":names[2] }
		relationship = self.t.xmlTag("Relationship", attrib)
		storyRel.insert(self.totSlide, relationship)

		# ADD SLIDE _ID IN story.scene
		sldId = self.t.xmlTag("sldId", {})
		sldId.text = names[2]
		sldIdLst.append(sldId)

		# SAVE SLIDE
		sldRoot._setroot(sld)				# RIMPIAZZO DELLA ROOT
		self.fileRels._setroot(storyRel)	# RIMPIAZZO DELLA ROOT

		self.saveSlide(names[0], sldRoot, relRoot) # save slide
		self.save('story') # save story

		# RETURN RIFERIMENTO A SLIDE, PER POTERCI AGGIUNGERE TRIGGER
		self.totSlide += 1
		#self.t.printLOG('<slide:{0}, gid:{1}, scena:{2}>'.format(nome, sld.attrib['g'], sceneG))

		# ADD SLIDE TO SLIDE LIST
		self.slideList[faf[0]] = names[0]

		return sld.attrib['g']

	def addTrig (self):
		pass
	def addTrig_jumpToSlide (self, sldFrom, sldTo, isNext=True):
		if not self.slideList.has_key(sldFrom) and not self.slideList.has_key(sldTo): 
			return

		sldRoot = self.t.xmlOpen("{0}/story/slides/{1}".format(self.projc, self.slideList[sldFrom]))
		sld = self.t.getAsset(sldRoot)

		trigLst = sld.find('trigLst')
		trig = self.p.jumpToSlide_onNextBtt(sld.attrib['g'], sldTo, isNext)
		trigLst.append(trig)

		sldRoot._setroot(sld)
		self.saveSlide(self.slideList[sldFrom], sldRoot, None) # save slide
	def addTrig_assingToVar (self, sldGid, varGid, value, var1G=None):
		if not self.slideList.has_key(sldGid): 
			return

		sldRoot = self.t.xmlOpen("{0}/story/slides/{1}".format(self.projc, self.slideList[sldGid]))
		sld = self.t.getAsset(sldRoot)

		trigLst = sld.find('trigLst')
		trig = self.p.addTrig_assingToVar(sld.attrib['g'], varGid, value, var1G)
		trigLst.append(trig)

		sldRoot._setroot(sld)
		self.saveSlide(self.slideList[sldGid], sldRoot, None) # save slide

	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SLIDE -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SLIDE -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
	# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SLIDE -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

	def calcAreaGroup (self, elenco):

		areaGroup = [9999,9999,0,0]

		for shp in elenco:
			loc = shp.find('loc')
			t = int(loc.attrib['t'])
			b = int(loc.attrib['b'])
			l = int(loc.attrib['l'])
			r = int(loc.attrib['r'])

			if (areaGroup[0] > t): areaGroup[0] = t
			if (areaGroup[1] > l): areaGroup[1] = l
			if (areaGroup[2] < b): areaGroup[2] = b
			if (areaGroup[3] < r): areaGroup[3] = r

		t = areaGroup[0]; l = areaGroup[1]
		b = areaGroup[2]; r = areaGroup[3]

		cords = ( t, l, (r-l), (b-t) )
		return cords

	def formGroup (self, sldGid, nome, elenco=[]):

		sldRoot = self.t.xmlOpen("{0}/story/slides/{1}".format(self.projc, self.slideList[sldGid]))
		sld = self.t.getAsset(sldRoot)

		relRoot = self.t.xmlOpen("{0}/story/slides/_rels/{1}.rels".format(self.projc, self.slideList[sldGid]))
		rel = self.t.getAsset(relRoot)

		gids = self.g.get('group')
		group = self.p.group(nome, gids)
		childs = group.find('childLst')

		shapeLst = sld.find('shapeLst')

		locList = []
		for shp in shapeLst:
			if shp.attrib.has_key('g'):
				if shp.attrib['g'] in elenco:
					shp.attrib['parentG'] = gids[0]
					locList.append( shp )
				childs.append( self.p.childGroup(shp.attrib['g']) )

		pos = self.calcAreaGroup( locList )
		group.append( self.p.loc( *pos ) )

		# INSERIMENTO GRUPPO
		shapeLst.append( group )

		# SAVE SLIDE
		sldRoot._setroot(sld)	# RIMPIAZZO DELLA ROOT
		relRoot._setroot(rel)	# RIMPIAZZO DELLA ROOT
		self.saveSlide(self.slideList[sldGid], sldRoot, relRoot) # save slide

	def importVideo (self, video):
		# assetG_ansG_Target_Id
		vidCens = self.videoCensimento[self.inportedVideo]

		# OPERAZIONI SUL VIDEO
		vidPath = self.t.path_assoluto( video )
		i = vidPath
		o = "{0}\\story\\media\\{1}.mp4".format(self.projc, vidCens[2])
		#self.t.printINFO( i+";\n"+o )
		res = self.t.videoConverter(i, o)
		#self.t.printINFO( o+";\n"+o )
		self.t.rinomina(o, o[:-4]+".mpeg")
		o = o[:-4]+".mpeg"

		origBytes = self.t.videoInfo(i)['size']
		outInf = self.t.videoInfo(o)
		#self.t.printINFO( origBytes+";\n"+outInf['size'] )

		g = ( vidCens[0], "{0}123".format(vidCens[0][:-3]) )
		mediaVid = self.p.mediaVideo( g, vidPath, outInf['size'], origBytes)

		# Inserimento video in story.xml
		self.mediaLst.append( mediaVid )

		self.inportedVideo += 1

		outInf["assetG"] = vidCens[0]     # assetG_ansG_Target_Id
		outInf["ansG"] = vidCens[1]
		outInf["target"] = vidCens[2]
		outInf["id"] = vidCens[3]
		#self.t.printINFO( outInf )
		return outInf

	def addVideo (self, nome, sldGid, info, pos=(0,0,100,100)):
		sldRoot = self.t.xmlOpen("{0}/story/slides/{1}".format(self.projc, self.slideList[sldGid]))
		sld = self.t.getAsset(sldRoot)

		relRoot = self.t.xmlOpen("{0}/story/slides/_rels/{1}.rels".format(self.projc, self.slideList[sldGid]))
		rel = self.t.getAsset(relRoot)

		# MODIFICE ALLA SLIDE.xml
		gids = self.g.get('media')
		shapeLst = sld.find('shapeLst')
		vid = self.p.video(nome, gids, info["assetG"], info["ansG"], info["duration"], pos=pos)
		shapeLst.append( vid )
		#self.t.printINFO( vid )

		# MODIFICHE ALLA SLIDE.rel
		vidR = self.p.relationship("media", "/story/media/{0}.mpeg".format(info["target"]), info["id"])
		rel.append( vidR )
		#self.t.printINFO( vidR )

		# SAVE SLIDE
		sldRoot._setroot(sld)	# RIMPIAZZO DELLA ROOT
		relRoot._setroot(rel)	# RIMPIAZZO DELLA ROOT
		self.saveSlide(self.slideList[sldGid], sldRoot, relRoot) # save slide

	def addAudio (self):
		pass

	def addImage (self):
		pass
	def linkImg (self, nome, assetName, sldGid, pos=(0,0,100,100)):
		# HEADER
		sldRoot = self.t.xmlOpen("{0}/story/slides/{1}".format(self.projc, self.slideList[sldGid]))
		sld = self.t.getAsset(sldRoot)

		relRoot = self.t.xmlOpen("{0}/story/slides/_rels/{1}.rels".format(self.projc, self.slideList[sldGid]))
		rel = self.t.getAsset(relRoot)

		gids = self.g.get('media')

		# BODY { 'file':l[1], 'gid':l[2], 'info':tuple(l[3:]) }
		shapeLst = sld.find('shapeLst')
		pic = self.p.pic(nome, gids, self.elementLst[assetName]['gid'], pos=pos)
		shapeLst.append( pic )


		#self.t.printERR("pic: {0}".format( sld.find('shapeLst').find('pic').find('tmProps')) )
		#self.t.printERR("pic: {0}".format( sld.find('shapeLst').find('pic').find('tmCtxLst')) )
		#self.t.printERR("pic: {0}".format( sld.find('shapeLst').find('pic').find('tmCtxLst').find('tmCtx')) )

		# self.elementLst[assetName]['info'][0]
		relation = self.p.relationship('media', "/story/media/{0}".format(self.elementLst[assetName]['file']), self.g.iD("media"))
		self.t.printERR(relation)
		rel.insert(0, relation)
		#self.t.printERR("relationship: {0}".format( rel.find('Relationship').attrib) )

		# SAVE SLIDE
		sldRoot._setroot(sld)	# RIMPIAZZO DELLA ROOT
		relRoot._setroot(rel)	# RIMPIAZZO DELLA ROOT
		self.saveSlide(self.slideList[sldGid], sldRoot, relRoot) # save slide

		return gids[0]