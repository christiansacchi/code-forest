# -*- coding: utf-8 -*-
from WbtEvo import WbtEVO
from WbtEvo import WbtPaper
from WbtEvo import WbtOLDbutGOLD
from WbtEvo import WbtUbi
from storyLineObj_plus import Sl_text, Sl_State
from tool import Tool

import simplejson as json
import codecs

t = Tool()
wp = None

# -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # 
# -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # 

if __name__ == "__main__" and False:

	wp = WbtPaper('progetti/AQuestaCondizione -19-')

	wp.onScene(0)
	wp.onSlide(0)

	wp.slide('Lorem ipsum dolor sit amet!')
	wp.video("meidainfo/conduzione_01.mp4", "cond_01")

	wp.save()

# -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # 
# -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # 

if __name__ == "__main__" and False:

	wp = WbtPaper('progetti/Evoluzione Tecnologia')

	videoPerSld = 2
	titoli = [
		None, "Gli strumenti di pagamento", "Il contante", "Strumenti alternativi", "Assegno bancario", "Il bonifico bancario",
		"L'addebito diretto", "Le rimesse di denaro", "Carte di pagamento", "Le carte di credito", "Carte di debito",
		"Carte prepagate", "New Digital Payment", "Il Mobile Payments", "E-Wallet", "Electronic Payment", "Contactless Payment",
		"Il comportamento di acquisto del consumatore", "Matrice di Assael", "Il comportamento successivo all'acquisto"
	]

	wp.onScene(0)
	wp.onSlide(0)

	for i in range(1, 20):

		wp.slide(titoli[i])

		videoName = "C:/christian_lavoro/wbt_storyline_locale/15_12 - Evoluzione Tecnologica/"
		videoName += "vid_{0:02}.mov".format(i)

		wp.video(videoName, "att_{0:02}".format(i))

		if i in (9, 11, 15):
			videoName = "C:/christian_lavoro/wbt_storyline_locale/15_12 - Evoluzione Tecnologica/"
			videoName += "vid_{0:02}_{1}.mov".format(i, videoPerSld)

			wp.video(videoName, "att_{0:02}".format(i+1))

		print "# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #\n"

	wp.save()

# -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # 
# -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # 

if __name__ == "__main__" and False:

	wp = WbtOLDbutGOLD('progetti/OLDGOLD -23')
	wp.onScene(0)
	wp.onSlide(0)

	wp.slide('TITOLOOOOOO 1')
	wp.slide('TITOLOOOOOO 2')
	wp.slide('TITOLOOOOOO 3')
	wp.slide('TITOLOOOOOO 4')
	wp.slide('TITOLOOOOOO 5')
	wp.slide('TITOLOOOOOO 6')


	wp.save()

# -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # 
# -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # 

if __name__ == "__main__" and False:
	wp = WbtOLDbutGOLD('progetti/fattistrada 1999')
	wp.onScene(0)
	wp.onSlide(0)

	env = "C:/christian_lavoro/wbt_storyline_locale/04_01 - fatti strada storyline/fattistrada_RELEASE"
	js = "{0}/config/config.json".format(env)

	jsStr = None
	# codecs.open(js, )
	with codecs.open(js, 'rb', encoding='utf-8', errors='replace') as data_file:
		data = data_file.read()

		jsStr = json.loads(data)
		# print jsStr

		for i in range(1, 24+1):
			s = "p{0}".format(i)

			tipo = jsStr['config']['pagine'][s]['tipologia']['id']
			if tipo == 'video':
				titolo = jsStr['config']['pagine'][s]['titolo']
				titVideo = jsStr['config']['pagine'][s]['tipologia']['sources']['s0']['file']

				wp.slide(titolo)
				wp.video("{0}/media/videos/{1}".format(env, titVideo), "video")

			else:
				wp.jobstop()

		for i in range(1, 2+1):
			a = "a{0}".format(i)
			tit = jsStr['config']['approfondimenti'][a]['titolo']
			aprf = jsStr['config']['approfondimenti'][a]['file']
			wp.approfondimento(tit, "{0}/media/approfondimenti/{1}".format(env, aprf))

	wp.save()

# -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # 
# -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=- # 



if __name__ == "__main__" and False:
	wp = WbtUbi('progetti/UBI 12')
	wp.onScene(0)
	wp.onSlide(0)

	wp.layer('mario')
	wp.layer('antonio')
	wp.layer('franco')
	wp.layer('cicco')
	wp.layer('francula')

	jb = {
		'domanda':"QUANTI PESCI CI VOGLIONO PER AVVITARE UNA LAMPADINA?",
		'g':"42",
		's':"39"
	}
	
	wp.jobstop('PRIMOOOOOOOOOOOOOOO', 'VF', jb)
	wp.slide_RES('RES_1')
	
	wp.jobstop('SECONDOOOOOOOOOOO', 'VF', jb)
	wp.slide_RES('RES_2')
	


	jb1 = {
	'domanda':"QUALE E' LA DOMANDA ALLA RISPOSTA FONDAMENTALE SULLA VITA, L'UNIVERSO E TUTTOQUANTO?",
	'g':"Quante strade dove percorrere l'uomo?",
	's1':u"Qual'è il seme dell'universo?",
	's2':"Non ne ho idea, ma DON'T PANIC.",
	's3':"La risposta si trova a pagina 42 della 'Guida Galattica per Autostoppisti'."
	}
	jb2 = {
		'domanda':"DOMANDA 2",
		'g':"GIUSTO",
		's1':"SBAGLIATO",
		's2':"SBAGLIATO",
	}
	jb3 = {
		'domanda':"DOMANDA 2",
		'g':"GIUSTO",
		's1':"SBAGLIATO",
		's2':"SBAGLIATO",
	}

	wp.JobStop()
	wp.BnkJobStop('JOB 1', 'MC', jb1)
	wp.BnkJobStop('JOB 2', 'MC', jb2)
	wp.BnkJobStop('JOB 3', 'MC', jb3)

	wp.slide("SONO MHARIO!")

	wp.jobstop('JIOBBE STOP 1', 'MC', jb1)

	wp.slide("SONO LUIGI!")

	wp.link_slide()

	wp.save()

tits = [u"Introduzione",
u"L’agenzia Studi e progetti",
u"Il bilancio di esercizio",
u"Il bilancio – le norme del codice civile",
u"L’ammortamento di un bene",
u"++jobstop--",
u"I principi di redazione",
u"Il problema della competenza",
u"I principi di redazione II",
u"Le finalità del bilancio"]
jb1 = {
	'domanda':u"Proviamo a rispondere: A quale obbligo devono rispondere le società di capitali dopo la redazione del bilancio:",
	'g':u"Devono depositarlo presso il registro delle imprese",
	's1':u"Devono pubblicarlo su almeno due quotidiani nazionali",
	's2':u"Devono trasmetterlo per raccomandata a tutti gli azionisti."
}
if __name__ == "__main__" and False:
	env = "C:/christian_lavoro/wbt_storyline_locale/16_01 - Contabilita - Cattolica/cantabilita_bilancio"

	wp = WbtUbi('progetti/Contabilita_Bilancio_UD01')
	wp.onScene(0)
	wp.onSlide(0)

	wp.slide("Copertina")

	titVideo = 2
	for i in tits:

		if i == "++jobstop--":
			wp.jobstop('JOBSTOP', 'VF', jb1)
		else:
			wp.slide(i)
			if titVideo != 2:
				wp.videoSx("{0}/T2_{1:02}.mov".format(env, titVideo), "T2")
			wp.videoDx("{0}/T1_{1:02}.mov".format(env, titVideo), "T1")
			
		titVideo += 1

	wp.slide_FIN()
	wp.link_slide()
	wp.save()





tits = [u"L’analisi dei risultati",
u"i portatori di interesse",
u"Lo stato patrimoniale",
u"Lo stato patrimoniale II",
"BANK",
u"il conto economico",
u"I ricavi dell’agenzia",
u"il risultato economico",
u"Ciclo attivo e passivo",
u"il gestionale",
u"il piano dei conti",
u"i costi dell’agenzia"]
jb2 = {
	'domanda':u"Indica se attivo o passivo: Mobilio, attrezzature, computer, stampanti",
	'g':"Attivo",
	's1':"Passivo"
}
jb3 = {
	'domanda':u"Indica se attivo o passivo: Mutuo per l’acquisto dell’immobile dell’agenzia",
	's1':"Attivo",
	'g':"Passivo"
}
jb4 = {
	'domanda':u"Indica se attivo o passivo: Leasing per l’acquisto di computer",
	'g':"Nessuno dei due",
	's1':"Passivo",
	'sg':"Attivo"
}
jb5 = {
	'domanda':u"Indica se attivo o passivo: Rivalsa",
	'g':"Attivo",
	's1':"Passivo"
}
jb6 = {
	'domanda':u"Proviamo a rispondere: Che cosa rappresentano i beni/diritti nello stato patrimoniale?",
	'g':u"Rappresentano lo stato Attivo",
	's1':u"Rappresentano lo stato Passivo",
	's2':u"Rappresentano l’utile d’esercizio"
}
if __name__ == "__main__" and False:
	env = "C:/christian_lavoro/wbt_storyline_locale/16_01 - Contabilita - Cattolica/cantabilita_bilancio"

	wp = WbtUbi('progetti/Contabilita_Bilancio_UD02')
	wp.onScene(0)
	wp.onSlide(0)

	titVideo = 12
	for i in tits:

		if i == "BANK":
			wp.JobStop()
			wp.BnkJobStop('JOB 1', 'MC', jb2)
			wp.BnkJobStop('JOB 2', 'MC', jb3)
			wp.BnkJobStop('JOB 3', 'MC', jb4)
			wp.BnkJobStop('JOB 4', 'MC', jb5)
			wp.BnkJobStop('JOB 5', 'MC', jb6)
		else:
			wp.slide(i.upper())
			wp.videoSx("{0}/T2_{1:02}.mov".format(env, titVideo), "T2")
			wp.videoDx("{0}/T1_{1:02}.mov".format(env, titVideo), "T1")
			
		titVideo += 1

	wp.slide_FIN()
	wp.link_slide()
	wp.save()

if __name__ == "__main__" and False:
	env = "C:/christian_lavoro/wbt_storyline_locale/30_01 - MiFID modifiche"

	wp = WbtUbi('progetti/MIFID new')
	wp.onScene(0)
	wp.onSlide(0)

	videos = [
		'1_2.mov',
		'1_3.mov',
		'1_4.mov',
		'1_5.mov',
		'1_6.mov',
		'2_1.mov',
		'2_2.mov',
		'3_1.mov',
		'4_1.mov',
		'4_2.mov',
		'4_3.mov',
		'4_4.mov',
		'4_5.mov',
		'4_6.mov',
		'1.mov',
		'2.mov',
		'3.mov',
		'4.mov',
		'5.mov',
		'6.mov'
	]

	for v in videos:
		wp.slide('tit', navbar=False)
		wp.videoDx("{0}/{1}".format(env, v), "VID")

	wp.save()

if __name__ == "__main__" and False:
	titoli = [u"DAL BILANCIO CONTABILE AL BILANCIO GESTIONALE",
	"JOB",
	u"RICLASSIFICARE IL CONTO ECONOMICO",
	u"RICLASSIFICARE IL CONTO ECONOMICO II",
	u"IL CRITERIO MARGINE DI CONTRIBUZIONE",
	u"IL CRITERIO MARGINE DI CONTRIBUZIONE II",
	"JOB",
	u"STRUMENTO DI GESTIONE",
	u"LO STRUMENTO DI RICLASSIFICAZIONE PER L'AGENZIA",
	u"LA REMUNERAZIONE DELL'AGENTE",
	"JOB",
	u"I COSTI DI FUNZIONAMENTO",
	"JOB",
	u"RICLASSIFICARE LO STATO PATRIMONIALE",
	u"IL CRITERIO FINANZIARIO",
	"JOB",
	u"SINTESI: RICLASSIFICAZIONE DELLO STATO PATRIMONIALE",
	u"VOCI EVIDENZIATE",
	"JOB",
	u"CONTO ECONOMICO STESURA",
	"JOB",
	u"RISULTATO DELLA STESURA DEL CONTO ECONOMICO",
	u"CONTO ECONOMICO DELL'AGENZIA STUDI E PROGETTI S.R.L.",
	"JOB",
	u"STESURA DELLO STATO PATRIMONIALE",
	u"STESURA DELLO STATO PATRIMONIALE II",
	"JOB",
	u"PUBBLICAZIONE DEL BILANCIO",
	u"ROI",
	u"IL CALCOLO DEL ROI",
	u"ROE",
	u"CONFRONTO TRA AZIENDE",
	"JOB",
	u"SINTESI"]

	wp = WbtUbi('progetti/Contabilita_Bilancio_UD03_TITOLI')
	wp.onScene(0)
	wp.onSlide(0)

	for t in titoli:
		if t == "JOB":
			wp.jobstop('JOBSTOP', 'VF', jb1)
		else:
			wp.slide(t, navbar=False)

	wp.save()

if __name__ == "__main__" and True:
	wp = WbtUbi('progetti/prova_temp_02')
	wp.onScene(0)
	wp.onSlide(0)

	wp.videoDx("C:/christian_lavoro/wbt_storyline_locale/08_02 - Businnes Planning - Cattolica/video/1_T2.mov", "VID")

	wp.save()