# -*- coding: utf-8 -*-
from storyLineObj_plus import Sl_Story, Sl_TrigObj
from tool import Tool

# -=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=- #

env = "/Volumes/P0RTABL3/Documents/"
env = "C:/christian_lavoro/wbt/__development__/"


def scene_slideNum (story):
	for scn in story.l_scene:
		nome = scn.nome
		if scn.nome == '':
			nome = "Untitled_Slide"
		print nome, len(scn.l_slide)
	print "TOTALE: ", story.get_slideTotalNumber()


if __name__ == "__main__":
	if True:
		s = Sl_Story('{0}__SARA__/progetti/PicPicPic 010'.format(env), 'paper')

		# -=-==-=-=-=-=-=- SLD 2 -=-=-=-=-=-=-=-=- #
		s.l_scene[0].new_slide('SLD 2'); s.new_var("item01P", 0); s.new_var("item01T", '...')

		varItm = s.get_var('item01P')
		trg = Sl_TrigObj( "", s.l_scene[0].l_slide[0].g )
		trg.act_setVar( varItm.g, 1 )
		trg.evt_onTmLnStart()
		s.l_scene[0].l_slide[0].addTrig(trg)

		v1 = s.l_scene[0].l_slide[0].insert_video("meidainfo/conduzione_01.mp4", nick="cond_01")
		v1.playOnTrig()
		trg = Sl_TrigObj( "", v1.g )
		trg.act_playMedia( v1.g, 'video' )
		trg.evt_onTmLnStart()
		v1.addTrig(trg)
		# -=-==-=-=-=-=-=- SLD 2 -=-=-=-=-=-=-=-=- #

		s.l_scene[0].new_slide('SLD 3')
		s.l_scene[0].new_slide('SLD 4')

		fromG = s.l_scene[0].l_slide[0]
		for toG in s.l_scene[0].l_slide[1:]:

			nome = 'jmp2_{0}_{1}'.format(fromG.nome, toG.nome)
			trg = Sl_TrigObj( nome, fromG.g )
			trg.act_jumpToSlide( toG.g )
			trg.evt_onClick( 'next' )

			print nome
			fromG.addTrig( trg )

			nome = 'jmp2_{0}_{1}'.format(toG.nome, fromG.nome)
			trg = Sl_TrigObj( nome, toG.g )
			trg.act_jumpToSlide( fromG.g )
			trg.evt_onClick( 'prev' )

			print nome
			toG.addTrig( trg )

			print "-=-=-=-=-=-=-=-=-=-=-=-=-"
			fromG = toG

		#s.importPic( "meidainfo/cubi.PNG", nick="cubiPNG" )
		#s.importPic( "meidainfo/Cattura.PNG", nick="CatturaPNG" )
		s.l_scene[0].l_slide[0].insert_pic("meidainfo/cubi.PNG", nick="cubiPNG")
		s.l_scene[0].l_slide[1].insert_pic("meidainfo/cubi.PNG", nick="cubiPNG")

		s.save()

	if False:
		s = Sl_Story('{0}__SARA__/progetti/Forme Finanziamento 01'.format(env), 'sara')
		s.new_var( "NEW_VAR_01", 420 )
		s.new_var( "NEW_VAR_02", True )
		s.new_var( "NEW_VAR_03", "Python, or not Python: that is the proplem." )
		s.l_scene[0].l_slide[0].insert_video("meidainfo/conduzione_01.mp4", nick="conduzione_01")
		s.l_scene[0].l_slide[0].insert_video("meidainfo/gestore_11.mov", nick="gestore_11")
		s.save()
		
	if False:
		envir = 'c:/christian_lavoro/wbt_storyline_locale/02_12 - Forme di finanziamento - OAM (CRAsti)'
		s = Sl_Story('{0}/Forme Finanziamento 02'.format(envir), 'paper')
		s.l_scene[0].l_slide[0].insert_video('{0}/video/vid_01.mov'.format(envir), nick="vid_01")
		s.l_scene[0].l_slide[0].insert_video('{0}/video/vid_02.mov'.format(envir), nick="vid_02")
		s.save()
		
	if False:
		s = Sl_Story('{0}__SARA__/progetti/djent'.format(env), 'ubi')
		s.l_scene[0].new_slide('Slide_01---')
		s.l_scene[0].new_slide('Slide_02---')
		s.l_scene[0].new_slide('Slide_03---')

	t = Tool()
	t.pressToContinue()
