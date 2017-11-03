# -*- coding: utf-8 -*-
from tool import Tool
import Gid
from SLPrefabs import SLPrefabs

t = Tool()

# ###################################################################### #
# #### LIVELLO 1 ####################################################### #
# ###################################################################### #
class StoryLineObj(object):
	''' Qualsiasi elemento abbia almeno un g e un verG '''
	
	# Tools
	gidGen = Gid.Gid()
	tools = Tool()
	prefabs = SLPrefabs()

	# Vars
	c = 0

	def __init__ (self, gids, xml, rel=None):
		self.g = None
		self.verG = None
		self.xml = None
		self.rel = None

		self.f_xml = xml
		self.f_rel = rel

		if gids is None:
		# Se non vengono passati GID allora significa
		# che li devo andare a prendere dalla struttura xml stessa 

			keyList = self.f_xml.attrib.keys()
			if 'id' in keyList and 'pG' in keyList:
				self.g = self.f_xml.attrib['id']
				self.verG = self.f_xml.attrib['pG']
			else:
				self.g = self.f_xml.attrib['g']
				self.verG = self.f_xml.attrib['verG']
				
		else:
		# Se invece viene passato qualcosa a GID, allora genero gli id
		# in base a quello che mi viene passato, poi li metto io nella struttura
			# print gids
			g = self.gidGen.get(gids)
			self.g = g[0]
			self.verG = g[1]
			keyList = self.f_xml.attrib.keys()
			if 'id' in keyList and 'pG' in keyList:
				self.f_xml.attrib['id'] = self.g
				self.f_xml.attrib['pG'] = self.verG
			else:
				self.f_xml.attrib['g'] = self.g
				self.f_xml.attrib['verG'] = self.verG

		# COMPLETATO g
		# COMPLETATO verG
		# COMPLETATO xml
		# COMPLETATO rel

		self.c += 1

	def getGid (self, friz_and_frez=False):
		if not friz_and_frez:
			return self.g
		else:
			return ( self.g, self.verG )
	def getStruct (self):
		return self.f_xml
# ###################################################################### #
# #### LIVELLO 1 ####################################################### #
# ###################################################################### # FINE









# ###################################################################### #
# #### LIVELLO 2 ####################################################### #
# ###################################################################### #
class SlObj_FixedObj (StoryLineObj):
	def __init__ (self, g, xml, rel=None):
		super(SlObj_FixedObj, self).__init__(g, xml, rel)

# [! [! [! [! [! [! [! [! [! [! [! [! [! [! [!] !] !] !] !] !] !] !] !] !] !] !] !] !] !] #

class SlObj_TimelineObj (StoryLineObj):
	def __init__ (self, g, xml, rel=None, time=5000, timing=None, moreInfo=None):
		super(SlObj_TimelineObj, self).__init__(g, xml, rel)

		self.time = None
		self.startTime = None
		self.duration = None
		self.shw_tilEnd = None
		self.shw_always = None
		
		if timing is None:
			# print "G is {0}".format(g)
			tmProps = self.f_xml.find('tmProps')
			if g is None:
				self.time = time
				tmProps.attrib['min'] = str(time)
			else:
				self.time = int( tmProps.attrib['min'] )

		elif timing is not None:
			self.setTiming(timing[0], timing[1], timing[2], timing[3], moreInfo)

		# TRIGGER
		self.l_trig = []

	def addTrig (self, trig):
		self.l_trig.append( trig )
		self.f_xml.find('trigLst').append( trig.f_xml )

	def StartTime (self, t=None):
		if t is None:
			return self.startTime
		else:
			self.startTime = t
			self.retiming( self.startTime, None )

	convs = {None:'tmCtx', 'video':'vidTmCtx', 'text':'txtTmCtx'}
	def setTiming (self, startTime, duration, shw_tilEnd=False, shw_always=False, moreInfo=None):
		self.prefabs.timing(self.f_xml, startTime, duration, shw_tilEnd, shw_always, self.convs[moreInfo])

		self.startTime = startTime
		self.duration = duration
		self.shw_tilEnd = shw_tilEnd
		self.shw_always = shw_always

	def retiming (self, startTime, duration, shw_tilEnd=False, shw_always=False):
		probe = None
		for tmFind in ('tmCtx', 'vidTmCtx', 'txtTmCtx'):
			if probe is None:
				probe = self.f_xml.find('tmCtxLst').find(tmFind)

		if startTime is not None:
			probe.attrib['start'] = str( startTime )
			self.startTime = startTime

		if duration is not None:
			probe.attrib['dur'] = str( duration )
			self.duration = duration

		probe.attrib['untilEnd'] = str( shw_tilEnd )
		probe.attrib['alwysShw'] = str( shw_always )
		self.shw_tilEnd = shw_tilEnd
		self.shw_always = shw_always


# ###################################################################### #
# #### LIVELLO 2 ####################################################### #
# ###################################################################### # FINE









# ###################################################################### #
# #### LIVELLO 3 ####################################################### #
# ###################################################################### #
class SlObj_ProgObj (SlObj_FixedObj):
	progC = 0
	def __init__ (self, g, xml, rel=None):

		f_xml = self.tools.xmlGetRoot(xml)
		f_rel = self.tools.xmlGetRoot(rel)

		super(SlObj_ProgObj, self).__init__(g, f_xml, f_rel)

		self.xml = xml
		self.rel = rel
		self.path = None

		self.l_rels = []
		xmlns = "{http://schemas.openxmlformats.org/package/2006/relationships}Relationships"
		for rel in self.f_rel.iter():
			if rel.tag != xmlns:
				self.l_rels.append( (rel.attrib['Id'], rel.attrib['Target'], rel.attrib['Type']) )

		self.l_media = None

		self.progC += 1

	def create (self):
		pass
	def open (self):
		pass
	def close (self):
		pass

	def get_media (self, g):
		for media in self.l_media:
			if media.g == g:
				return media
		return None
	def get_media_byPath (self, fileName):
		for media in self.l_media:
			if media.fileName == fileName:
				return media
		return None

	def add_media (self, tag, fileName, xml=None, nick=""):
		media = Sl_MediaObj(tag, fileName, xml=xml, nome=nick)
		self.l_media.append( media )
		return media.g

	def importPic (self, f, nick):
		pic_nameSpace = self.censimentoPic[self.imprtPic]; self.imprtPic += 1

		pic_i = self.tools.path_assoluto( f )
		pic_o = "{0}\\story\\media\\{1}.png".format(self.path, pic_nameSpace[1])

		self.tools.ctrlC_ctrlV_file(pic_i, pic_o)

		inf = self.tools.videoInfo(pic_o)

		# CREAZIONE STRUTTURA XML ---> mediaPic (self, gids, bytes, path, tipo='png')
		g = ( pic_nameSpace[0], "{0}123".format(pic_nameSpace[0][:-3]) )
		xml = self.prefabs.mediaPic( g, inf['size'], pic_i)

		# INSERIMENTO XML VIDEO STRUCT NELLA LISTA MEDIA DELLO STORY
		# part 1
		mediaG = self.add_media('media', pic_i, xml, nick)
		media = self.get_media(mediaG)
		extInf = {'target':pic_nameSpace[1],'id':pic_nameSpace[2],'size':(inf['width'], inf['height'])}
		media.add_extraInfo( extInf )
		# part 2
		mediaList = None
		if self.f_xml.find('assetLst') is not None:
			mediaList = self.f_xml.find('assetLst').find('mediaLst') # From theme.xml
		else:
			mediaList = self.f_xml.find('mediaLst').find('mediaLst') # From story.xml
		mediaList.append(xml)

		return g[0]

	def importVideo (self, f, nick):
		vid_nameSpace = self.censimentoVd[self.inportedVd]; self.inportedVd += 1

		vd_i = self.tools.path_assoluto( f )
		#vid_nameSpace[2] = "{1}".format(nick, self.tools.joke_loading(0, 9999999))
		vd_o = "{0}\\story\\media\\{1}.mp4".format(self.path, vid_nameSpace[2])

		# Conversione
		self.tools.videoConverter(vd_i, vd_o)
		# Rinominazione File
		self.tools.rinomina(vd_o, vd_o[:-4]+".mpeg"); vd_o = vd_o[:-4]+".mpeg"

		inf_in_orByte = self.tools.videoInfo(vd_i)['size']
		inf_out = self.tools.videoInfo(vd_o)

		# CREAZIONE STRUTTURA XML
		g = ( vid_nameSpace[0], "{0}123".format(vid_nameSpace[0][:-3]) )
		xml = self.prefabs.mediaVideo( g, vd_i, inf_out['size'], inf_in_orByte)

		# INSERIMENTO XML VIDEO STRUCT NELLA LISTA MEDIA DELLO STORY
		# part 1
		mediaG = self.add_media('video', vd_i, xml, nick)
		media = self.get_media(mediaG)
		extInf = {
			'ansG':vid_nameSpace[1], 'target':vid_nameSpace[2], 'id':vid_nameSpace[3], 
			'time':inf_out['duration'], 'size':(inf_out['width'], inf_out['height'])
		}
		media.add_extraInfo( extInf )
		# part 2
		mediaList = None
		if self.f_xml.find('assetLst') is not None:
			mediaList = self.f_xml.find('assetLst').find('mediaLst') # From theme.xml
		else:
			mediaList = self.f_xml.find('mediaLst').find('mediaLst') # From story.xml
		mediaList.append(xml)

		return g[0] # Retun of Asset

	def print_rels (self):
		whatNotShow = ('viewProps','defaultStyles','playerProps')
		for rel in self.l_rels:
			if rel[2] not in whatNotShow: # 2 = Type
				print rel

class SlObj_AssetObj (SlObj_FixedObj):
	def __init__ (self, nome, g, xml):
		super(SlObj_AssetObj, self).__init__(g, xml)
		self.nome = nome

# [! [! [! [! [! [! [! [! [! [! [! [! [! [! [!] !] !] !] !] !] !] !] !] !] !] !] !] !] !] #

class SlObj_ShapeObj (SlObj_TimelineObj):
	def __init__ (	self, g, xml,
					pos=(100, 100), size=(100, 100), timing=(0, 5000, False, False), zindex=None, moreInfo=None):

		super(SlObj_ShapeObj, self).__init__(g, xml, timing=timing, moreInfo=moreInfo)
		
		self.pos = pos
		self.size = size

		loc = self.prefabs.posizione(pos, size)
		self.f_xml.append( loc )

	def realloc (self):
		loc = self.f_xml.find('loc')
		loc.attrib['l'] = str( self.pos[0] )
		loc.attrib['t'] = str( self.pos[1] )
		loc.attrib['r'] = str( self.pos[0] + self.size[0] )
		loc.attrib['b'] = str( self.pos[1] + self.size[1])
	def resize (self, w, h):
		self.size = (w, h); self.realloc()
	def scale (self, perCent_w, perCent_h):
		w = (float(self.size[0])/100.00)*float(perCent_w)
		h = (float(self.size[1])/100.00)*float(perCent_h)
		self.size = (int(w), int(h)); self.realloc()
	def cord (self, x, y):
		self.pos = (x, y); self.realloc()

	def set_parentG (self, gid):
		self.f_xml.attrib['parentG'] = gid

	def zIndex(self, z):
		self.f_xml.attrib['zOrder'] = str(z)

	def fadeIn(self, dur=25, direz='none'):
		self.f_xml.find('animEffect').append( self.prefabs.fadeIn(dur, direz) )
	def fadeOut(self, dur=25, direz='none'):
		self.f_xml.find('animEffect').append( self.prefabs.fadeOut(dur, direz) )

class Sl_text (SlObj_ShapeObj):
	def __init__ (self, nome, text, stileFont=['Ruda', '16', '#A6412B', True, False], xml=None, _PADRE=None):
		par_g = 'text'; tag_xml = xml

		text = text # CONVERSIONE TEXT CON CHAR ADATTO
		self._PADRE = None
		if _PADRE != None:
			self._PADRE = _PADRE

		self.l_state = []

		if tag_xml is None:
			tag_xml = self.prefabs.textBox(nome, text)

		super(Sl_text, self).__init__(par_g, tag_xml, moreInfo='text')

		self.tagText = None; self.tagText_str = None
		self.tagFtmText = None; self.tagFtmText_str = None

		self.tagText = self.prefabs.textBox_tagText(text, stileFont[0], stileFont[1], stileFont[2], stileFont[3], stileFont[4] );
		self.tagFtmText = self.prefabs.textBox_tagFtmText(text, stileFont[0], stileFont[1], stileFont[3], stileFont[4] );

		self.tagText_str = self.tools.xmltoTextedXml( self.tagText )
		self.tagFtmText_str = self.tools.xmltoTextedXml( self.tagFtmText )

		self.f_xml.find('text').text = self.tagText_str
		self.f_xml.find('fmtText').text = self.tagFtmText_str

	def add_state (self, nome):
		sta = Sl_State(nome, self._PADRE)
		self.l_state.append( sta )
		self.f_xml.find('stateLst').append(sta.f_xml)
		return sta

	def margin (self, l, t, r, b):
		textMargin = self.f_xml.find('textMargin')
		textMargin.attrib['l'] = str( l )
		textMargin.attrib['t'] = str( t )
		textMargin.attrib['r'] = str( r )
		textMargin.attrib['b'] = str( b )

class Sl_group (SlObj_ShapeObj):
	def __init__ (self, nome, childs, xml=None):
		par_g = 'group'; tag_xml = None

		if xml is None: # pic (self, nome, gids, assetG, effect=(1,0))
			tag_xml = self.prefabs.group(nome)
		else:
			tag_xml = xml

		super(Sl_group, self).__init__(par_g, tag_xml)

		self.childLst = self.f_xml.find('childLst')
		self.l_child = []
		self.area = [270, 360, 270, 360]

		'''#area = self.calcAreaGroup();
		print childs[0]
		loc = childs[0].f_xml.find('loc').attrib
		self.area = [loc['t'], loc['l'], loc['b'], loc['r']]
		st = 0; dur = 0; indx = 0'''

		for child in childs:
			self.addChild( child )
			'''# EREDE
			child.set_parentG( self.g )
			child.zIndex(indx); indx += 1
			childLst.append( self.prefabs.childGroup(child.g) )

			self.l_child.append( child.g )

			# CALCOLO AREA DEL GRUPPO
			loc = child.f_xml.find('loc').attrib
			area = self.calcAreaGroup(area, [loc['t'], loc['l'], loc['b'], loc['r']])

			# CALOLO TIMING AREA
			if (child.startTime + child.duration) > (st + dur):
				st = child.startTime; dur = child.duration'''

	def addChild (self, child):
		st = 0; dur = 0; 
		indx = len(self.l_child)

		# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- # 

		child.set_parentG( self.g );
		child.zIndex(indx);
		
		self.childLst.append( self.prefabs.childGroup(child.g) )
		self.l_child.append( child.g )

		# CALCOLO AREA DEL GRUPPO
		loc = child.f_xml.find('loc').attrib
		self.area = self.calcAreaGroup(self.area, [loc['t'], loc['l'], loc['b'], loc['r']])

		# CALOLO TIMING AREA
		if (child.startTime + child.duration) > (st + dur):
			st = child.startTime; dur = child.duration

		# RE-SIZE, RE-POSITION, RE-TIMING
		t = self.area[0]; l = self.area[1]
		b = self.area[2]; r = self.area[3]
		self.area = [ t, l, (r-l), (b-t) ]
		self.cord(self.area[1], self.area[0])
		self.resize(self.area[2], self.area[3])
		self.retiming( st, dur )

	def calcAreaGroup (self, area=[9999,9999,0,0], newArea=[0,0,0,0]):
		for i in range(4):
			area[i] = int( area[i] ); newArea[i] = int( newArea[i] )

		if (newArea[0] < area[0]): area[0] = newArea[0]
		if (newArea[1] < area[1]): area[1] = newArea[1]
		if (newArea[2] > area[2]): area[2] = newArea[2]
		if (newArea[3] > area[3]): area[3] = newArea[3]

		t = area[0]; l = area[1]
		b = area[2]; r = area[3]

		areaRis = [ t, l, b, r ]
		return areaRis

class Sl_scrollBox (Sl_group):
	def __init__ (self, nome, childs=[], xml=None):
		par_g = 'group'; tag_xml = None

		if xml is None: # pic (self, nome, gids, assetG, effect=(1,0))
			tag_xml = self.prefabs.scrollBox(nome)

		super(Sl_scrollBox, self).__init__(par_g, [], tag_xml)

class Sl_jobstop (Sl_group):
	def __init__ (self, tipo, titleBoxG, incG, corG, childs=[], xml=None):
		par_g = 'quiz'; tag_xml = None

		if xml is None: # pic (self, nome, gids, assetG, effect=(1,0))
			tag_xml = self.prefabs.jobstop(tipo, titleBoxG, incG, corG)

		super(Sl_jobstop, self).__init__(par_g, [], tag_xml)

class Sl_pic (SlObj_ShapeObj):
	def __init__ (self, nome, assetG, relInf, time, pos, size, xml=None):
		par_g = 'media'
		tag_xml = None

		if xml is None: # pic (self, nome, gids, assetG, effect=(1,0))
			tag_xml = self.prefabs.pic(nome, None, assetG)
		else:
			tag_xml = xml
			pos = None		#
			size = None		#
			time = None		# DEVO PRENDERE QUESTE INFO DALLA STRUTTURA XML GIA' COMPLETA

		# SUPER CALL
		super(Sl_pic, self).__init__(par_g, tag_xml, pos, size, timing=time)
		self.nome = nome

		self.f_rel = self.prefabs.relationship("media", "/story/media/{0}.png".format(relInf[0]), relInf[1]) # 0:Target, 1:Info

class Sl_video (SlObj_ShapeObj):
	def __init__ (self, nome, assetG, infG, relInf, time, pos, size, xml=None):
		par_g = 'media'
		tag_xml = None

		if xml is None:
			tag_xml = self.prefabs.video(nome, None, assetG, infG[1])
		else:
			tag_xml = xml
			pos = None		#
			size = None		#
			time = None		# DEVO PRENDERE QUESTE INFO DALLA STRUTTURA XML GIA' COMPLETA

		# SUPER CALL
		super(Sl_video, self).__init__(par_g, tag_xml, pos, size, timing=time, zindex=1, moreInfo='video')
		self.nome = nome

		# Video MODIFICA TAG SPECIFICA
		tag_movie = tag_sz = None
		tag_movie = self.f_xml.find('movie')
		tag_movie.attrib['dur'] = str( time[1] )
		tag_sz = tag_movie.find('sz')
		tag_sz.attrib['w'] = str( size[0] )
		tag_sz.attrib['h'] = str( size[1] )

		# Creo la struttura del rel, che insieme alla struttura xml, una volta ritornata la funzione
		# saranno posizionati dentro ai file .xml
		self.f_rel = self.prefabs.relationship("media", "/story/media/{0}.mpeg".format(relInf[0]), relInf[1]) # 0:Target, 1:Info

	def playOnTrig (self):
		self.f_xml.attrib['play'] = 'trig'

class Sl_SlideObj (SlObj_TimelineObj):
	def __init__ (self, g, _PADRE, layout, xml, rel=None, timing=None):

		self._PADRE = _PADRE

		f_xml = self.tools.xmlGetRoot(xml)
		f_rel = None
		if rel is not None:
			f_rel = self.tools.xmlGetRoot(rel)

		super(Sl_SlideObj, self).__init__(g, f_xml, f_rel, timing=timing)

		# ALL LISTs
		self.l_video = [] # SHAPE LISTs
		self.l_audio = []
		self.l_pic = []
		self.l_text = []
		self.l_shape = []
		self.l_group = []
		self.l_layer = []

		shapeLst = self.f_xml.find('shapeLst')
		for shp in shapeLst.iter('video'):
			self.l_video.append( shp )
		for shp in shapeLst.iter('sound'):
			self.l_audio.append( shp )
		for shp in shapeLst.iter('pic'):
			self.l_pic.append( shp )
		for shp in shapeLst.iter('textBox'):
			self.l_text.append( shp )

		for shp in shapeLst.iter('shape'):
			self.l_shape.append( shp )
		for shp in shapeLst.iter('line'):
			self.l_shape.append( shp )

		trigLst = self.f_xml.find('trigLst')
		for trig in trigLst.iter('trig'):
			self.l_trig.append( trig )

	def set_titolo (self, tit):
		self.f_xml.attrib['name'] = tit

	def add_video (self, g):
		pass
	def add_pic (self, g):
		pass
	def add_audio (self, g):
		pass

	def calc_total_time (self):
		pass

	def elementOnSlide (self):
		return 1

	def insert_video (self, f, nick=None, pos=(100,100)):
		# print "inserting video {0}".format(nick)

		# Importazione Video ---> SlObj_AssetObj
		gid = self._PADRE._PADRE.importVideo(f, nick)

		# Inserimento Vd in Slide ---> SlObj_ShapeObj
		vidM = self._PADRE._PADRE.get_media(gid)
		# Sl_video (self, nome, assetG, infG, relInf, time, pos, size, xml=None)
		# def setTiming (self, startTime, duration, shw_tilEnd=False, shw_always=False):
		vid = Sl_video(vidM.nome, vidM.g, (None, vidM.info['ansG']), (vidM.info['target'],vidM.info['id']),
				(0,vidM.info['time'],False,False), pos, (vidM.info['size'][0],vidM.info['size'][1]) )
		# print (100,100), (vidM.info['size'][0],vidM.info['size'][1])
		self.l_video.append( vid )

		# AGGIUNTA STRUTTURE AI RISPETTIVI FILE
		self.f_xml.find('shapeLst').append( vid.f_xml )
		self.f_rel.insert(0, vid.f_rel)
		return vid

	def insert_pic (self, f, nick=None, pos=(100,100)):
		asset = None
		wherePutPhoto = None

		# if type(self._PADRE._PADRE) is StoryLineObj:
		if StoryLineObj in type(self._PADRE._PADRE).__mro__:
			wherePutPhoto = self._PADRE._PADRE
		else:
			wherePutPhoto = self._PADRE._PADRE._PADRE

		asset = wherePutPhoto.get_media_byPath(self.tools.path_assoluto(f))

		onePHOTO = False
		if asset is None:
			gid = wherePutPhoto.importPic(f, nick)
			onePHOTO = True
		else:
			gid = asset.g
			#print "IMG GID: {0}".format(gid)

		picM = wherePutPhoto.get_media(gid)
		pic = Sl_pic( picM.nome, picM.g, (picM.info['target'],picM.info['id']),
			(0,5000,False,False), pos, (picM.info['size'][0],picM.info['size'][1]))
		self.l_pic.append( pic )

		# AGGIUNTA STRUTTURE AI RISPETTIVI FILE
		self.f_xml.find('shapeLst').append( pic.f_xml );
		if onePHOTO:
			if self.f_rel is not None:
				self.f_rel.insert(0, pic.f_rel)
			elif self.f_rel is None:
				self._PADRE.f_rel.insert(0, pic.f_rel)

		return pic

	def formGroup (self, nome, childs=[]):
		group = Sl_group(nome, childs)
		self.f_xml.find('shapeLst').append( group.f_xml )
		return group

	def insert_scrollBox (self, nome, childs=[]):
		group = Sl_scrollBox(nome, childs)
		self.f_xml.find('shapeLst').append( group.f_xml )
		return group

	def insert_text (self, nome, testo, impostazioni, _PADRE=None):
		text = Sl_text(nome, testo, impostazioni, _PADRE=_PADRE)
		self.f_xml.find('shapeLst').append( text.f_xml )
		return text

	def insert_layer (self, nome, layout='01dfe22b-2e1c-4dc9-a514-a7d3f1ab7177'):
		ly = Sl_Layer(nome, layout=layout)
		self.l_layer.append(ly)
		
		if self.f_xml.find('sldLayerLst') is None:
			self.f_xml.append( self.prefabs.sldLayerLst() )

		self.f_xml.find('sldLayerLst').append( ly.f_xml )
		return ly

# ###################################################################### #
# #### LIVELLO 3 ####################################################### #
# ###################################################################### # FINE








# ###################################################################### #
# #### LIVELLO 4 ####################################################### #
# ###################################################################### #

# [| [| [| [| [| (| -= SlObj_TimelineObj =- |) |] |] |] |] |] #
# [! [! [! [! [! [! [! [! [! [! [! [! [! [! [!] !] !] !] !] !] !] !] !] !] !] !] !] !] !] #
class Sl_Layer (Sl_SlideObj):
	def __init__ (self, nome, _PADRE=None, layout='01dfe22b-2e1c-4dc9-a514-a7d3f1ab7177', xml=None, timing=None):

		str_xml = None
		if xml is None:
			str_xml = self.prefabs.layer(nome)

		tag_xml = self.tools.xmlOpen('asset\\prefabs\\empty.xml')
		tag_xml._setroot(str_xml)
		super(Sl_Layer, self).__init__('altro', _PADRE, layout, tag_xml, timing=(0, 5000, False, False))

		self.f_xml.attrib['layoutG'] = layout
		self.layout = self.f_xml.attrib['layoutG']

class Sl_State (Sl_SlideObj):
	def __init__ (self, nome, _PADRE):
		par_g = 'state'
		str_xml = self.prefabs.state(nome, _PADRE.g)

		tag_xml = self.tools.xmlOpen('asset\\prefabs\\empty.xml')
		tag_xml._setroot(str_xml)
		super(Sl_State, self).__init__(par_g, _PADRE, None, tag_xml, timing=(0, 5000, False, False))

class SlObj_FileObj (Sl_SlideObj):
	def __init__ (self, path_xml, path_rel, _PADRE, layout, gids=None):

		# print path_xml, path_rel
		xmlStcr_xml = t.xmlOpen(path_xml)
		xmlStcr_rel = t.xmlOpen(path_rel)

		super(SlObj_FileObj, self).__init__(gids, _PADRE, layout, xmlStcr_xml, xmlStcr_rel)
		
		self.xml = xmlStcr_xml
		self.rel = xmlStcr_rel
		self.path_xml = path_xml
		self.path_rel = path_rel

		self.nome = self.f_xml.attrib['name']

	def create (self):
		pass
	def open (self):
		pass
	def save (self):
		pass
	
	def add_layer(self):
		pass

class Sl_QuestBank (SlObj_FileObj):
	def __init__ (self, nome, fileName, layout, bankG, gids=None, _PADRE=None):

		path = _PADRE._PADRE.path
		path_xml = "{0}{1}".format(path, fileName)
		path_rel = "{0}/story/slides/_rels/{1}.rels".format(path, fileName[14:])

		super(Sl_QuestBank, self).__init__(path_xml, path_rel, _PADRE, layout, gids)

		print self.g, self.verG
		self.f_xml.attrib['name'] = nome
		self.f_xml.attrib['layoutG'] = layout
		self.f_xml.attrib['bankG'] = bankG

		self.nome = self.f_xml.attrib['name']
		self.layout = self.f_xml.attrib['layoutG']

	def save (self):
		print u"saving Bank {0}".format(self.nome)
		self.tools.xmlClose(self.xml, self.path_xml)
		self.tools.xmlClose(self.rel, self.path_rel, isRels=True)

class Sl_Slide (SlObj_FileObj):
	def __init__ (self, nome, _PADRE, fileName, layout, gids=None):

		path = _PADRE._PADRE.path
		path_xml = "{0}{1}".format(path, fileName)
		path_rel = "{0}/story/slides/_rels/{1}.rels".format(path, fileName[14:])

		super(Sl_Slide, self).__init__(path_xml, path_rel, _PADRE, layout, gids)
		
		if nome is not None:
			self.f_xml.attrib['name'] = nome
		if layout is not None:
			self.f_xml.attrib['layoutG'] = layout

		self.nome = self.f_xml.attrib['name']
		self.layout = self.f_xml.attrib['layoutG']
		self.navDt = self.f_xml.find('navData')

	def navData (self, prev, next, submit):
		self.navDt.attrib['prev'] = str(prev).lower()
		self.navDt.attrib['next'] = str(next).lower()
		self.navDt.attrib['submit'] = str(submit).lower()

	def update (self):
		# UPDATE TIME! Here! #
		t = 5000
		for vid in self.l_video:
			#print type(vid.startTime), type(vid.duration)
			if (vid.startTime+vid.duration) > t:
				t = (vid.startTime+vid.duration)
		for pic in self.l_pic:
			if (pic.startTime+pic.duration) > t:
				t = (pic.startTime+pic.duration)
		self.f_xml.find('tmProps').attrib['min'] = str( t )

	def save (self):
		print u"saving Slide {0}".format(self.nome)

		self.update()
		''' self.update() tolto per fastLinking_promotoriFinanziari.py'''

		self.tools.xmlClose(self.xml, self.path_xml)
		self.tools.xmlClose(self.rel, self.path_rel, isRels=True)

	def make_jobstop (self, tipo, quest, laylay):
		print "{0} BECOMES JOBSTOP".format(self.nome)

		shpList = self.f_xml.find('shapeLst')
		self.f_xml.attrib['resetMode'] = 'n' # NEVER RESUME

		self.navData(False, False, True)
		titleBox = self.insert_text( 'domanda', quest['domanda'], ['Cabin', '16', '#C54B12', False, False] )
		titleBox.cord(36, 106); titleBox.resize(648, 82)

		# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/* #
		# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/* # LAYER
		layNeg = laylay[1]; layPos = laylay[0]
		ly_sucs = self.insert_layer('Success', layPos[0])

		trg = Sl_TrigObj( "", layPos[1]); trg.act_hideLayer(ly_sucs.g, me=True);
		trg.evt_chngVar(self._PADRE._PADRE.get_var('pageNext').g)
		ly_sucs.addTrig(trg)
		trg = Sl_TrigObj( "", layPos[1]); trg.act_jumpToNext();
		trg.evt_chngVar(self._PADRE._PADRE.get_var('pageNext').g)

		ly_sucs.addTrig(trg)
		# -=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=- #

		ly_fail = self.insert_layer('Failure', layNeg[0])

		trg = Sl_TrigObj( "", layNeg[1]); trg.act_hideLayer(ly_fail.g, me=True);
		trg.evt_chngVar(self._PADRE._PADRE.get_var('pagePrev').g)
		ly_fail.addTrig(trg)
		trg = Sl_TrigObj( "", layNeg[1]); trg.act_jumpToNext(); 
		trg.evt_chngVar(self._PADRE._PADRE.get_var('pagePrev').g)

		ly_fail.addTrig(trg)
		# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/* #
		# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/* #

		jb = Sl_jobstop(tipo, titleBox.g, ly_fail.g, ly_sucs.g)

		stileTesto=['Cabin', '12', '#808080', False, False]; i = 0
		for key, value in quest.iteritems():
			
			if key == 'domanda':
				continue

			rat = None
			if key == 'g':
				r = self.prefabs.ratio('risp', value, stile='jobstop_radio.xml', stileTesto=stileTesto, initState='Selected')
				rat = SlObj_ShapeObj( 'text', r, pos=(0,70), size=(720, 34), timing=(0, 5000, False, True))
				rat.cord(40, 187+(50*i)); rat.resize(648, 46)
				shpList.append(rat.f_xml)
			else:
				r = self.prefabs.ratio('risp', value, stile='jobstop_radio.xml', stileTesto=stileTesto, initState='Normal')
				rat = SlObj_ShapeObj( 'text', r, pos=(0,70), size=(720, 34), timing=(0, 5000, False, True))
				rat.cord(40, 187+(50*i)); rat.resize(648, 46)
				shpList.append(rat.f_xml)
			i += 1

			if tipo == 'VF':
				rat.f_xml.attrib['grpId'] = 'True/False'
				rat.f_xml.find('propBag').find('prop').find('val').find('str').text = 'True/False'
			elif tipo == 'MC':
				rat.f_xml.attrib['grpId'] = 'Multiple Choice'
				rat.f_xml.find('propBag').find('prop').find('val').find('str').text = 'Multiple Choice'

			jb.addChild( rat )

		# Trigger interation SUBMIT
		trg_submit = Sl_TrigObj( "", self.g )
		trg_submit.act_sbmtInteraction(jb.g)
		trg_submit.evt_onClick('submit')
		self.addTrig(trg_submit)

		shpList.append(jb.f_xml)

	def make_resultSlide (self, laylay, passScore=60, isFIN=False):
		print "{0} BECOMES RESULT SLIDE".format(self.nome)

		stry = self._PADRE._PADRE

		nome = "Results{0}"
		if stry.popCount == 0:
			nome = nome.format('')
		else:
			nome = nome.format(stry.popCount)

		v1 = stry.new_var('{0}.ScorePercent'.format(nome), 0)
		v2 = stry.new_var('{0}.ScorePoints'.format(nome), 0)
		v3 = stry.new_var('{0}.PassPoints'.format(nome), 0)
		v4 = stry.new_var('{0}.PassPercent'.format(nome), 0)

		v1.makeProb(stry.popCount)
		v2.makeProb(stry.popCount)
		v3.makeProb(stry.popCount)
		v4.makeProb(stry.popCount)

		qtag = self.prefabs.quiz_tag(nome, (v1.g, v2.g, v3.g, v4.g), self.g, passScore=passScore)
		stry.f_xml.find('quizMgr').find('quizLst').append( qtag )

		# self.tools.xmlShowBranch( qtag )

		stry.popCount += 1
		
		# -=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=- # 
		# -=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=- #

		sucs = ('00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-000000000000')
		fail = ('00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-000000000000')
		guids = ('00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-000000000000')

		self.f_xml.attrib['resetMode'] = 'n'
		shpList = self.f_xml.find('shapeLst')

		if isFIN is False:
			layNeg = laylay[1]; layPos = laylay[0]
			# SUCS
			ly_sucs = self.insert_layer('Success', layPos)

			trg_sucs = Sl_TrigObj( "", self.g )
			trg_sucs.act_showLayer(ly_sucs.g)
			trg_sucs.evt_onTmLnStart()
			trg_sucs.condition([v2.g], ">=", [v3.g])
			self.addTrig(trg_sucs)

			sucs = (trg_sucs.g, ly_sucs.g)

			# FAIL
			ly_fail = self.insert_layer('Failure', layNeg)

			trg_fail = Sl_TrigObj( "", self.g )
			trg_fail.act_showLayer(ly_fail.g)
			trg_fail.evt_onTmLnStart()
			trg_fail.condition([v2.g], "<", [v3.g])
			self.addTrig(trg_fail)

			fail = (trg_fail.g, ly_fail.g)

			# GUIDS
			txt1 = self.insert_text( v1.nome, '%{0}%%'.format(v1.nome), ['Arial', '16', '#808080', False, False])
			txt1.cord(395, 167); txt1.resize(290, 30); txt1.margin(0,0,0,0)
			txt2 = self.insert_text( v4.nome, '%{0}%%'.format(v4.nome), ['Arial', '16', '#808080', False, False])
			txt2.cord(395, 221); txt2.resize(290, 30); txt2.margin(0,0,0,0)
			guids = (txt1.g, txt2.g)

		# def rsltsIntr (self, quizG, sucs, fail, guids):
		rsltsIntr = self.prefabs.rsltsIntr(qtag.attrib['g'], sucs, fail, guids)
		rsltsIntr = SlObj_TimelineObj(None, rsltsIntr, timing=(0, 5000, False, False))
		shpList.append(rsltsIntr.f_xml)

		trg_submit = Sl_TrigObj( "", self.g )
		trg_submit.act_submitQuiz(self.g)
		trg_submit.evt_onTmLnStart()
		self.addTrig(trg_submit)

class Sl_JbCover (Sl_Slide):
	def __init__ (self, nome, _PADRE, fileName, layout, gids=None):
		super(Sl_JbCover, self).__init__(nome, _PADRE, fileName, layout, gids)

class Sl_ResSlide (Sl_Slide):
	def __init__ (self, nome, _PADRE, fileName, layout, gids=None):
		super(Sl_ResSlide, self).__init__(nome, _PADRE, fileName, layout, gids)

class Sl_JBSlide (Sl_Slide):
	def __init__ (self, nome, _PADRE, fileName, layout, gids=None):
		super(Sl_JBSlide, self).__init__(nome, _PADRE, fileName, layout, gids)

# [| [| [| [| [| (| -= SlObj_FixedObj =- |) |] |] |] |] |] #
# [! [! [! [! [! [! [! [! [! [! [! [! [! [! [!] !] !] !] !] !] !] !] !] !] !] !] !] !] !] #
class Sl_TrigObj (SlObj_AssetObj):
	def __init__ (self, nome, copiedG=None, xml=None):
		par_g = None
		tag_xml = None

		if xml is not None:
			tag_xml = xml
		else:
			tag_xml = self.prefabs.trigger_base(copiedG)

		super(Sl_TrigObj, self).__init__(nome, None, tag_xml)
		self.data = self.f_xml.find('data')
		self.condLst = self.f_xml.find('condLst')

	# ================ ACTIONs ================ #
	def action (self, act):
		pass
	def act_jumpToSlide (self, toG):
		tagData = self.data
		tagData.attrib['action'] = 'jumpToSlide'
		tagData.attrib['actSubType'] = 'spec'

		tagSlide = tagData.find('slide')
		tagSlide.attrib['jumpG'] = toG
	def act_jumpToNext (self):
		tagData = self.data
		tagData.attrib['action'] = 'jumpToSlide'
		tagData.attrib['actSubType'] = 'next'

	def act_playMedia (self, mediaG, mediaType='video'):
		tagData = self.data
		tagData.attrib['action'] = 'playMedia'
		tagData.attrib['actSubType'] = mediaType

		tagVideo = tagData.find('video')
		tagVideo.attrib['playG'] = mediaG
	def act_setVar (self, varG, val, opp='ass'):
		tagData = self.data
		tagData.attrib['action'] = 'adjustVar'
		tagData.attrib['actSubType'] = 'next'

		otherVideo = tagData.find('other')
		otherVideo.attrib['varG'] = varG
		otherVideo.attrib['op'] = opp
		otherVideo.attrib['dblVal'] = str(val)

	def act_exeJS (self, javascript):
		tagData = self.data
		tagData.attrib['action'] = 'executeJavaScript'
		tagData.attrib['actSubType'] = 'next'

		other = tagData.find('other')
		other.attrib['js'] = javascript

	def act_chngState (self, setStateG, stateName):
		tagData = self.data
		tagData.attrib['action'] = 'changeShapeState'
		tagData.attrib['actSubType'] = 'next'
		tagShape = tagData.find('shape')
		tagShape.attrib['setStateG'] = setStateG
		tagShape.attrib['setStateName'] = stateName

	def act_downloadFile (self, fileName): # jumpToFileUrl
		tagData = self.data
		tagData.attrib['action'] = 'jumpToFileUrl'
		tagData.attrib['actSubType'] = 'next'
		tagOther = tagData.find('other')
		tagOther.attrib['open'] = fileName

	def act_showLayer(self, layerG, me=False):
		tagData = self.data
		tagData.attrib['action'] = 'showSubSlide'
		tagData.attrib['actSubType'] = 'next'
		tagOther = tagData.find('sldLayer')
		tagOther.attrib['showG'] = layerG
	def act_hideLayer(self, layerG, me=False):
		tagData = self.data
		tagData.attrib['action'] = 'hideSubSlide'
		if me is True:
			tagData.attrib['actSubType'] = 'me'
		else:
			tagData.attrib['actSubType'] = 'next'
		tagOther = tagData.find('sldLayer')
		tagOther.attrib['hideG'] = layerG

	def act_submitQuiz(self, resG):
		tagData = self.data
		tagData.attrib['action'] = 'SubmitQuizSL'
		tagData.attrib['actSubType'] = 'next'
		cD = {'enumName':'SubmitQuizSL', 'data':'', 'bool':'false', 'g':resG}
		tagData.append( self.prefabs.customData(cD) )

	def act_resetQuiz(self, resG):
		tagData = self.data
		tagData.attrib['action'] = 'ResetQuizSL'
		tagData.attrib['actSubType'] = 'next'
		cD = {'enumName':'ResetQuizSL', 'data':'', 'bool':'false', 'g':resG}
		tagData.append( self.prefabs.customData(cD) )

	def act_sbmtInteraction(self, submitG):
		tagData = self.data
		tagData.attrib['action'] = 'submitInteraction'
		tagData.attrib['actSubType'] = 'next'
		tagIntr = tagData.find('interaction')
		tagIntr.attrib['submitG'] = submitG

	# ================ EVENTs ================ #
	def event (self, evt):
		pass
	def evt_onClick (self, clickedObj=None):
		tagData = self.data

		if clickedObj == "next":
			self.f_xml.attrib['name'] = 'Navigation'
			self.f_xml.attrib['group'] = 'next'
			self.f_xml.attrib['edit'] = 'variablename, subslides, keypresskeys, actions, operators, variablevalue, variableoperators'
			tagData.attrib['event'] = 'OnNextButtonClick'
			tagData.find('frame').attrib['actionG'] = "0ec0db78-2e1d-4919-bde6-6824587f77c4"
			tagData.find('frame').attrib['restore'] = "true"

		elif clickedObj == "prev":
			self.f_xml.attrib['name'] = 'Previous'
			tagData.attrib['event'] = 'OnClick'
			self.f_xml.attrib['edit'] = 'variablename, subslides, keypresskeys, actions, operators, variablevalue, variableoperators'
			tagData.find('frame').attrib['actionG'] = "ae475cc5-601c-414e-82c1-df8dc7d39471"
			tagData.find('frame').attrib['restore'] = "true"

		elif clickedObj == "submit":
			self.f_xml.attrib['name'] = 'SubmitInteraction'
			tagData.attrib['event'] = 'OnClick'
			self.f_xml.attrib['group'] = 'next'
			self.f_xml.attrib['type'] = 'internalEdit'
			tagData.find('frame').attrib['actionG'] = "ded656e9-96d2-4bb0-825c-2290fa8c4a2b"
			tagData.find('frame').attrib['restore'] = "true"

		else:
			tagData.attrib['event'] = 'OnClick'
	def evt_onTmLnStart (self):
		tagData = self.data
		tagData.attrib['event'] = 'OnStart'
	def evt_onTmLnEnd (self):
		tagData = self.data
		tagData.attrib['event'] = 'OnEnd'
	def evt_chngVar (self, varG):
		tagData = self.data
		tagData.attrib['event'] = 'OnVariableValueChange'
		tagData.find('other').attrib['varChangeG'] = varG

	# ================ CONDITIONs ================ #
	conds = {"==":"eq", "-==":"eqIgnore", "<":"lt", "<=":"lte", ">":"gt", ">=":"gte"}
	def condition (self, lValue, cond, rValue, andOr='and'):
		tag_cond = self.prefabs.trigCond(self.conds[cond], andOr)

		# L VALUE
		if type(lValue) is list:
			tag_cond.attrib['varG'] = str(lValue[0])

		elif type(lValue) in (int, float):
			tag_cond.attrib['floatVal1'] = str(lValue)
		elif type(lValue) is str:
			tag_cond.attrib['strVal1'] = str(lValue)
		# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- #
		# R VALUE
		if type(rValue) is list:
			tag_cond.attrib['varG2'] = str(rValue[0])
			tag_cond.attrib['dataType'] = 'var'

			# SE E' UN GID ALLORA MODIFICARE TIPO DI VALORE DI CONFRONTO

		elif type(rValue) in (int, float):
			tag_cond.attrib['floatVal1'] = str(rValue)
			print "rValue: {0}".format(str(rValue))
		elif type(rValue) is str:
			tag_cond.attrib['strVal2'] = str(rValue)
		elif type(rValue) is bool:
			tag_cond.attrib['boolVal'] = str(rValue)

		self.condLst.append( tag_cond )

class Sl_VarObj (SlObj_AssetObj):
	def __init__ (self, nome, val, xml=None):
		par_g = None
		tag_xml = None

		if xml is not None:
			tag_xml = xml

		super(Sl_VarObj, self).__init__(nome, par_g, tag_xml) # _={ SUPER }=_

		self.nome = nome
		# self.val = val if type(val) is not str else float(val)
		self.val = val
		
	def set (self, val):
		if type(val) in (int, float, long):
			self.f_xml.attrib['val'] = str(val)
		elif type(val) in (str, unicode):
			self.f_xml.attrib['val'] = val
		elif type(val) is bool:
			self.f_xml.attrib['val'] = str(val)
		else:
			raise WbtE_varE_wrongVarType
		self.val = val

	def makeProb (self, popCount):
		nome = self.f_xml.attrib['name']

		propN = None

		if nome[-12:] == 'ScorePercent':
			propN = "_player.6X4NP{0:06}.$PercentScore"

		elif nome[-11:] == 'ScorePoints':
			propN = "_player.6X4NP{0:06}.$Score"

		elif nome[-10:] == 'PassPoints':
			propN = "_player.6X4NP{0:06}.$PassScore"

		elif nome[-11:] == 'PassPercent':
			propN = "_player.6X4NP{0:06}.$PassPercent"

		else:
			propN = "6X4NP{0:06}"

		propN = propN.format(popCount)

		self.f_xml.attrib['type'] = 'prop'
		self.f_xml.attrib['propPath'] = propN

class Sl_MediaObj (SlObj_AssetObj):
	def __init__ (self, tag, fileName, xml=None, nome=None):
		par_g = None; tag_xml = None

		if xml is not None:
			tag_xml = xml

		super(Sl_MediaObj, self).__init__(nome, par_g, tag_xml) # _={ SUPER }=_

		self.tag = tag
		self.fileName = fileName
	def add_extraInfo (self, extInf):
		self.info = extInf

class  Sl_SceneObj (SlObj_AssetObj):
	def __init__ (self, nome, _PADRE, xml=None):
		par_g = None; tag_xml = None

		if xml is not None:
			tag_xml = xml
		else:
			tag_xml = self.prefabs.scene(nome)
			
		super(Sl_SceneObj, self).__init__(nome, par_g, tag_xml) # _={ SUPER }=_

		self._PADRE = _PADRE  # LINK TO story obj
		self.l_slide = []

		# LISTA SLIDE # >>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>" #
		slideLst = self.f_xml.find('sldIdLst')
		for slide in slideLst.iter('sldId'):
			sldId = slide.text

			# fileName = ( self._PADRE.path, self._PADRE.get_slide_byId(sldId) )
			fileName = self._PADRE.get_slide_byId(sldId)
			# print "----> {0}".format(fileName)
			
			self.add_slide(fileName, self)
			
	def add_slide (self, fileName, _PADRE, nome=None, layout=None, gids=None):
		# __init__ (self, nome, _PADRE, fileName, layout=None, gids=None)
		slide = Sl_Slide(nome, _PADRE, fileName, layout, gids)
		self.l_slide.append( slide )
		return slide
	def add_jbCover (self, fileName, _PADRE, nome=None, layout=None, gids=None):
		# __init__ (self, nome, _PADRE, fileName, layout=None, gids=None)
		slide = Sl_JbCover(nome, _PADRE, fileName, layout, gids)
		self.l_slide.append( slide )
		return slide
	def add_ResSlide (self, fileName, _PADRE, nome=None, layout=None, gids=None):
		# __init__ (self, nome, _PADRE, fileName, layout=None, gids=None)
		slide = Sl_ResSlide(nome, _PADRE, fileName, layout, gids)
		self.l_slide.append( slide )
		return slide
	def add_bank (self, fileName, _PADRE, nome=None, layout=None, gids=None):
		# __init__ (self, nome, _PADRE, fileName, layout=None, gids=None)
		slide = Sl_QuestBank(nome, fileName, layout, None, gids, _PADRE)
		self.l_slide.append( slide )
		return slide
	def add_JBSlide (self, fileName, _PADRE, nome=None, layout=None, gids=None):
		# def __init__ (self, nome, _PADRE, fileName, layout, gids=None):
		slide = Sl_JBSlide(nome, _PADRE, fileName, layout, gids)
		self.l_slide.append( slide )
		return slide

	def nameSpace_slide (self):
		l = self._PADRE.get_slideTotalNumber() +1
		nomeFile = "slide"
		if (l > 1): nomeFile += "{0:x}".format(l) # la prima slide si deve chiamare slide.xml
		names = ( "{0}.xml".format(nomeFile), "{0}.xml.rels".format(nomeFile), "R5{0:010x}".format(l).upper() )
		return names

	def new_slide (self, nome, layout='dbda9ab9-710c-4ce2-84f2-002cafd9bc89', sldBase='slide.xml'):
		names = self.nameSpace_slide()

		# CREAZIONE FILE DI SLIDE
		# modifica di nome, g, verG, layoutG
		self.tools.ctrlC_ctrlV_file("asset\\prefabs\\{0}".format(sldBase), "{0}/story/slides/{1}".format(self._PADRE.path, names[0]))
		self.tools.ctrlC_ctrlV_file("asset\\prefabs\\slide.xml.rels", "{0}/story/slides/_rels/{1}".format(self._PADRE.path, names[1]))
		self.tools.ctrlC_ctrlV_file("__slide masters__\\__immagini__\\R6hc6m9Xt0sL.jpg", "{0}/story/media/R6hc6m9Xt0sL.jpg".format(self._PADRE.path))

		# ADD SLIDE _ID IN story.xml.rels
		self._PADRE.add_slideLink(names[0], names[2])

		# ADD SLIDE _ID IN story.scene
		sldId = self.tools.xmlTag("sldId", {})
		sldId.text = names[2]
		self.f_xml.find('sldIdLst').append(sldId)

		# ADDING SLIDE TO ABSTRACT PYTHON OBJ
		sld = None
		if sldBase == 'slide.xml':
			sld = self.add_slide("/story/slides/{0}".format(names[0]), self, nome, layout, "slide")
		elif sldBase == 'bnkSlide.xml':
			sld = self.add_bank("/story/slides/{0}".format(names[0]), self, nome=nome, layout=layout, gids="slide")
		elif sldBase == 'jbCover.xml':
			sld = self.add_jbCover("/story/slides/{0}".format(names[0]), self, nome=nome, layout=layout, gids="slide")
		elif sldBase == 'ResSlide.xml':
			sld = self.add_ResSlide("/story/slides/{0}".format(names[0]), self, nome=nome, layout=layout, gids="slide")
		elif sldBase == 'JBSlide.xml':
			sld = self.add_JBSlide("/story/slides/{0}".format(names[0]), self, nome=nome, layout=layout, gids="slide")
		
		return sld

class Sl_ScnBnkObj (Sl_SceneObj):
	def __init__ (self, nome, _PADRE, xml=None):
		if xml is None:
			xml = self.prefabs.bnk_scene(nome)
		super(Sl_ScnBnkObj, self).__init__(nome, _PADRE, xml) # _={ SUPER }=_

class Sl_Story (SlObj_ProgObj):
	storyC = 0

	def __init__ (self, nome, layout):
		global t

		print "WORKING ON PROGECT {0}...".format(nome)

		gids = None
		if not t.dirExist(nome):
			t.ctrlC_ctrlV(layout, nome)
			# gids = 'story'

		# RICONOSCIMENTO DEL FILE SYSTEM DI PROGETTO
		'''chkDir = t.dir2(nome)
		print chkDir
		if "story" not in chkDir or "[Content_Types].xml" not in chkDir:
			raise "NON SI TRATTA DI UN FILE .STORY PROBABILMENTE"'''

		path_xml = "{0}/story/story.xml".format(nome)
		path_rel = "{0}/story/_rels/story.xml.rels".format(nome)
		# print nome
		# print path_xml
		# print path_rel
		# print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="

		xmlStcr_xml = t.xmlOpen(path_xml)
		xmlStcr_rel = t.xmlOpen(path_rel)

		# ### ### ### ### ### ### ### ### ### #

		super(Sl_Story, self).__init__(gids, xmlStcr_xml, xmlStcr_rel)
		self.path = nome
		self.nome = nome
		self.l_var = []
		self.popCount = 0
		self.l_media = []
		self.l_scene = []

		# LISTA VARIABILI # >>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>" # 
		varLst = self.f_xml.find('varLst')
		for var in varLst.iter('var'):
			if var.attrib['type'] == "user": # Non salva le variabili collegate (prop) ai risultati dei quiz
				nome = var.attrib['name']
				val = var.attrib['val']
				xml = var
				self.add_var(nome, val, xml)

			# elif var.attrib['type'] == "prop": pass'''

		# LISTA MEDIA # >>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>" #
		mediaLst = self.f_xml.find('mediaLst').find('mediaLst')
		for media in mediaLst.iter('media'):
			tag = media.tag
			fileName = media.attrib['origFile']
			xml = media
			self.add_media(tag, fileName, xml)
		for media in mediaLst.iter('video'):
			tag = media.tag; fileName = media.attrib['origFile']; xml = media
			self.add_media(tag, fileName, xml)
		for media in mediaLst.iter('audio'):
			tag = media.tag; fileName = media.attrib['origFile']; xml = media
			self.add_media(tag, fileName, xml)

		# LISTA SCENE # >>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>">>>" #
		sceneLst = self.f_xml.find('sceneLst')
		for scene in sceneLst.iter('scene'):
			nome = scene.attrib['name']
			xml = scene

			self.add_scene(nome, xml=xml)

		sldCount = 0 
		for scn in self.l_scene:
			for sld in scn.l_slide:
				sldCount += 1
		self.gidGen.set('slide', sldCount)

		varCount = 0 # [{) -=- The News -=- ()}]
		for var in self.l_var:
			varCount += 1
		self.gidGen.set('var', varCount)

		self.load_videoSpaceGIDs()
		self.load_picSpaceGIDs()

		self.storyC += 1

	def save (self, justStory=False):
		print "\n\n\n"
		print self.nome
		print "SAVING PROJECT # ######################################## {0}% #".format(self.tools.joke_loading(0, 99))
		self.tools.xmlClose(self.xml, "{0}/story/story.xml".format(self.path))
		self.tools.xmlClose(self.rel, "{0}/story/_rels/story.xml.rels".format(self.path), isRels=True)

		if justStory == False:
			for scn in self.l_scene:
				for sld in scn.l_slide:
					sld.save()

		print "SAVED PROJECT # ######################################## 100% #\n\n\n"

	def load_videoSpaceGIDs (self):
		self.inportedVd = 0
		videoCensimentoF = open('asset/prefabs/assetG_ansG_Target_Id.txt', 'r')
		self.censimentoVd = []
		for l in videoCensimentoF.xreadlines():
			self.censimentoVd.append( l.split() )
	def load_picSpaceGIDs (self):
		self.imprtPic = 0
		picCensimentoF = open('asset/prefabs/pic_censimento.txt', 'r')
		self.censimentoPic = []
		for l in picCensimentoF.xreadlines():
			self.censimentoPic.append( l.split() )
			
	def get_slide_byId (self, sldId):
		for rel in self.l_rels:
			if rel[0] == sldId:
				return rel[1]
				
	def get_slideTotalNumber(self):
		sldTotNum = 0
		for scn in self.l_scene:
			sldTotNum += len(scn.l_slide)
		return sldTotNum
		
	def add_slideLink (self, nome, _id):
		attrib = {	"Type":"slide", "Target":"/story/slides/{0}".format(nome), "Id":_id }
		relationship = self.tools.xmlTag("Relationship", attrib)
		self.f_rel.insert(self.get_slideTotalNumber(), relationship)
		
	def get_var (self, nome):
		for var in self.l_var:
			if var.nome == nome:
				return var

	def add_var (self, nome, val, xml=None):
		var = Sl_VarObj(nome, val, xml=xml)
		self.l_var.append( var )
		return var
	def new_var (self, nome, val, faf=None): # [{) -=- The News -=- ()}]
		'''for c in ['.', ',', '-']:
			if c in nome:
				raise WbtE_varE_badName'''

		tipo = None
		if type(val) in (int, float, long):
			tipo = 'num'
		elif type(val) in (str, unicode):
			tipo = 'text'
		elif type(val) is bool:
			tipo = 'bool'
		else:
			raise WbtE_varE_wrongVarType

		if faf is None:
			faf = self.gidGen.get('var')

		faf = self.gidGen.get('var')
		xml = self.prefabs.var(tipo, nome, val, faf)

		varList = self.f_xml.find('varLst')
		varList.append(xml)

		print u"added new var {0} of value {1}".format(nome, val)
		return self.add_var(nome, val, xml)

	def print_var (self):
		for var in self.l_var:
			s = "{0} ==> {1}: {2}\t\t\t{3}".format(var.g, var.nome, var.val, var.f_xml)
			print s

	'''def add_media (self, tag, fileName, xml=None, nick=""):
		return super(Sl_Story, self).add_media(tag, fileName, xml) '''

	def new_media (self, nome):
		pass
	def print_media (self):
		for media in self.l_media:
			s = "{0}: {1} \n{2} ==> {3} \n{4}\n".format(media.tag, media.fileName, media.g, media.f_xml, ("=-"*20+"="))
			print s

	def add_scene (self, nome, xml=None):
		scene = Sl_SceneObj(nome, self, xml=xml)
		self.l_scene.append( scene )
		if scene.g == self.verG: self.MainScene = scene # verG dello story.xml contiene il pG dello story
		return scene
	def new_scene (self, nome):
		scene = self.add_scene(nome, None)
		self.f_xml.find('sceneLst').append(scene.f_xml)
		return scene

	def add_questBank (self, nome, curScn):
		scn = Sl_ScnBnkObj(nome, self, None)
		self.f_xml.find('quizMgr').find('bankLst').append( scn.f_xml )
		self.l_scene.append( scn )
		
		sld = curScn.new_slide(nome, sldBase='bnkSlide.xml')
		sld.f_xml.attrib['bankG'] = scn.g
		return (scn, sld)

# ###################################################################### #
# #### LIVELLO 4 ####################################################### #
# ###################################################################### # FINE
















