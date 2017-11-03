# -*- coding: utf-8 -*-
from WbtEvo import WbtEVO
from WbtEvo import WbtPaper
from WbtEvo import WbtOLDbutGOLD
from WbtEvo import WbtUbi
from storyLineObj_plus import Sl_text, Sl_State, Sl_TrigObj
from tool import Tool

import simplejson as json
import codecs

t = Tool()
wp = None


if __name__ == "__main__" and True:
	wp = WbtUbi('progetti/Palestra RISK _UD3')

	wp.onScene(0); wp.onSlide(0)


	# 2e2b46db-dca6-4dac-a439-3d865377ba8b
	wp.var('bookmark', 0, 								('00000420-0000-4000-0000-111000000000', '00000420-0000-4099-0000-111000000000'))
	wp.var('firstPage', 1, 								('00000420-0000-4000-0000-111000000000', '00000420-0000-4099-0000-111000000000'))
	wp.var('lastPage', int(wp.get_var('numPages').val), ('00000420-0000-4000-0000-111000000000', '00000420-0000-4099-0000-111000000000'))

	wp.scene('LOADER')
	wp.curSld = wp.curScn.new_slide('Loader', wp.layouts['blank'])

	wp.f_xml.attrib['pG'] = str(wp.curScn.g)

	# -=-=-=-=-=-=-=-=- #
	bkg = wp.curSld.insert_pic("C:/christian_lavoro/wbt/__development__/__SARA__/asset/loader-layout.png", nick="loooololool")
	bkg.cord(0, 0)

	# -=-=-=-=-=-=-=-=- #
	wp.curSld.navData(False, False, False)

	txt = wp.curSld.insert_text( 'TIT CORSO', 'Titolo Corso', ['Cabin', '32', '#FFFFFF', True, False])
	txt.margin(0, 0, 0, 0)
	txt.scale(691, 62); txt.cord(15, 94)

	txt = wp.curSld.insert_text( 'UD', 'UD 01', ['Cabin', '24', '#FFFFFF', True, False])
	txt.margin(0, 0, 0, 0)
	txt.scale(691, 48); txt.cord(15, 216)

	txt = wp.curSld.insert_text( 'TIT UNITA', 'Titolo Unita', ['Cabin', '32', '#FFFFFF', True, False])
	txt.margin(0, 0, 0, 0)
	txt.scale(691, 62); txt.cord(15, 264)
	# -=-=-=-=-=-=-=-=- #

	scn_main = None
	for scn in wp.l_scene:
		if scn.nome == 'MAIN':
			scn_main = scn

	i = 1
	for sld in scn_main.l_slide:

		if sld.nome == 'BANK' or sld.nome == 'RES':
			continue

		if sld.nome == 'JOBSTOP':
			trg = Sl_TrigObj( "", wp.curSld.g )
			trg.act_setVar( wp.get_var('maxQuiz').g, i)
			trg.evt_onTmLnEnd()
			trg.condition( [wp.get_var('bookmark').g], '>', i )
			wp.curSld.f_xml.find('trigLst').insert(0, trg.f_xml )

		trg = Sl_TrigObj( "", wp.curSld.g )
		trg.act_jumpToSlide( sld.g )
		trg.evt_onTmLnEnd()
		trg.condition( [wp.get_var('bookmark').g], '==', i )
		wp.curSld.f_xml.find('trigLst').append( trg.f_xml )
		i += 1

	trg = Sl_TrigObj( "", wp.curSld.g )
	trg.act_exeJS( "carica();" )
	trg.evt_onTmLnStart()
	wp.curSld.f_xml.find('trigLst').insert(0, trg.f_xml )

	i = 1
	for sld in scn_main.l_slide:    
		if i > 1: 
			break
		trg = Sl_TrigObj( "", wp.curSld.g )
		trg.act_jumpToSlide( sld.g )
		trg.evt_onTmLnEnd()
		wp.curSld.f_xml.find('trigLst').append( trg.f_xml )
		i += 1


	'''FIILEE.find('navigationsettings').find('browsersettings').attrib['playersize'] = 'Scale'
	FIILEE.find('navigationsettings').find('resumesettings').attrib['restartresume'] = 'Never'

	optGrup = None
	for o in FIILEE.find('control_options').find('optiongroups').iter():
		if o.attrib['name'] == 'controls':
			optGrup = o.find('options')

	for o in optGrup.find('optiongroups').iter():
		if o.attrib['name'] == 'controls':
			optGrup = o.find('options')'''


	wp.curSld.save()
	wp.save(justStory=True)
