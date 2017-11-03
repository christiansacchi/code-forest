'''
# ###################################################################### #
# #### INPUT 	 ####################################################### #
# ###################################################################### #

# Trova gli aggiornamento cercando la stringa di testo: [{) -=- The News -=- ()}]

def scene_slideNum ():
	for scn in s.l_scene:
		nome = scn.nome 
		if scn.nome == '':
			nome = "Untitled_Slide"
		print nome, len(scn.l_slide)
	print "TOTALE: ", s.get_slideTotalNumber()

env = "/Volumes/P0RTABL3/Documents/"
env = "C:/christian_lavoro/wbt/__development__/"

if False:
	# s = Sl_Story('C:\\christian_lavoro\\wbt\\__development__\\__SARA__\\asset\\__esperimenti__\\layer')
	s = Sl_Story('{0}__SARA__/progetti/djent'.format(env), 'ubi')
	# s.l_scene[0].l_slide[0]
	s.l_scene[0].new_slide('Slide_01---')
	s.l_scene[0].new_slide('Slide_02---')
	s.l_scene[0].new_slide('Slide_03---')
	s.save()

if False:
	s1 = Sl_Story('{0}__SARA__/progetti/Evviva_01'.format(env), 'aviva')
	s1.l_scene[0].new_slide('-=-=-=-=-=-=- 1')
	s1.l_scene[0].new_slide('-=-=-=-=-=-=- 2')
	s1.l_scene[0].new_slide('-=-=-=-=-=-=- 3')
	s1.save()
if False:
	s2 = Sl_Story('{0}__SARA__/progetti/SARA_01'.format(env), 'sara')
	s2.l_scene[0].new_slide('SLIDEEE 1')
	s2.l_scene[0].new_slide('SLIDEEE 2')
	s2.l_scene[0].new_slide('SLIDEEE 3')
	s2.save()

if True:
	s = Sl_Story('{0}__SARA__/progetti/VideCLIPPER_01'.format(env), 'sara')
	# print "1 - NumOfSlide: {0}".format(s.gidGen.slide), print "2 - NumOfSlide: {0}".format(s.gidGen.slide)
	s.new_var( "NEW_VAR_01", 420 )
	s.new_var( "NEW_VAR_02", True )
	s.new_var( "NEW_VAR_03", "Python, or not Python: that is the proplem." )
	s.l_scene[0].l_slide[0].insert_video("meidainfo/conduzione_01.mp4", nick="conduzione_01")
	s.save()
	

t.pressToContinue()
'''