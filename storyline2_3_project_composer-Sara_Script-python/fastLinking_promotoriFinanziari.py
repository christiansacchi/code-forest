from storyLineObj_plus import Sl_Story, Sl_TrigObj

wbt = None
scn = None
sld = None
# -=-=-=-=-=-=-=-=- #
trg_pN = None
trg_pPrv = None
trg_pNxt = None

wbt = Sl_Story("____conversione_WBTvideo_WBTstoryline____/AREA3_normativa_C10 - V2", "42 IS NOT SIMPLY A NUMBER!")
scn = wbt.l_scene[0]

for i in range(len(scn.l_slide)):

	print i

	sld = scn.l_slide[i]

	trg_pN = Sl_TrigObj( "", sld.g )
	trg_pN.act_setVar( wbt.get_var('pageNumber').g, i+1 )
	trg_pN.evt_onTmLnStart()
	sld.addTrig(trg_pN)

	if i >= 2:
		if sld.f_xml.attrib['name'] == "":
			trg_pNxt = Sl_TrigObj( "", sld.g )
			trg_pNxt.act_jumpToNext( )
			trg_pNxt.evt_onTmLnEnd()
			sld.addTrig(trg_pNxt)
			continue

		if scn.l_slide[i-1].f_xml.attrib['name'] == "":
			sld.f_xml.find('navData').attrib['prev'] = "true"
			sld.f_xml.find('navData').attrib['next'] = "true"

			trg_pPrv = Sl_TrigObj( "", scn.l_slide[i].g )
			trg_pPrv.act_jumpToSlide( scn.l_slide[i-2].g )
			trg_pPrv.evt_onClick('prev')
			sld.addTrig(trg_pPrv)
			if i < len(scn.l_slide)-1:
				trg_pNxt = Sl_TrigObj( "", sld.g )
				trg_pNxt.act_jumpToSlide( scn.l_slide[i+1].g )
				trg_pNxt.evt_onClick('next')
				sld.addTrig(trg_pNxt)
			continue

	sld.f_xml.find('navData').attrib['prev'] = "true"
	sld.f_xml.find('navData').attrib['next'] = "true"

	if i != 0:
		trg_pPrv = Sl_TrigObj( "", sld.g )
		trg_pPrv.act_jumpToSlide( scn.l_slide[i-1].g )
		trg_pPrv.evt_onClick('prev')
		sld.addTrig(trg_pPrv)

	if i < len(scn.l_slide)-1:
		trg_pNxt = Sl_TrigObj( "", sld.g )
		trg_pNxt.act_jumpToSlide( scn.l_slide[i+1].g )
		trg_pNxt.evt_onClick('next')
		sld.addTrig(trg_pNxt)

wbt.save()