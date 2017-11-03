# -*- coding: utf-8 -*-
from tool import Tool
import Gid
from SLPrefabs import SLPrefabs

class StoryLineObj(object):
	''' Qualsiasi elemento abbia almeno un g e un verG '''
	
	# Tools
	gidGen = Gid.Gid()
	tools = Tool()

	# Vars
	c = 0

	def __init__ (self, gids, xml, rel=None):
		if type(gids) == str:
			pass
		elif type(gids) == Gid:
			pass
		self.g = gids.g()
		self.verG = gids.verG()

		self.xml = xml
		self.rel = rel

		self.f_xml = xml
		self.f_rel = rel
		# Modifica GID in XML

		self.c += 1

	def getGid (self, friz_and_frez=False):
		if not friz_and_frez:
			return self.g
		else:
			return ( self.g, self.verG )

# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-











# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-

class SlObj_FixedObj (StoryLineObj):
	def __init__ (self, g, xml):
		super(SlObj_FixedObj, self).__init__(g, xml)

class SlObj_ProgObj (SlObj_FixedObj):
	progC = 0
	def __init__ (self, g):
		super(SlObj_ProgObj, self).__init__(g)
		self.rel = self.xml+".rels"
		self.l_media = None

		self.progC += 1

	def create (self):
		pass
	def open (self):
		pass
	def close (self):
		pass

	def mediaImport (self, f, type):
		pass

class SlObj_AssetObj (SlObj_FixedObj):
	def __init__ (self, g):
		super(SlObj_AssetObj, self).__init__(g)

class Sl_TrigObj (SlObj_AssetObj):
	def __init__ (self, g):
		super(Sl_TrigObj, self).__init__(g)

class Sl_VarObj (SlObj_AssetObj):
	def __init__ (self, nome, val, xml=None):
		super(Sl_VarObj, self).__init__(g)


# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-

class SlObj_TimelineObj (StoryLineObj):
	def __init__ (self, g):
		super(SlObj_TimelineObj, self).__init__(g)

class Sl_SlideObj (SlObj_TimelineObj):
	def __init__ (self, g):
		super(Sl_SlideObj, self).__init__(g)
		self._PADRE = None # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

		self.rel = self.xml+".rels"
		self.l_trig = []
		# SHAPE LISTs
		self.l_video = []
		self.l_audio = []
		self.l_pic = []
		self.l_text = []
		self.l_shape = []
		self.l_group = []
	def add_video (self, g):
		pass
	def add_pic (self, g):
		pass
	def add_audio (self, g):
		pass
class SlObj_FileObj (Sl_SlideObj):
	def __init__ (self, g):
		super(SlObj_FileObj, self).__init__(g)
		pass

	def create (self):
		pass
	def open (self):
		pass
	def save (self):
		pass
	
	def add_layer(self):
		pass

class SlObj_ShapeObj (SlObj_TimelineObj):
	def __init__ (self, g):
		super(SlObj_ShapeObj, self).__init__(g)

# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-











# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-











# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
class Sl_Story (SlObj_ProgObj):
	storyC = 0
	def __init__ (self, g):
		super(Sl_Story, self).__init__(g)
		self.l_var = []
		self.l_scene = []

		self.storyC += 1
	def add_var (self, nome, val):
		pass
	def add_scene (self, nome):
		pass
	def add_media (self, nome):
		pass 
class Sl_Theme (SlObj_ProgObj):
	def __init__ (self, g):
		super(Sl_Story, self).__init__(g)
		self.l_master = []
	def add_mstr (self, nome):
		pass
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
class Sl_Layer (Sl_SlideObj):
	def __init__ (self, g):
		super(Sl_Layer, self).__init__(g)

class Sl_Slide (SlObj_FileObj):
	def __init__ (self, g):
		super(Sl_Slide, self).__init__(g)

class Sl_Master (SlObj_FileObj):
	def __init__ (self, g):
		super(Sl_Master, self).__init__(g)
		self.l_layout = []
	def add_layout (self, g):
		pass

class Sl_Layout (SlObj_FileObj):
	def __init__ (self, g):
		super(Sl_Layout, self).__init__(g)


class Sl_video (SlObj_ShapeObj):
	def __init__ (self, g):
		super(Sl_video, self).__init__(g)

class Sl_audio (SlObj_ShapeObj):
	def __init__ (self, g):
		super(Sl_audio, self).__init__(g)

class Sl_pic (SlObj_ShapeObj):
	def __init__ (self, g):
		super(Sl_pic, self).__init__(g)

class Sl_text (SlObj_ShapeObj):
	def __init__ (self, g):
		super(Sl_text, self).__init__(g)

class Sl_shape (SlObj_ShapeObj):
	def __init__ (self, g):
		super(Sl_shape, self).__init__(g)

class Sl_group (SlObj_ShapeObj):
	def __init__ (self, g):
		super(Sl_group, self).__init__(g)


# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-



bailin = Sl_Story('bailin')

bailin.add_scene('main')
bailin.add_scene('indice')

main = bailin.select_scene('main')
main.add_slide('slide 1') 
main.get_slide('slide 1').insert_video('conduzione_1_1.mov')
main.get_slide('slide 1').insert_video('esperto_1_1.mov')
main.get_slide('slide 1').insert_video('conduzione_1_2.mov')

main.add_slide('slide 2')
main.get_slide('slide 2').insert_video('conduzione_1_1_PP.mov')
main.get_slide('slide 2').insert_pic('primopiano.png')
main.formGroup( 'conduzione', ( main.get_shape('conduzione_1_1_PP'), main.get_shape('primopiano') ) )

main.add_slide('slide 3')
main.add_slide('slide 4')
main.add_slide('slide 5')

main.add_slide('FIN')
bailin.close()

# -=-=-=- # # -=-=-=- # # -=-=-=- # # -=-=-=- # # -=-=-=- # # -=-=-=- #

bailin = Wbt_paper('bailin')

bailin.add_slide('slide 1')

bailin.get_slide('slide 1').insert_video('conduzione_1_1.mov')
# {
# main.get_slide('slide 1').insert_video('conduzione_1_1.mov')
# main.get_slide('slide 1').insert_pic('bgVideo_postit.png')
# main.formGroup( 'conduzione', ( main.get_shape('conduzione_1_1'), main.get_shape('bgVideo_postit') ) )
# }

bailin.close()
# {
# main.add_slide('FIN')
# bailin.close()
# }

# -=-=-=- # # -=-=-=- # # -=-=-=- # # -=-=-=- # # -=-=-=- # # -=-=-=- #

wbt = Wbt_aiva('Special Protection')

wbt.add_slide('slide 1')
wbt.get_slide('slide 1').insert_video('conduzione_1_1.mov')
# {
# wbt.get_slide('slide 1').insert_video('conduzione_1_1.mov')
# wbt.get_slide('slide 1').insert_pic('primopiano.png')
# wbt.formGroup( 'conduzione', ( wbt.get_shape('conduzione_1_1_PP'), wbt.get_shape('primopiano') ) )
# }

wbt.close()
# {
# wbt.add_slide('FIN')
# bailin.close()
# }