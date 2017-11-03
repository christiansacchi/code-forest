# -*- coding: utf-8 -*-
import storyLineObj_plus
from storyLineObj_plus import Sl_Story, Sl_TrigObj, SlObj_ShapeObj, Sl_text
from tool import Tool

class WbtEVO (Sl_Story):
	masters = {
		"ubi":		"__slide masters__/ubi",
		"sara":		"__slide masters__/sara",
		"axa":		"__slide masters__/axa",
		"aviva":	"__slide masters__/aviva",
		"paper":	"__slide masters__/paper",
		"ObG": 		"__slide masters__/ObG",
		"ObUBI": 	"__slide masters__/ObUBI",
		"LAND":		"__slide masters__/LAND"
	}
	layouts = {
		"titolo":				"91807a5e-a461-47c8-bd45-00e1dd2b4b93",
		"titolo_custom":		"2e110db8-f69a-4bbb-ac30-bcd1151a532d",
		"cover":				"5441f67c-ca48-4e79-9195-96ed113cfe99",
		"cover_custom":			"dc276d19-9f1f-4e21-8466-97f33dd8bc8e",
		"copertina":			"65c01df3-6ce7-438c-9bdc-24d5485ca071",
		"copertina_custom":		"661a2c5f-e665-4ac9-b88a-d420b2b064d2",
		"copertina_secondaria":	None,
		"fin":					"c73d4a01-e034-4f53-a6e1-9537200eefb1",
		"blank":				"dbda9ab9-710c-4ce2-84f2-002cafd9bc89",

		"risultati":			"1dba9253-8684-4515-99f5-96687584bab5",
		"cartello":				"84adf749-3975-4db5-94e9-fdd11ec146d7",
		"blackJB":				"f9b2563b-9756-4944-b560-1f55a52efee7"
	}
	layLayer = {
		"RES_superato":			"c6549418-e4ae-487b-b855-0d878a7048fe",
		"RES_fallito":			"30e5f3c6-90d8-4af7-9e31-292e59d29032",
		"QUIZ_RES_giusto":		("04534019-334b-4097-9652-a5d3a4bd1eb6", "b8357ecc-df16-4480-87b1-fdd171302ade"),
		"QUIZ_RES_sbagliato":	("c285d117-2c18-4d08-b344-b7757c7a7f45", "d5d7855e-a8d1-4dec-8910-9edb638da741")
	}

	def __init__ (self, nome, layout):
		print "+==(time: {0})===+".format(self.tools.now())
		super(WbtEVO, self).__init__(nome, self.masters[layout])
		self.curScn = None
		self.curSld = None
		self.curBank = None
		self.curRes = None
		self.c_tit = 0
		self.c_vid = 0
		self.c_lyr = 0
		self.c_sld = 1
		self.c_jb = 1

		# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

		self.indeSld = None; self.indeSldscroll = None
		self.aprfSld = None

		self.onScene(1); self.onSlide(0)
		self.indeSld = self.curSld
		
		self.onScene(1); self.onSlide(2)
		self.aprfSld = self.curSld

		self.get_var('titolo_corso').set(nome)

		self.indeSldscroll = self.indeSld.insert_scrollBox('scrollBox')

	def save (self, justStory=False):
		if not justStory:
			self.get_var('numPages').set(self.c_sld)

		super(WbtEVO, self).save(justStory)
		print "+==(time: {0})===+".format(self.tools.now())

	def onScene (self, _id):
		if 0 <= _id < len(self.l_scene):
			self.curScn = self.l_scene[_id]
			self.curSld = None # Reset curSld
		else:
			print "Scena non trovata: l'id dato sembra essere fuori range"
	def onSlide (self, _id):
		if self.curScn is not None:
			if 0 <= _id < len(self.curScn.l_slide):
				self.curSld = self.curScn.l_slide[_id]
			else:
				print "Slide non trovata: l'id dato sembra essere fuori range"
		else:
			print "Impossibile selezionare una slide: Nessuna scena e' stata prima selezionata."
	
	def scene (self, tit):
		self.curScn = self.new_scene(tit)

	def var (self, nome, val, gid=None):
		super(WbtEVO, self).new_var(nome, val, gid)

	def slide (self, tit, navbar=False, layout='blank'):

		print u"\nNEW SLIDE {0}...".format(tit)

		self.c_sld += 1

		neoSld = self.curScn.new_slide(tit, self.layouts[layout])

		# NODE THEORY, se me la ricordo...
		neoSld.prevSld = self.curSld
		self.curSld.nextSld = neoSld
		self.curSld = neoSld
			
		self.trig_pageNumber(self.c_sld)
		self.curSld.navData(False, False, False)

	def link_slide (self):
		print "LINKING SLIDE..."

		ls = self.curScn.l_slide
		cur = next = None

		i = 0
		while i < len(ls)-1:
			
			cur = ls[i]
			next = None

			if type(cur) is storyLineObj_plus.Sl_JbCover:
				next = ls[i+3]
				res = ls[i+2]
				
				trg = Sl_TrigObj( "", cur.g )
				trg.act_jumpToSlide( next.g )
				trg.evt_onTmLnStart()
				trg.condition( [self.get_var('maxQuiz').g], '>=', [self.get_var('pageNumber').g] )
				cur.addTrig(trg)

				trg = Sl_TrigObj( "", res.g )
				trg.act_jumpToSlide( next.g )
				trg.evt_chngVar(self.get_var('pageNext').g)
				res.addTrig(trg)

				if type(next) is not storyLineObj_plus.Sl_JbCover:
					trg = self.trig_toPagePrev(next.g, ls[i-1].g)
					next.addTrig(trg)

			elif type(cur) is storyLineObj_plus.Sl_Slide:
				next = ls[i+1]

				trg = self.trig_toPageNext(cur.g, next.g)
				cur.addTrig(trg)

				if type(next) is storyLineObj_plus.Sl_Slide:
					trg = self.trig_toPagePrev(next.g, cur.g)
					next.addTrig(trg)

			if type(cur) is storyLineObj_plus.Sl_ResSlide and cur.nome == 'FIN':
				prev = ls[i-1]
				if type(prev) is storyLineObj_plus.Sl_ResSlide:
					prev = ls[i-4]

				trg = self.trig_toPagePrev(cur.g, prev.g)
				cur.addTrig(trg)

			if type(cur) is storyLineObj_plus.Sl_JBSlide:
				next = ls[i+1]
				trg = Sl_TrigObj( "", cur.g )
				trg.act_jumpToSlide( next.g )
				trg.evt_onTmLnStart()
				trg.condition( [self.get_var('maxQuiz').g], '>=', [self.get_var('pageNumber').g] )
				cur.addTrig(trg)

				prev = ls[i-1]
				if type(prev) is storyLineObj_plus.Sl_Slide:
					trg = self.trig_toPagePrev(next.g, prev.g)
					next.addTrig(trg)

				trg = Sl_TrigObj( "", cur.g )
				trg.act_jumpToSlide( next.g )
				trg.evt_chngVar(self.get_var('pageNext').g)
				cur.addTrig(trg)
				
				trg = Sl_TrigObj( "", cur.g )
				trg.act_jumpToSlide( next.g )
				trg.evt_chngVar(self.get_var('pagePrev').g)
				cur.addTrig(trg)	

			i += 1
				
			
	def cartello (self, tit):
		print u"\nNEW JB COPERTINA {0}...".format(tit)

		self.c_sld += 1

		neoSld = self.curScn.new_slide(tit, self.layouts['cartello'], sldBase='jbCover.xml')

		# NODE THEORY, se me la ricordo...
		neoSld.prevSld = self.curSld
		self.curSld.nextSld = neoSld
		self.curSld = neoSld

		self.trig_pageNumber(self.c_sld)
		self.curSld.navData(False, False, False)

	def questionBank (self, tit):
		print "NEW QUESTION BANK {0}...".format(tit)
		self.curBank = self.add_questBank(tit, self.curScn)

	def BnkJobStop (self, tit, tipo, quest, navbar=True):
		print "\nNEW JOB STOP IN BANK {0}...".format(self.curBank[0].nome)
		sld = self.curBank[0].new_slide(tit, self.layouts['blackJB'])
		sld.make_jobstop(tipo, quest, (self.layLayer['QUIZ_RES_giusto'], self.layLayer['QUIZ_RES_sbagliato']))
		#self.c_sld += 1

	def slide_RES (self, tit):
		print "\nNEW SLIDE {0}...".format(tit)

		self.curRes = self.curScn.new_slide(tit, self.layouts['risultati'], 'ResSlide.xml')
		self.curRes.make_resultSlide(laylay=(self.layLayer['RES_superato'], self.layLayer['RES_fallito']))
		self.curRes.navData(False, False, False)

	def slide_FIN (self):
		print "\nFIN SLIDE"
		self.curRes = self.curScn.new_slide('FIN', self.layouts['fin'], 'ResSlide.xml')

		self.curSld = self.curRes
		self.c_sld += 1
		self.trig_pageNumber(self.c_sld)

		self.curRes.make_resultSlide(None, passScore=0, isFIN=True)
		self.curRes.navData(False, False, False)

	def jobstop (self, tit, tipo, quest, navbar=True):
		print "\nNEW SLIDE {0}...".format(tit)

		neoSld = self.curScn.new_slide(tit, self.layouts['blackJB'], 'JBSlide.xml')
		neoSld.make_jobstop(tipo, quest, (self.layLayer['QUIZ_RES_giusto'], self.layLayer['QUIZ_RES_sbagliato']))
		self.curSld = neoSld
		self.c_sld += 1
		self.trig_pageNumber(self.c_sld)


		#self.c_sld += 1

	def JobStop (self):
		t_jb = "JOB {0}".format(self.c_jb)
		t_bk = "BNK {0}".format(self.c_jb)
		t_res = "RES {0}".format(self.c_jb)

		self.cartello( t_jb ) # self.curSld

		self.questionBank( t_bk ) # self.curBank

		self.slide_RES( t_res ) # self.curRes

		self.gidGen.slide += 3
		nextSldGID = self.gidGen.get('slide')[0]; self.gidGen.slide -= 4
		# print nextSldGID

		# TRIGGER DI COVER...
		t = Sl_TrigObj( "", self.curSld.g )
		t.act_jumpToSlide( self.curBank[1].g )
		t.evt_onTmLnEnd()
		self.curSld.addTrig(t)

		'''t = Sl_TrigObj( "", self.curSld.g )
		t.act_jumpToSlide( nextSldGID )
		t.evt_onTmLnStart()
		t.condition( [self.get_var('maxQuiz').g], '>=', [self.get_var('pageNumber').g] )
		self.curSld.addTrig(t)'''

		# TRIGGER DI RISULTATO...
		t = Sl_TrigObj( "", self.curRes.g )
		t.act_resetQuiz( self.curRes.g )
		t.evt_chngVar(self.get_var('pagePrev').g)
		self.curRes.addTrig(t)

		t = Sl_TrigObj( "", self.curRes.g )
		t.act_jumpToSlide( self.curSld.prevSld.g )
		t.evt_chngVar(self.get_var('pagePrev').g)
		self.curRes.addTrig(t)

		'''t = Sl_TrigObj( "", self.curRes.g )
		t.act_jumpToSlide( nextSldGID )
		t.evt_chngVar(self.get_var('pageNext').g)
		self.curRes.addTrig(t)'''

		self.c_jb += 1;

	def layer (self, nome=None):
		if nome is None:
			nome = "layer_{0}".format(self.c_lyr)

		ly = self.curSld.insert_layer(nome)

	def titolo (self, tit):
		self.c_tit += 1
		# self.c_tit = self.c_sld

		itm = ("item{0:02}P".format(self.c_tit), "item{0:02}T".format(self.c_tit))

		tit = self.tools.replaceAccentiVocali(tit)
		# print u"-=-=- {0} -=-=-".format(tit)
		super(WbtEVO, self).new_var(itm[0], self.c_sld)
		super(WbtEVO, self).new_var(itm[1], tit)

		return itm

	def trig_PVoTS (self, v):
		trg = Sl_TrigObj( "", v.g )
		trg.act_playMedia( v.g, 'video' )
		trg.evt_onTmLnStart()
		v.addTrig(trg)
		return trg
	def trig_pageNumber (self, pageN):
		trg = Sl_TrigObj( "", self.curSld.g )
		trg.act_setVar( self.get_var('pageNumber').g, pageN )
		trg.evt_onTmLnStart()
		self.curSld.addTrig(trg)

	def trig_toPagePrev (self, copiedG, prevG):
		trg = Sl_TrigObj( "", copiedG )
		trg.act_jumpToSlide( prevG )
		trg.evt_chngVar(self.get_var('pagePrev').g)
		return trg
	def trig_toPageNext (self, copiedG, nextG):
		trg = Sl_TrigObj( "", copiedG )
		trg.act_jumpToSlide( nextG )
		trg.evt_chngVar(self.get_var('pageNext').g)
		return trg

# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #

class WbtOLDbutGOLD (WbtEVO):

	layLayer = {
		"RES_superato":			"c6549418-e4ae-487b-b855-0d878a7048fe",
		"RES_fallito":			"30e5f3c6-90d8-4af7-9e31-292e59d29032",
		"QUIZ_RES_giusto":		("04534019-334b-4097-9652-a5d3a4bd1eb6", "b8357ecc-df16-4480-87b1-fdd171302ade"),
		"QUIZ_RES_sbagliato":	("c285d117-2c18-4d08-b344-b7757c7a7f45", "d5d7855e-a8d1-4dec-8910-9edb638da741")
	}

	def __init__(self, nome, titolo=None):
		super(WbtOLDbutGOLD, self).__init__(nome, 'ObG')
		self.c_aprf = 1

		self.indeSld = None; self.indeSldscroll = None
		self.aprfSld = None

		self.onScene(1); self.onSlide(0)
		self.indeSld = self.curSld
		
		self.onScene(1); self.onSlide(2)
		self.aprfSld = self.curSld

		
		if titolo is None:
			self.get_var('titolo_corso').set(nome)
		else:
			self.get_var('titolo_corso').set(titolo)

		self.indeSldscroll = self.indeSld.insert_scrollBox('scrollBox')
		self.indeSldscroll

	def approfondimento (self, n, f):
		txt = self.aprfSld.insert_text( 'aprf{0}'.format(self.c_aprf), n, ['Arial', '12', '#808080', False, False])

		txt.margin(23, 0, 23, 0)
		txt.scale(720, 20); txt.cord(0, (34*(self.c_aprf-1))+152)

		trg = Sl_TrigObj( "", txt.g )
		trg.evt_onClick()
		f = self.tools.path_assoluto(f)
		trg.act_downloadFile(f)
		txt.addTrig(trg)

		self.c_aprf += 1

	def titolo_v1_funzioneFutura(self, tit):
		var = super(WbtOLDbutGOLD, self).titolo(tit)
		text = "%{0}%".format(var[1])

		txt = self.curSld.insert_text( tit, text, ['Arial Narrow', '12', '#808080', False, False], _PADRE=self.curSld)
		txt.margin(35, 0, 30, 0)
		txt.scale(720, 20); txt.cord(0, (34*(self.c_tit-1))+70)

		sta = txt.add_state('Normal')
		t1 = sta.insert_text('nmT', text, ['Arial Narrow', '12', '#808080', False, False])
		t1.margin(35, 0, 30, 0); t1.scale(720, 20); t1.cord(0, 0);
		'''pic = sta.insert_pic('__slide masters__\\ObG_asset\\indiceBox_normal.png', nick="indiceBox_normal", pos=(17, -1))
		pic.scale(38, 38); pic.cord(5, -3);'''

		sta1 = txt.add_state('_visited_')
		t2 = sta1.insert_text('nmT', text, ['Arial Narrow', '12', '#000000', False, False])
		t2.margin(35, 0, 30, 0); t2.scale(720, 20); t2.cord(0, 0);
		'''pic = sta1.insert_pic('__slide masters__\\ObG_asset\\indiceBox_visited.png', nick="indiceBox_visited", pos=(17, -1))
		pic.scale(38, 38); pic.cord(3, -11);'''

		sta2 = txt.add_state('_on_')
		t3 = sta2.insert_text('nmT', text, ['Arial Narrow', '12', '#EA980D', True, False])
		t3.margin(35, 0, 30, 0); t3.scale(720, 20); t3.cord(0, 0);
		'''pic = sta2.insert_pic('__slide masters__\\ObG_asset\\indiceBox_on.png', nick="indiceBox_on", pos=(17, -1))
		pic.scale(38, 38); pic.cord(5, -3);'''

		# TRIGGERRRRR
		trg = Sl_TrigObj( "", self.curSld.g )
		trg.act_chngState( txt.g, '_visited_' )
		trg.evt_onTmLnStart()
		trg.condition( [self.get_var('maxPage').g], '>=', [self.get_var(var[0]).g] )

		trg2 = Sl_TrigObj( "", self.curSld.g )
		trg2.act_chngState( txt.g, '_on_' )
		trg2.evt_onTmLnStart()
		trg2.condition( [self.get_var('pageNumber').g], '==', [self.get_var(var[0]).g] )

		self.curSld.addTrig(trg)
		self.curSld.addTrig(trg2)

	def titolo(self, tit):
		print u"- write Titolo: {0}".format(tit)

		var = super(WbtOLDbutGOLD, self).titolo(tit)

		# CREAZIONE TITOLO PER INDICE
		text = "%{0}%".format(var[1])
		r = self.prefabs.ratio(str(text), text, stile='oldWBT_radio.xml', stileTesto=['Arial Narrow', '12', '#808080', False, False])
		rat = SlObj_ShapeObj( 'text', r, pos=(0,(34*(self.c_tit-1))+70), size=(720, 34), timing=(0, 5000, False, True))

		# CREAZIONE TRIGGER PER ELEMENTI INDICE		
		trg = Sl_TrigObj( "", self.indeSld.g )
		trg.act_chngState( rat.g, '_visited_' )
		trg.evt_onTmLnStart()
		trg.condition( [self.get_var('maxPage').g], '>=', [self.get_var(var[0]).g] )

		trg2 = Sl_TrigObj( "", self.indeSld.g )
		trg2.act_chngState( rat.g, '_on_' )
		trg2.evt_onTmLnStart()
		trg2.condition( [self.get_var('pageNumber').g], '==', [self.get_var(var[0]).g] )

		# INSERIMENTO ELEMENTO INDICE E TRIGGER IN SLIDE
		self.indeSld.f_xml.find('shapeLst').append( rat.f_xml )
		self.indeSld.f_xml.find('trigLst').append( trg.f_xml )
		self.indeSld.f_xml.find('trigLst').append( trg2.f_xml )
		self.indeSldscroll.addChild(rat)
		self.indeSldscroll.resize(720, 470); self.indeSldscroll.cord(0, 70)

		# AGGIUNTA TITOLO NELLA SLIDE CORRENTE
		titSld = self.curSld.insert_text( 'titolo', text, ['Arial', '16', '#EA980D', True, False] )
		titSld.scale(720, 51); titSld.cord(0, 73)
		titSld.retiming(0, 5000, True, True)
		titSld.margin (44, 0, 44, 3)
		self.curSld.set_titolo(tit)

	def slide (self, tit, navbar=False, layout='blank'):

		print u"\nNEW SLIDE {0}...".format(tit)

		self.c_sld += 1

		neoSld = self.curScn.new_slide(tit, self.layouts[layout])

		# NODE THEORY, se me la ricordo...
		neoSld.prevSld = self.curSld
		self.curSld.nextSld = neoSld
		self.curSld = neoSld

		if navbar is True:
			prevSld = self.curSld.prevSld
			trg = self.trig_toPagePrev(self.curSld.g, prevSld.g)
			self.curSld.addTrig(trg)

			lastSld = self.curSld.prevSld
			trg = self.trig_toPageNext(lastSld.g, self.curSld.g)
			lastSld.addTrig(trg)
		
		if type(self.curSld) is storyLineObj_plus.Sl_Slide:
			self.titolo(tit)
			
		self.trig_pageNumber(self.c_sld)
		self.curSld.navData(False, False, False)

	def video (self, v, n='video', 
			pi="__slide masters__/ObG_asset/cover_in.png",
			po="__slide masters__/ObG_asset/cover_out.png"):
		print u"- add Video: {0}; filename: {1}".format(n, v)

		# IMPORTING...
		vid = self.curSld.insert_video(v, n)
		pstIn = self.curSld.insert_pic(pi, nick="post-in")
		pstOut = self.curSld.insert_pic(po, nick="post-out")

		trg = Sl_TrigObj( "", self.indeSld.g )
		trg.act_jumpToSlide( self.curSld.g )
		trg.evt_onClick()
		pstOut.addTrig(trg)

		# ASSEMBLAGGIO SLIDE
		vid.scale(132, 132)
		vid.cord(44, 124)
		vid.StartTime(3000)
		vid.fadeIn(); vid.fadeOut()

		pstIn.cord(44, 124)
		pstIn.retiming(0, 3000)
		pstIn.fadeIn(50); pstIn.fadeOut(50)

		pstOut.cord(44, 124)
		pstOut.retiming((vid.duration + vid.startTime), 1500, shw_tilEnd=True)
		pstOut.fadeIn(50)

		# IMPOSTAZIONI VIDEO
		vid.playOnTrig()
		trg = self.trig_PVoTS(vid)

# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #

class WbtOLDbutUBI (WbtEVO):

	layLayer = {
		"RES_superato":			"c6549418-e4ae-487b-b855-0d878a7048fe",
		"RES_fallito":			"30e5f3c6-90d8-4af7-9e31-292e59d29032",
		"QUIZ_RES_giusto":		("04534019-334b-4097-9652-a5d3a4bd1eb6", "b8357ecc-df16-4480-87b1-fdd171302ade"),
		"QUIZ_RES_sbagliato":	("c285d117-2c18-4d08-b344-b7757c7a7f45", "d5d7855e-a8d1-4dec-8910-9edb638da741")
	}

	def __init__(self, nome, titolo=None):
		super(WbtOLDbutUBI, self).__init__(nome, 'ObUBI')
		self.c_aprf = 1

		self.indeSld = None; self.indeSldscroll = None
		self.aprfSld = None

		self.onScene(1); self.onSlide(0)
		self.indeSld = self.curSld
		
		self.onScene(1); self.onSlide(2)
		self.aprfSld = self.curSld

		
		if titolo is None:
			self.get_var('titolo_corso').set(nome)
		else:
			self.get_var('titolo_corso').set(titolo)

		self.indeSldscroll = self.indeSld.insert_scrollBox('scrollBox')
		self.indeSldscroll

	def approfondimento (self, n, f):
		txt = self.aprfSld.insert_text( 'aprf{0}'.format(self.c_aprf), n, ['Cabin', '12', '#808080', False, False])

		txt.margin(23, 0, 23, 0)
		txt.scale(720, 20); txt.cord(0, (34*(self.c_aprf-1))+152)

		trg = Sl_TrigObj( "", txt.g )
		trg.evt_onClick()
		f = self.tools.path_assoluto(f)
		trg.act_downloadFile(f)
		txt.addTrig(trg)

		self.c_aprf += 1

	def titolo_v1_funzioneFutura(self, tit):
		var = super(WbtOLDbutUBI, self).titolo(tit)
		text = "%{0}%".format(var[1])

		txt = self.curSld.insert_text( tit, text, ['Cabin Narrow', '12', '#808080', False, False], _PADRE=self.curSld)
		txt.margin(35, 0, 30, 0)
		txt.scale(720, 20); txt.cord(0, (34*(self.c_tit-1))+70)

		sta = txt.add_state('Normal')
		t1 = sta.insert_text('nmT', text, ['Cabin Narrow', '12', '#808080', False, False])
		t1.margin(35, 0, 30, 0); t1.scale(720, 20); t1.cord(0, 0);
		'''pic = sta.insert_pic('__slide masters__\\ObG_asset\\indiceBox_normal.png', nick="indiceBox_normal", pos=(17, -1))
		pic.scale(38, 38); pic.cord(5, -3);'''

		sta1 = txt.add_state('_visited_')
		t2 = sta1.insert_text('nmT', text, ['Cabin Narrow', '12', '#000000', False, False])
		t2.margin(35, 0, 30, 0); t2.scale(720, 20); t2.cord(0, 0);
		'''pic = sta1.insert_pic('__slide masters__\\ObG_asset\\indiceBox_visited.png', nick="indiceBox_visited", pos=(17, -1))
		pic.scale(38, 38); pic.cord(3, -11);'''

		sta2 = txt.add_state('_on_')
		t3 = sta2.insert_text('nmT', text, ['Cabin Narrow', '12', '#EA980D', True, False])
		t3.margin(35, 0, 30, 0); t3.scale(720, 20); t3.cord(0, 0);
		'''pic = sta2.insert_pic('__slide masters__\\ObG_asset\\indiceBox_on.png', nick="indiceBox_on", pos=(17, -1))
		pic.scale(38, 38); pic.cord(5, -3);'''

		# TRIGGERRRRR
		trg = Sl_TrigObj( "", self.curSld.g )
		trg.act_chngState( txt.g, '_visited_' )
		trg.evt_onTmLnStart()
		trg.condition( [self.get_var('maxPage').g], '>=', [self.get_var(var[0]).g] )

		trg2 = Sl_TrigObj( "", self.curSld.g )
		trg2.act_chngState( txt.g, '_on_' )
		trg2.evt_onTmLnStart()
		trg2.condition( [self.get_var('pageNumber').g], '==', [self.get_var(var[0]).g] )

		self.curSld.addTrig(trg)
		self.curSld.addTrig(trg2)

	def titolo(self, tit):
		print u"- write Titolo: {0}".format(tit)

		var = super(WbtOLDbutUBI, self).titolo(tit)

		# CREAZIONE TITOLO PER INDICE
		text = "%{0}%".format(var[1])
		'''r = self.prefabs.ratio(str(text), text, stile='oldWBT_radio.xml', stileTesto=['Cabin Narrow', '12', '#808080', False, False])
		rat = SlObj_ShapeObj( 'text', r, pos=(0,(34*(self.c_tit-1))+70), size=(720, 34), timing=(0, 5000, False, True))

		# CREAZIONE TRIGGER PER ELEMENTI INDICE		
		trg = Sl_TrigObj( "", self.indeSld.g )
		trg.act_chngState( rat.g, '_visited_' )
		trg.evt_onTmLnStart()
		trg.condition( [self.get_var('maxPage').g], '>=', [self.get_var(var[0]).g] )

		trg2 = Sl_TrigObj( "", self.indeSld.g )
		trg2.act_chngState( rat.g, '_on_' )
		trg2.evt_onTmLnStart()
		trg2.condition( [self.get_var('pageNumber').g], '==', [self.get_var(var[0]).g] )

		# INSERIMENTO ELEMENTO INDICE E TRIGGER IN SLIDE
		self.indeSld.f_xml.find('shapeLst').append( rat.f_xml )
		self.indeSld.f_xml.find('trigLst').append( trg.f_xml )
		self.indeSld.f_xml.find('trigLst').append( trg2.f_xml )
		self.indeSldscroll.addChild(rat)
		self.indeSldscroll.resize(720, 470); self.indeSldscroll.cord(0, 70)'''

		# AGGIUNTA TITOLO NELLA SLIDE CORRENTE
		titSld = self.curSld.insert_text( 'titolo', text, ['Cabin', '14', '#5F95B7', False, False] )
		titSld.scale(350, 90); titSld.cord(36, 20)
		titSld.retiming(0, 5000, True, True)
		titSld.margin (0, 0, 0, 0)
		self.curSld.set_titolo(tit)

	def slide (self, tit, navbar=False, layout='blank'):

		print u"\nNEW SLIDE {0}...".format(tit)

		self.c_sld += 1

		neoSld = self.curScn.new_slide(tit, self.layouts[layout])

		# NODE THEORY, se me la ricordo...
		neoSld.prevSld = self.curSld
		self.curSld.nextSld = neoSld
		self.curSld = neoSld

		if navbar is True:
			prevSld = self.curSld.prevSld
			trg = self.trig_toPagePrev(self.curSld.g, prevSld.g)
			self.curSld.addTrig(trg)

			lastSld = self.curSld.prevSld
			trg = self.trig_toPageNext(lastSld.g, self.curSld.g)
			lastSld.addTrig(trg)
		
		if type(self.curSld) is storyLineObj_plus.Sl_Slide:
			self.titolo(tit)
			
		self.trig_pageNumber(self.c_sld)
		self.curSld.navData(False, False, False)

	def video (self, v, n='video',
			pi="__slide masters__/ObG_asset/cornice.png",
			po="__slide masters__/ObG_asset/riguarda.png"):
		print u"- add Video: {0}; filename: {1}".format(n, v)

		# IMPORTING...
		vid = self.curSld.insert_video(v, n)
		'''pstIn = self.curSld.insert_pic(pi, nick="post-in")
		pstOut = self.curSld.insert_pic(po, nick="post-out")'''
		cornice = self.curSld.insert_pic(pi, nick="cornice")
		riguarda = self.curSld.insert_pic(po, nick="riguarda")

		trg = Sl_TrigObj( "", self.indeSld.g )
		trg.act_jumpToSlide( self.curSld.g )
		trg.evt_onClick()
		riguarda.addTrig(trg)

		# ASSEMBLAGGIO SLIDE
		vid.cord(120, 121+(145-121))
		vid.StartTime(3000)
		vid.fadeIn(); vid.fadeOut();

		cornice.cord(101, 111+(145-121))
		cornice.StartTime(3000)
		cornice.retiming(3000, (vid.duration + vid.startTime), shw_tilEnd=True)
		cornice.fadeIn();

		riguarda.cord(272, 209+(145-121))
		riguarda.retiming((vid.duration + vid.startTime), 1500, shw_tilEnd=True)
		riguarda.fadeIn(50)

		'''pstIn.cord(44, 124)
		pstIn.retiming(0, 3000)
		pstIn.fadeIn(50); pstIn.fadeOut(50)

		pstOut.cord(44, 124)
		pstOut.retiming((vid.duration + vid.startTime), 1500, shw_tilEnd=True)
		pstOut.fadeIn(50)'''

		# IMPOSTAZIONI VIDEO
		vid.playOnTrig()
		trg = self.trig_PVoTS(vid)

# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #


class WbtLAND (WbtEVO):

	layLayer = {
		"RES_superato":			"c6549418-e4ae-487b-b855-0d878a7048fe",
		"RES_fallito":			"30e5f3c6-90d8-4af7-9e31-292e59d29032",
		"QUIZ_RES_giusto":		("04534019-334b-4097-9652-a5d3a4bd1eb6", "b8357ecc-df16-4480-87b1-fdd171302ade"),
		"QUIZ_RES_sbagliato":	("c285d117-2c18-4d08-b344-b7757c7a7f45", "d5d7855e-a8d1-4dec-8910-9edb638da741")
	}

	def __init__(self, nome, titolo=None):
		super(WbtLAND, self).__init__(nome, 'LAND') # "LAND":"__slide masters__/LAND"
		self.c_aprf = 1

		self.indeSld = None; self.indeSldscroll = None
		self.aprfSld = None

		self.onScene(1); self.onSlide(0)
		self.indeSld = self.curSld

		if titolo is None:
			self.get_var('titolo_corso').set(nome)
		else:
			self.get_var('titolo_corso').set(titolo)

		self.indeSldscroll = self.indeSld.insert_scrollBox('scrollBox')

	def titolo(self, tit):
		print u"- write Titolo: {0}".format(tit)

		var = super(WbtLAND, self).titolo(tit)

		# CREAZIONE TITOLO PER INDICE
		text = "%{0}%".format(var[1])
		r = self.prefabs.ratio(str(text), text, stile='ubi_radio.xml', stileTesto=['Cabin', '12', '#808080', False, False])
		rat = SlObj_ShapeObj( 'text', r, pos=(0,(34*(self.c_tit-1))+70), size=(720, 34), timing=(0, 5000, False, True))

		# CREAZIONE TRIGGER PER ELEMENTI INDICE		
		trg = Sl_TrigObj( "", self.indeSld.g )
		trg.act_chngState( rat.g, '_on_' ) # _visited_
		trg.evt_onTmLnStart()
		trg.condition( [self.get_var('maxPage').g], '>=', [self.get_var(var[0]).g] )

		trg2 = Sl_TrigObj( "", self.indeSld.g )
		trg2.act_chngState( rat.g, '_visited_' ) # _on_
		trg2.evt_onTmLnStart()
		trg2.condition( [self.get_var('pageNumber').g], '==', [self.get_var(var[0]).g] )

		# rat.cord=(0,(34*(self.c_tit-1))+70)

		# INSERIMENTO ELEMENTO INDICE E TRIGGER IN SLIDE
		self.indeSld.f_xml.find('shapeLst').append( rat.f_xml )
		self.indeSld.f_xml.find('trigLst').append( trg.f_xml )
		self.indeSld.f_xml.find('trigLst').append( trg2.f_xml )
		self.indeSldscroll.addChild(rat)
		self.indeSldscroll.resize(720, 470);
		self.indeSldscroll.cord(0, 70)

		# AGGIUNTA TITOLO NELLA SLIDE CORRENTE
		titSld = self.curSld.insert_text( 'titolo', text, ['Cabin', '16', '#5F95B7', False, False] )
		titSld.scale(350, 90); titSld.cord(36, 20)
		titSld.retiming(0, 5000, True, True)
		titSld.margin (0, 0, 0, 0)
		self.curSld.set_titolo(tit)

	def slide (self, tit, navbar=False, layout='blank'):

		print u"\nNEW SLIDE {0}...".format(tit)

		self.c_sld += 1

		neoSld = self.curScn.new_slide(tit, self.layouts[layout])

		# NODE THEORY, se me la ricordo...
		neoSld.prevSld = self.curSld
		self.curSld.nextSld = neoSld
		self.curSld = neoSld

		if navbar is True:
			prevSld = self.curSld.prevSld
			trg = self.trig_toPagePrev(self.curSld.g, prevSld.g)
			self.curSld.addTrig(trg)

			lastSld = self.curSld.prevSld
			trg = self.trig_toPageNext(lastSld.g, self.curSld.g)
			lastSld.addTrig(trg)
		
		if type(self.curSld) is storyLineObj_plus.Sl_Slide and layout != 'copertina':
			self.titolo(tit)
			
		self.trig_pageNumber(self.c_sld)
		self.curSld.navData(False, False, False)

	def video (self, v, n='video',
			pi="__slide masters__/LAND_asset/cornice.png",
			po="__slide masters__/LAND_asset/riguarda.png"):
		print u"- add Video: {0}; filename: {1}".format(n, v)

		# IMPORTING...
		vid = self.curSld.insert_video(v, n)
		cornice = self.curSld.insert_pic(pi, nick="cornice")

		trg = Sl_TrigObj( "", self.indeSld.g )
		trg.act_jumpToSlide( self.curSld.g )
		trg.evt_onClick()

		# ASSEMBLAGGIO SLIDE
		vid.scale(47, 47)
		vid.cord(59, 117)
		vid.StartTime(1500)
		vid.fadeIn();

		cornice.scale(45, 48)
		cornice.cord(36, 102)
		cornice.StartTime(1500)
		cornice.retiming(1500, vid.duration, shw_tilEnd=True)
		cornice.fadeIn();

		# IMPOSTAZIONI VIDEO
		vid.playOnTrig()
		trg = self.trig_PVoTS(vid)

	def JobStop (self):
		t_jb = "JOB {0}".format(self.c_jb)
		t_bk = "BNK {0}".format(self.c_jb)

		self.cartello( t_jb ) # self.curSld

		self.questionBank( t_bk ) # self.curBank

		self.gidGen.slide += 2
		nextSldGID = self.gidGen.get('slide')[0]; self.gidGen.slide -= 4

		# TRIGGER DI COVER...
		t = Sl_TrigObj( "", self.curSld.g )
		t.act_jumpToSlide( self.curBank[1].g )
		t.evt_onTmLnEnd()
		self.curSld.addTrig(t)

		self.c_jb += 1;

	def link_slide (self):
		print "LINKING SLIDE..."

		ls = self.curScn.l_slide
		cur = next = None

		i = 0
		while i < len(ls)-1:
			
			cur = ls[i]
			next = None

			if type(cur) is storyLineObj_plus.Sl_JbCover:
				next = ls[i+2]
				
				trg = Sl_TrigObj( "", cur.g )
				trg.act_jumpToSlide( next.g )
				trg.evt_onTmLnStart()
				trg.condition( [self.get_var('maxQuiz').g], '>=', [self.get_var('pageNumber').g] )
				cur.addTrig(trg)

				if type(next) is not storyLineObj_plus.Sl_JbCover:
					trg = self.trig_toPagePrev(next.g, ls[i-1].g)
					next.addTrig(trg)

			elif type(cur) is storyLineObj_plus.Sl_Slide:
				next = ls[i+1]

				trg = self.trig_toPageNext(cur.g, next.g)
				cur.addTrig(trg)

				if type(next) is storyLineObj_plus.Sl_Slide:
					trg = self.trig_toPagePrev(next.g, cur.g)
					next.addTrig(trg)

			if type(cur) is storyLineObj_plus.Sl_ResSlide and cur.nome == 'FIN':
				prev = ls[i-1]
				if type(prev) is storyLineObj_plus.Sl_ResSlide:
					prev = ls[i-4]

				trg = self.trig_toPagePrev(cur.g, prev.g)
				cur.addTrig(trg)

			if type(cur) is storyLineObj_plus.Sl_JBSlide:
				next = ls[i+1]
				trg = Sl_TrigObj( "", cur.g )
				trg.act_jumpToSlide( next.g )
				trg.evt_onTmLnStart()
				trg.condition( [self.get_var('maxQuiz').g], '>=', [self.get_var('pageNumber').g] )
				cur.addTrig(trg)

				prev = ls[i-1]
				if type(prev) is storyLineObj_plus.Sl_Slide:
					trg = self.trig_toPagePrev(next.g, prev.g)
					next.addTrig(trg)

				trg = Sl_TrigObj( "", cur.g )
				trg.act_jumpToSlide( next.g )
				trg.evt_chngVar(self.get_var('pageNext').g)
				cur.addTrig(trg)
				
				trg = Sl_TrigObj( "", cur.g )
				trg.act_jumpToSlide( next.g )
				trg.evt_chngVar(self.get_var('pagePrev').g)
				cur.addTrig(trg)	

			i += 1
				
# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #


class WbtPaper (WbtEVO):
	def __init__ (self, nome):
		super(WbtPaper, self).__init__(nome, 'paper')

	def slide (self, tit, navbar=True):

		print "NEW SLIDE {0}...".format(tit)

		neoSld = self.curScn.new_slide(tit, self.layouts['blank'])

		# NODE THEORY, se me la ricordo...
		neoSld.prevSld = self.curSld
		self.curSld.nextSld = neoSld
		self.curSld = neoSld

		if navbar is True:
			prevSld = self.curSld.prevSld
			trg = self.trig_toPagePrev(self.curSld.g, prevSld.g)
			self.curSld.addTrig(trg)

			lastSld = self.curSld.prevSld
			trg = self.trig_toPageNext(lastSld.g, self.curSld.g)
			lastSld.addTrig(trg)

		self.titolo(tit)
		self.c_sld += 1
		self.trig_pageNumber(self.c_sld)

	def trig_toPagePrev (self, copiedG, prevG):
		trg = Sl_TrigObj( "", copiedG )
		trg.act_jumpToSlide( prevG )
		trg.evt_onClick('prev')
		return trg

	def trig_toPageNext (self, copiedG, nextG):
		trg = Sl_TrigObj( "", copiedG )
		trg.act_jumpToSlide( nextG )
		trg.evt_onClick('next')
		trg.condition( [self.get_var('continue').g], '-==', True )
		return trg

	def titolo (self, tit):
		print "- write Titolo: {0}".format(tit)

		# CONTROLLI
		if self.curSld is None:
			print "Impossibile inserire TextBox: nessuna slide selezionata."
			return
		self.c_tit += 1

		txt = self.curSld.insert_text( 'titolo', tit, ['Ruda', '16', '#A6412B', True, False] )

		txt.scale(670, 40); txt.cord(24, 14)
		txt.retiming(0, 5000, True, True)

		self.curSld.set_titolo(tit)

	def video (self, v, n):
		print "- add Video: {0}; filename: {1}".format(n, v)

		# CONTROLLI
		if self.curSld is None:
			print "Impossibile importare video: nessuna slide selezionata."
			return
		self.c_vid += 1

		# IMPORTING...
		vid = self.curSld.insert_video(v, n)
		bkg = self.curSld.insert_pic("__slide masters__/paper_asset/bkg_video.png", nick="post-it")

		# ASSEMBLAGGIO SLIDE
		# vid.scale(92, 92)
		vid.scale(96, 96)
		vid.cord(520, 85)
		bkg.cord(488, 62)

		# IMPOSTAZIONI VIDEO
		vid.playOnTrig()
		trg = self.trig_PVoTS(vid)

		# TEMPISTICA
		bkg.retiming( vid.startTime, vid.duration )

		# GROUPING
		#childs = [bkg, vid]
		#grp = self.curSld.formGroup("video{0}".format(self.c_vid), childs)

		# GROUP ANIM
		#grp.fadeIn(50, 'r')

# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=- #


class WbtUbi(WbtEVO):

	layLayer = {
		"RES_superato":			"b40d068c-581c-4c87-96ff-da7e7d848b3e",
		"RES_fallito":			"11bdfaf2-e0e0-4dd1-9e19-497975695ed9",
		"QUIZ_RES_giusto":		("8f36cfd2-613c-4c7d-b9c8-6412a49d73b9", "b8357ecc-df16-4480-87b1-fdd171302ade"),
		"QUIZ_RES_sbagliato":	("c75678ea-e6bb-47de-9bcf-ea52235d605d", "d5d7855e-a8d1-4dec-8910-9edb638da741")
	}

	def __init__ (self, nome):
		super(WbtUbi, self).__init__(nome, 'ubi')

	def titolo(self, tit):
		print u"- write Titolo: {0}".format(tit)

		var = super(WbtUbi, self).titolo(tit)

		# CREAZIONE TITOLO PER INDICE
		text = "%{0}%".format(var[1])
		r = self.prefabs.ratio(str(text), text, stile='ubi_radio.xml', stileTesto=['Cabin', '12', '#808080', False, False])
		rat = SlObj_ShapeObj( 'text', r, pos=(0,(34*(self.c_tit-1))+70), size=(720, 34), timing=(0, 5000, False, True))

		# CREAZIONE TRIGGER PER ELEMENTI INDICE		
		trg = Sl_TrigObj( "", self.indeSld.g )
		trg.act_chngState( rat.g, '_visited_' )
		trg.evt_onTmLnStart()
		trg.condition( [self.get_var('maxPage').g], '>=', [self.get_var(var[0]).g] )

		trg2 = Sl_TrigObj( "", self.indeSld.g )
		trg2.act_chngState( rat.g, '_on_' )
		trg2.evt_onTmLnStart()
		trg2.condition( [self.get_var('pageNumber').g], '==', [self.get_var(var[0]).g] )

		# INSERIMENTO ELEMENTO INDICE E TRIGGER IN SLIDE
		self.indeSld.f_xml.find('shapeLst').append( rat.f_xml )
		self.indeSld.f_xml.find('trigLst').append( trg.f_xml )
		self.indeSld.f_xml.find('trigLst').append( trg2.f_xml )
		self.indeSldscroll.addChild(rat)
		self.indeSldscroll.resize(720, 470); self.indeSldscroll.cord(0, 70)

		# AGGIUNTA TITOLO NELLA SLIDE CORRENTE
		titSld = self.curSld.insert_text( 'titolo', text, ['Cabin', '16', '#4C7792', False, False] )
		titSld.scale(230, 82); titSld.cord(36, 20)
		titSld.retiming(0, 5000, True, True)
		titSld.margin (0, 0, 0, 0)
		self.curSld.set_titolo(tit)

	def slide (self, tit, navbar=True):
		super(WbtUbi, self).slide(tit)
		self.titolo(tit)

	def videoSx (self, v, n):
		print "- add Video: {0}; filename: {1}".format(n, v)

		# CONTROLLI
		if self.curSld is None:
			print "Impossibile importare video: nessuna slide selezionata."
			return
		self.c_vid += 1

		# IMPORTING...
		vid = self.curSld.insert_video(v, n)

		# ASSEMBLAGGIO SLIDE
		# vid.scale(92, 92)
		vid.scale(96, 96)
		vid.cord(20, 108)
		vid.fadeIn()

		# IMPOSTAZIONI VIDEO
		vid.playOnTrig()
		trg = self.trig_PVoTS(vid)

	def videoDx (self, v, n):
		print "- add Video: {0}; filename: {1}".format(n, v)

		# CONTROLLI
		if self.curSld is None:
			print "Impossibile importare video: nessuna slide selezionata."
			return
		self.c_vid += 1

		# IMPORTING...
		vid = self.curSld.insert_video(v, n)

		# ASSEMBLAGGIO SLIDE
		# vid.scale(92, 92)
		vid.scale(96, 96)
		vid.cord(486, 116)
		vid.fadeIn()

		# IMPOSTAZIONI VIDEO
		vid.playOnTrig()
		trg = self.trig_PVoTS(vid)

