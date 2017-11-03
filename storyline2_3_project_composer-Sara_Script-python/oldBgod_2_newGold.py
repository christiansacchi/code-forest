# -*- coding: utf-8 -*-
from WbtEvo import WbtEVO
from WbtEvo import WbtPaper
from WbtEvo import WbtOLDbutGOLD
from WbtEvo import WbtOLDbutUBI
from storyLineObj_plus import Sl_text, Sl_State
from tool import Tool

import simplejson as json
import codecs

t = Tool()
wp = None

if __name__ == "__main__":

	def WBT_WBT_WBT(n, e, OLDbut='GOLD', importVideo_Offset=0):
		wp =  None
		if OLDbut == 'GOLD':
			wp = WbtOLDbutGOLD(n)
		elif OLDbut == 'UBI':
			wp = WbtOLDbutUBI(n)

		wp.inportedVd = importVideo_Offset

		wp.onScene(0); wp.onSlide(0)
		wp.trig_pageNumber(wp.c_sld)

		#env = "C:/christian_lavoro/wbt_storyline_locale/04_01 - fatti strada storyline/fattistrada_RELEASE"
		#env = "C:/xampp/htdocs/dashboard/sfide_intermediazione"
		env = e
		f_json = "{0}/config/config.json".format(env)

		with codecs.open(f_json, 'rb', encoding='utf-8', errors='replace') as data_file:
			data = data_file.read()
			jsn = json.loads(data)

			jsn_pages = jsn['config']['pagine']

			print "jns_paes: {0}".format(len(jsn_pages)+1)
			
			numPages = len(jsn_pages)+1
			# numPages = 3
			for i in range(1, numPages):

				p = jsn_pages['p{0}'.format(i)]

				tit = p['titolo']
				tipo = p['tipologia']['id']

				if tipo == 'video':
					titV = p['tipologia']['sources']['s0']['file']
					pi = "{0}/{1}".format(env, p['tipologia']['poster'][3:])
					wp.slide(tit)
					wp.video("{0}/media/videos/{1}".format(env, titV), "video") # , pi=pi

				elif tipo in ['test', 'test_random', 'test_fin', 'test_finale']:
					titQ = p['tipologia']['configfile']
					xml_tst = t.xmlOpen( "{0}/test/{1}".format(env, titQ) )
					xml_tst = t.xmlGetRoot(xml_tst)

					wp.JobStop()
					s_count = 1
					for d in xml_tst.iter('item'):
						# {'domanda':u"QUESITO 1: Il quesito è giusto o sbagliato?", 'g':"GIUSTO", 's':"SBAGLIATO"}
						quest = {}
						quest['domanda'] = d.find('stem').text
						for o in d.find('options').iter('option'):
							if o.attrib['value'] == '1':
								quest['g'] = o.text
							else:
								quest['s_{0}'.format(s_count)] = o.text
							s_count += 1

						wp.BnkJobStop('domanda', 'MC', quest) 
						# SE VOGLIO COMBIARE LO STYLE, NON POSSO FARLO TRAMITE PARAMETRI,
						# DEVO ANDARE NELLA FUNZIONE DI CREAZIONE DELLA DOMANDA (NELLA CLASSE Sl_Slide IN storyLineObj_plus.py)

				elif tipo == 'testo':
					wp.slide(tit)

				else:
					pass

			jsn_apprf = jsn['config']['approfondimenti']
			for i in range(1, 2+1):
				a = jsn_apprf["a{0}".format(i)]

				tit = a['titolo']
				aprf = a['file']
				wp.approfondimento(tit, "{0}/media/approfondimenti/{1}".format(env, aprf))


		wp.slide_FIN()

		wp.link_slide()

		wp.save()


	# WBT_WBT_WBT("previdenza_pubblica_complementare_1", "C:/christian_lavoro/wbt_storyline_locale/__NEW & GOLD__/previdenza_pubblica_complementare_1")
	
	# WBT_WBT_WBT("previdenza_pubblica_complementare_2", "C:/christian_lavoro/wbt_storyline_locale/__NEW & GOLD__/previdenza_pubblica_complementare_2")

	# WBT_WBT_WBT("previdenza_pubblica_complementare_3", "C:/christian_lavoro/wbt_storyline_locale/__NEW & GOLD__/previdenza_pubblica_complementare_3")

	# WBT_WBT_WBT("Sfide Intermediazione Assicurativa", "C:/xampp/htdocs/dashboard/sfide_intermediazione")

	# WBT_WBT_WBT("____conversione_WBTvideo_WBTstoryline____/multiramo_QUEST_2", 
	#			"____conversione_WBTvideo_WBTstoryline____/multiramo")


	WBT_WBT_WBT("____conversione_WBTvideo_WBTstoryline____/PPC1_CONVS",
				"____conversione_WBTvideo_WBTstoryline____/PPC1", 'UBI', importVideo_Offset=0)

	WBT_WBT_WBT("____conversione_WBTvideo_WBTstoryline____/PPC2_cnvs",
				"____conversione_WBTvideo_WBTstoryline____/PPC2", 'UBI', importVideo_Offset=16)

	WBT_WBT_WBT("____conversione_WBTvideo_WBTstoryline____/PPC3_cnvs",
				"____conversione_WBTvideo_WBTstoryline____/PPC3", 'UBI', importVideo_Offset=32)

	# GOTO 	
	# def importVideo (self, f, nick):
	#	vid_nameSpace = self.censimentoVd[self.inportedVd]; self.inportedVd += 1
	# self.inportedVd start from 25

	# PPC1 3
	# PCC2 2
	# PCC3 2

	t.pressToContinue()

