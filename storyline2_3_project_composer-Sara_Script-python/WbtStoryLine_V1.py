
class SlObj_PhisicsObj (StoryLineObj):
	""" Qualunque oggetto abbia una time-line """
	Phisics_c = 0
	def __init__ (self, g):
		super(SlObj_PhisicsObj, self).__init__(g)
		self.Phisics_c += 1
		self.time = 5000

class SlObj_AbstractObj (StoryLineObj):
	""" Oggetto senza time-line """
	Abstract_c = 0
	def __init__ (self, g):
		super(SlObj_AbstractObj, self).__init__(g)
		self.Abstract_c += 1

class SlObj_AssetsFile (SlObj_PhisicsObj):
	Assets_c = 0
	def cord2StoryCord ():
		pass
	def __init__ (self, loc):
		self.x = None
		self.y = None
		self.w = None
		self.h = None

# slide = SlObj_ProjObj('dfdf', 'slideee')
class SlObj_ProjFile (SlObj_PhisicsObj):
	ProjObj_c = 0
	def chkName (file):
		if len(file) >= 4:
			if file[-4:] != '.xml':
				return "{0}.xml".format(file)
	def __init__ (self, file, g, name):
		super(SlObj_ProjFile, self).__init__(g)
		self.ProjObj_c += 1

		self.name = name

		self.fileName = self.chkName(file)
		self.file = self.tools.xmlOpen(self.fileName)
		self.fileRoot = self.tools.getAsset(self.file)
		self.fileRel = self.tools.xmlOpen("{0}.rels".format(self.fileName))
		self.fileRelRoot = self.tools.getAsset(self.fileRelRoot)

		self.shapes = []
		self.shapeLst = self.fileRoot.find('shapeLst')
		self.trigs = []
		self.trigLst = self.fileRoot.find('trigLst')

	def save (self):
		self.file._setroot(self.fileRoot)		# RIMPIAZZO DELLA ROOT
		self.fileRel._setroot(self.fileRelRoot)	# RIMPIAZZO DELLA ROOT
		self.tools.xmlClose(self.file, "{1}".format("", self.fileName))
		self.tools.xmlClose(self.fileRel, "{1}.rels".format("", self.fileName), isRels=True)

	def addShape (self):
		pass

# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-

class SlObj_Slide (SlObj_ProjFile):
	slide_c = 0
	def __init__ (def, file, name, layoutG):
		super(SlObj_Slide, self).__init__(file, self.gidGen.get('slide'), name)
		self.slide_c += 1

		self.layoutG = layoutG

		# WORK IN FILE
		sld = self.fileRoot
		sld.attrib['name'] = self.name
		sld.attrib['id'] = '0'
		sld.attrib['g'] = self.g
		sld.attrib['verG'] = self.verG
		sld.attrib['layoutG'] = self.layoutG

