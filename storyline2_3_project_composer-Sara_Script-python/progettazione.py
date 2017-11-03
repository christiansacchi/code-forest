class SlObj_FixedObj (StoryLineObj):
	def __init__ (self, g):
		super(SlObj_FixedObj, self).__init__(g)

class SlObj_ProgObj (SlObj_FixedObj):
	progC = 0

	def __init__ (self):
		# calcolo g
		super(SlObj_ProgObj, self).__init__(g)
		self.rel = self.xml+".rels"
		self.rel_list = []
		self.l_media = []

		for rel in rels:
			l_scene.append( rel.attrib )

		self.progC += 1

	def create (self):
		pass
	def open (self):
		pass
	def close (self):
		pass

	def mediaImport (self, f, type):
		pass
class Sl_Story (SlObj_ProgObj):
	storyC = 0
	def __init__ (self, nome):
		par_g = None

		if il_file_esiste(nome):
			par_g = (file_story_xml['id'], file_story_xml['pG'])
		else:
			par_g = 'story'
			copy(empty_Progect, nome)
		file_story_xml = xml(nome)

		super(Sl_Story, self).__init__(par_g) # _={ SUPER }=_
		self.l_var = []
		self.l_scene = []; self.main_scene = None

		for xml_var in self.xml.find('var'):
			self.add_var( xml=xml_var )

		for scene in self.xml.find('scene'):
			pass

		self.storyC += 1
	def add_var (self, nome=None, val=None, xml=None):
		if xml is not None:
			nome = xml['nome']
			val = xml['val']

		var = Sl_VarObj( nome, val, xml=xml)
		self.l_var.append( var )

	def add_scene (self, nome=None, xml=None):
		if xml is not None:
			nome = xml['nome']

		scena = Sl_SceneObj( nome, xml=xml) # NON ESISTE QUESTA CLASSE, BISOGNA PENSARLA
		self.l_scene.append( scena )

	def add_media (self, nome=None, xml=None):
		if xml is not None:
			nome = xml['nome']
			
		media = Sl_MediaObj( nome, xml=xml) # NON ESISTE QUESTA CLASSE, BISOGNA PENSARLA ????????
		self.l_media.append( media )

	def select_scene (self, nome):
		pass

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class SlObj_AssetObj (SlObj_FixedObj):
	def __init__ (self, g, xml):
		super(SlObj_AssetObj, self).__init__(g, xml)


class  Sl_SceneObj (SlObj_AssetObj):
	def __init__ (self, nome, val, xml=None):


		super(Sl_SceneObj, self).__init__(g)
		self.l_slide = []

		for gid_slide in self.xml.find('scene'): # Se scena vuota, non succede niente
			# xml_slide calculation
			sld = self.add_slide( xml=xml_slide ) # { nome, gid, layout }

	def add_slide(self):
		if xml is not None:
			nome = xml['nome']

		slide = Sl_Slide( nome, xml=xml) # NON ESISTE QUESTA CLASSE, BISOGNA PENSARLA
		self.l_slide.append( slide )

		return slide


class Sl_VarObj (SlObj_AssetObj):
	def __init__ (self, nome, val, xml=None):

		par_g = None
		tag_xml = None

		if xml:
			par_g = (xml['g'], xml['verG'])
			tag_xml = xml
		else:
			par_g = 'var'
			tag_xml = xml(nome, val)

		super(Sl_VarObj, self).__init__(par_g, tag_xml) # _={ SUPER }=_

		self.nome = nome
		self.val = val
'''
Ogni funzione che crea un oggetto storyline deve avere la possibilità
di crearlo da 0 o partire da un modello aperto da file.

per fare questo la funzione che crea l'oggetto deve avere un parametro
che prende una struttura xml.

da questa struttura xml saranno poi estratte le informazioni da inserire nell'oggetto python,
le quali vengono utilizzate come informazioni di accesso rapido,
senza quindi passare dall'xml e allungare il flusso di esecuzione.

'''