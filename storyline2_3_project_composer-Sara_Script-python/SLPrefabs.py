# -*- coding: utf-8 -*-

from tool import Tool
from Gid import Gid
import simplejson as json

'''
faf = self.g.get("var")
attrib = {	"name":nome, "dataType":tipo, "val":str(val),
			"g":faf[0], "verG":faf[1],
			"type":"user", "propPath":"" }
var = self.t.xmlTag("var", attrib)
'''

class SLPrefabs():
	zOrder = 0
	iD = 1
	version = 1

	def __init__(self):
		self.t = Tool()
		self.g = Gid()

	def reset (self):
		self.zOrder = 0
		self.iD = 1
		self.version = 0

	def var (self, t, n, v, gids):
		valFin = None
		if type(v) in (str, unicode):
			valFin = v
		else:
			valFin = str(v)

		attrib = {	"name":n, "dataType":t, "val":valFin,
					"g":gids[0], "verG":gids[1],
					"type":"user", "propPath":"" }
		tag = self.t.xmlTag("var", attrib)
		return tag

	def jumpToSlide_onNextBtt (self, copiedG, jumpG, isNext=True):
		trig = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\jumpToSlide_onNextBtt.xml") )
		trigData = trig.find('data')
		dataSlide = trigData.find('slide')

		gids = self.g.get('trig')

		event = actionG = group = None
		if isNext:
			nome = "Navigation"
			group = "next"
			event = "OnNextButtonClick"
			actionG = "0ec0db78-2e1d-4919-bde6-6824587f77c4" # ID PER IL NEXT BUTTON
		else:
			nome = "Previous"
			group = "none"
			event = "OnClick"
			actionG = "ae475cc5-601c-414e-82c1-df8dc7d39471" # ID PER IL PREV BUTTON

		trig.attrib['name'] = nome
		trig.attrib['group'] = group
		trig.attrib['g'] = gids[0]
		trig.attrib['verG'] = gids[1]
		trig.attrib['copiedG'] = copiedG

		trigData.attrib['event'] = event
		trigData.attrib['action'] = "jumpToSlide"
		trigData.attrib['actSubType'] = "spec"

		dataSlide.attrib['jumpG'] = jumpG
		trigData.find('frame').attrib['actionG'] = actionG

		return trig

	def trigCond (self, cond, andOr):
		trig = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\trigCond.xml") )
		gids = self.g.get('trig')

		trig.attrib['g'] = gids[0]
		trig.attrib['verG'] = gids[1]

		trig.attrib['op'] = cond
		trig.attrib['andOr'] = andOr

		return trig

	def trigger_base(self, copiedG):
		trig = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\trigger_base.xml") )
		gids = self.g.get('trig')

		trig.attrib['g'] = gids[0]
		trig.attrib['verG'] = gids[1]
		trig.attrib['copiedG'] = copiedG

		return trig

	def customData (self, cD_dict={}):
		cD = self.t.xmlTag('customData', cD_dict)
		return cD

	def addTrig_assingToVar (self, copiedG, varG, val, var1G=None):
		trig = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\setPageNumber.xml") )
		trigData = trig.find('data')
		dataOther = trigData.find('other')

		gids = self.g.get('trig')

		trig.attrib['g'] = gids[0]
		trig.attrib['verG'] = gids[1]
		trig.attrib['copiedG'] = copiedG

		if var1G is not None:
			dataOther.attrib['var1G'] = var1G
			dataOther.attrib['useVar'] = 'true'

		dataOther.attrib['varG'] = varG
		dataOther.attrib['dblVal'] = str(val)

		return trig

	def addTrig_playMedia (self, videoG):
		trig = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\playMedia.xml") )
		trigVid = trig.find('data').find('video')

		gids = self.g.get('trig')

		trig.attrib['g'] = gids[0]
		trig.attrib['verG'] = gids[1]
		trig.attrib['copiedG'] = videoG

		trigVid.attrib['playG'] = videoG

		return trig

	def rsltsIntr (self, quizG, sucs, fail, guids):
		q = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\rsltsIntr.xml") )
		gids = self.g.get('quiz')

		q.attrib['g'] = gids[0]; q.attrib['verG'] = gids[1]

		# ...
		q.attrib['name'] = 'RES'
		q.attrib['id'] = str(self.iD)
		q.attrib['quizG'] = quizG

		tag_suc = q.find('success')
		tag_suc.attrib['trigG'] = sucs[0]
		tag_suc.attrib['g'] = sucs[1]

		tag_fil = q.find('failure')
		tag_fil.attrib['trigG'] = fail[0]
		tag_fil.attrib['g'] = fail[1]

		tag_gud = q.find('guids')
		tag_gud.attrib['uScSG'] = guids[0]
		tag_gud.attrib['pScSG'] = guids[1]

		self.iD += 1
		return q

	def quiz_tag (self, nome, varGs, resultSldG=None, passScore=60):
		q = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\quiz_tag.xml") )
		gids = self.g.get('quiz')

		q.attrib['g'] = gids[0]; q.attrib['verG'] = gids[1]
		q.attrib['name'] = nome

		q.attrib['scorePct'] = varGs[0]
		q.attrib['scorePoints'] = varGs[1]
		q.attrib['passPoints'] = varGs[2]
		q.attrib['passPct'] = varGs[3]

		if resultSldG is not None:
			q.attrib['resultSldG'] = resultSldG

		q.attrib['passScore'] = str( passScore )

		return q

	jobstopTipi = {
		'VF':('trueFalseIntr','df10780a-4cfd-4805-b876-271b909097e5', '2'),
		'MC':('multiChoiceIntr', '9ddb7ca0-d0e8-4e76-9684-3851ebaad90a', '10')
	}
	def jobstop (self, tipo, titleBoxG, incG, corG):
		q = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\jobstopType.xml") )
		q.tag = self.jobstopTipi[tipo][0]

		#gids = self.g.get('quiz')
		#q.attrib['g'] = gids[0]; q.attrib['verG'] = gids[1]

		intProp = q.find('intrProps')
		intProp.attrib['titleBoxG'] = titleBoxG
		intProp.attrib['intrG'] = self.jobstopTipi[tipo][1]
		intProp.attrib['incFbG'] = incG
		intProp.attrib['ansG'] = self.g.get('quiz')[1]
		intProp.attrib['corFbG'] = corG
		intProp.attrib['max'] = self.jobstopTipi[tipo][2]

		return q

	def jb_VeroFalso (self, titleBoxG, incG, corG):
		return self.jobstop ('VF', titleBoxG, incG, corG)
	def jb_MultiChois (self, titleBoxG, incG, corG):
		return self.jobstop ('MC', titleBoxG, incG, corG)

	def tmProps (self):
		gids = self.g.get('timeProbe')
		attrib = {	"cur":"0", "min":"5000", "visible":"true", "hideAll":"false",
					"g":gids[0], "verG":gids[1]  }
		tmp = self.t.xmlTag("tmProps", attrib)
		return tmp

	def tmCtxLst (self, version=1):
		tmp = self.t.xmlTag("tmCtxLst", {"version":str(version)})
		return tmp

	def tmCtx (self, start=0, dur=3000, untilEnd=False, alwysShw=False, tagName="tmCtx"):
		gids = self.g.get('timeProbe')
		attrib = {	"start":str(start), "dur":str(dur), "min":"250", "max":"0",
					"hasMax":"false", "alwysShw":str(alwysShw).lower(), "untilEnd":str(untilEnd).lower(), "assetStart":"0", "name":"",
					"g":gids[0], "verG":gids[1]  }
		tmp = self.t.xmlTag(tagName, attrib)
		return tmp

	def loc (self, x, y, w, h):
		attrib = {
			"l":str(x), "t":str(y),
			"r":str(x+w), "b":str(y+h),
		}
		l = self.t.xmlTag('loc', attrib)
		return l

	def sldLayerLst (self):
		sldLy = self.t.xmlTag('sldLayerLst', {'nextIdx':'0'})
		return sldLy

	def layer(self, nome, gids=None, layout='01dfe22b-2e1c-4dc9-a514-a7d3f1ab7177'):
		ly = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\layer.xml") )

		if gids is None:
			gids = self.g.get('slide')

		if type(gids) is not str:
			ly.attrib['g'] = gids[0]
			ly.attrib['verG'] = gids[1]

		ly.attrib['name'] = nome
		ly.attrib['layoutG'] = layout

		return ly


	def group (self, nome, gids=None):
		# La posizione e la grandezza dipendono dall-elemento pi\ grande nel gruppo, sono gli stessi
		group = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\group.xml") )

		if gids is not None:
			pic.attrib['g'] = gids[0]; pic.attrib['verG'] = gids[1]
		
		group.attrib['name'] = 'Group&#xD;&#xA;'
		group.attrib['typeName'] = nome
		group.attrib['id'] = str(self.iD);
		group.attrib['zOrder'] = str(self.zOrder)

		self.iD += 1
		return group

	def scrollBox(self, nome, gids=None):
		group = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\scrollBox.xml") )
		
		if gids is not None:
			pic.attrib['g'] = gids[0]; pic.attrib['verG'] = gids[1]
		
		group.attrib['name'] = 'Group&#xD;&#xA;'
		group.attrib['typeName'] = nome
		group.attrib['id'] = str(self.iD);
		group.attrib['zOrder'] = str(self.zOrder)

		self.iD += 1
		return group
		
	def shapeMedia (self, tag, typeName, name, assetG, gids, parentG=""):
		''' Funzione che probabilmente non userò mai '''
		attrib = {	"typeName":typeName, "id":str(self.iD), "name":name, "state":"107079",
					"zOrder":str(self.zOrder), "editCtx":"Normal", "initState":"", "handCur":"true", "rot":"-1", "acc":"true",
					"g":gids[0], "verG":gids[1], "assetG":"", "parentG":parentG  }
		shape = self.t.xmlTag(tag, attrib)
		return shape

	def relationship (self, tipo, target, iD):
		attrib = { "Type":tipo, "Target":target, "Id":iD }
		rel = self.t.xmlTag('Relationship', attrib)
		return rel
	def childGroup (self, gidChild):
		g = self.t.xmlTag('g', {})
		g.text = gidChild
		return g

	def fadeIn (self, time=25, direz="none"):
		entr = self.t.xmlTag('entr', {})
		fade = self.t.xmlTag('fade', {"dur":"PT0.{0}S".format(time), "lvl":"none", "easingDir":"none", "easingType":"lin", "dir":direz} )
		entr.append( fade )
		return entr
	def fadeOut (self, time=25, direz="none"):
		exit = self.t.xmlTag('exit', {})
		fade = self.t.xmlTag('fade', {"dur":"PT0.{0}S".format(time), "lvl":"none", "easingDir":"none", "easingType":"lin", "dir":direz} )
		exit.append( fade )
		return exit

	def posizione (self, pos, size):
		x = pos[0]; y = pos[1]
		w = size[0]; h = size[1]

		loc = self.t.xmlTag('loc', {"l":"{0}".format(x), "t":"{0}".format(y), "r":"{0}".format(x+w), "b":"{0}".format(y+h)} )
		return loc

	def pic (self, nome, gids, assetG, effect=(1,0)):
		pic = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\pic.xml") )

		if gids is not None:
			pic.attrib['g'] = gids[0]
			pic.attrib['verG'] = gids[1]

		pic.attrib['typeName'] = nome
		pic.attrib['name'] = "Picture"
		pic.attrib['assetG'] = assetG
		pic.attrib['id'] = str(self.iD)

		if gids is not None:
			# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
			# FADE IN - FADE OUT
			animEffect = vid.find('animEffect')
			if effect[0] == 1:
				animEffect.append( self.fadeIn() )
			if effect[1] == 1:
				animEffect.append( self.fadeOut() )
			# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

		self.iD += 1

		return pic

	def video (self, nome, gids, assetG, ansG, time=3000, parentG="", pos=(0,0,100,100), effect=(1,1,0), thumbG="11eb06a1-9aae-4e2f-91de-4e12939b8bf0"):
		vid = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\video.xml") )

		if gids is not None:
			vid.attrib['g'] = gids[0]
			vid.attrib['verG'] = gids[1]

		vid.attrib['typeName'] = nome
		vid.attrib['name'] = "Video"
		vid.attrib['assetG'] = assetG
		vid.attrib['ansG'] = ansG
		vid.attrib['thumbG'] = thumbG
		vid.attrib['id'] = str(self.iD)

		# vid.append( self.loc( *pos ) ) !!!!! self.loc() e' obsoleta 

		if gids is not None:
			# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
			# FADE IN - FADE OUT
			animEffect = vid.find('animEffect')
			if effect[1] == 1:
				animEffect.append( self.fadeIn() )
			if effect[2] == 1:
				animEffect.append( self.fadeOut() )
			# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

		self.iD += 1
		return vid

	def timing (self, xml, startTime, duration, shw_tilEnd, shw_always, TmCtx_name="tmCtx"):
		# <tmProps>
		xml.insert(0, self.tmProps())

		# <tmCtxLst>
		xml.find('tmCtxLst').attrib['version'] = str(self.version) #.update({"version":str(version)})
		tm = self.tmCtx(start=startTime, dur=duration, untilEnd=shw_tilEnd, alwysShw=shw_always, tagName=TmCtx_name)
		xml.find('tmCtxLst').insert(1, tm)

		self.version += 1

	def mediaVideo (self, gids, dN_orF_sou, bytes, origBytes):
		vid = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\media_video.xml") )

		vid.attrib['g'] = gids[0]
		vid.attrib['verG'] = gids[1]

		vid.attrib['displayName'] = dN_orF_sou
		vid.attrib['origFile'] = dN_orF_sou
		vid.attrib['source'] = dN_orF_sou

		vid.attrib['bytes'] = bytes
		vid.attrib['origBytes'] = origBytes

		return vid

	def mediaPic (self, gids, bytes, path, tipo='png'):
		pic = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\media_pic.xml") )

		pic.attrib['g'] = gids[0]
		pic.attrib['verG'] = gids[1]

		pic.attrib['type'] = tipo

		pic.attrib['displayName'] = path
		pic.attrib['origFile'] = path
		pic.attrib['source'] = path

		pic.attrib['bytes'] = bytes

		return pic

	def textBox (self, name, plain):
		tx = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\text.xml") )
		tx.attrib['displayName'] = name
		tx.attrib['autoFit'] = 'none'

		pln = tx.find('plain')
		pln.text = plain
		
		return tx

	def textBox_tagText (self, plain, fontFamily, fontSize, color, isBold=False, isItalic=False):
		tx = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\text_tagText.xml") )
		span = tx.find('Content').find('Block').find('Span')
		stile = span.find('Style')

		span.attrib['Text'] = plain
		stile.attrib['FontFamily'] = fontFamily
		stile.attrib['FontSize'] = fontSize
		stile.attrib['ForegroundColor'] = color
		stile.attrib['LinkColor'] = color

		if isBold == True:
			stile.attrib['FontIsBold'] = str( isBold )
		if isItalic == True:
			stile.attrib['FontIsItalic'] = str( isItalic )

		return tx

	def textBox_tagFtmText (self, plain, fontFamily, fontSize, isBold=False, isItalic=False):
		tx = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\text_tagFtmText.xml") )
		span = tx.find('Content').find('Block').find('Span')
		stile = span.find('Style')

		span.attrib['Text'] = plain
		stile.attrib['FontFamily'] = fontFamily
		stile.attrib['FontSize'] = fontSize
		stile.attrib['FontIsBold'] = str( isBold )
		stile.attrib['FontIsItalic'] = str( isItalic )

		return tx

	def ratio (self, nome, testo, stile="radio.xml", stileTesto=['Arial Narrow', '12', '#808080', False, False], initState=None):
		rat = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\{0}".format(stile)) )

		rat.attrib['typeName'] = str(nome)
		rat.attrib['id'] = str(self.iD)
		rat.attrib['zOrder'] = str(1)

		if initState is not None:
			rat.attrib['initState'] = initState
			rat.attrib['editCtx'] = initState

		i = 0
		for stato in rat.find('stateLst').iter('state'):
			r = stato.find('shapeLst').find('radio')
			r.find('plain').text = testo

			if i == 0:
				stileFont = stileTesto

				txt1 = self.textBox_tagText(testo, stileFont[0], stileFont[1], stileFont[2], stileFont[3], stileFont[4] )
				txt2 = self.textBox_tagFtmText(testo, stileFont[0], stileFont[1], stileFont[3], stileFont[4] )

				txt1 = self.t.xmltoTextedXml( txt1 )
				txt2 = self.t.xmltoTextedXml( txt2 )

				r.find('text').text = txt1
				r.find('fmtText').text = txt2
			i += 1

		self.iD += 1

		return rat

	def state (self, nome, defG):
		sta = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\state.xml") )
		sta.attrib['name'] = nome
		sta.attrib['defG'] = defG
		return sta

	def bnk_scene (self, nome):
		scn = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\bnkScene.xml") )
		scn.attrib['name'] = nome

		gids = self.g.get('scene')
		scn.attrib['g'] = gids[0]
		scn.attrib['verG'] = gids[1]
		
		return scn

	def scene (self, nome):
		scn = self.t.getAsset( self.t.xmlOpen("asset\\prefabs\\scene.xml") )
		scn.attrib['name'] = nome

		gids = self.g.get('scene')
		scn.attrib['g'] = gids[0]
		scn.attrib['verG'] = gids[1]
		
		return scn
