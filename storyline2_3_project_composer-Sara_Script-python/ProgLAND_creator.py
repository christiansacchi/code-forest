# -*- coding: utf-8 -*-
from WbtEvo import WbtLAND
from storyLineObj_plus import Sl_text, Sl_State
from tool import Tool

import codecs
import csv

t = Tool()
wp = None

# Nuove norme sulla distribuzione assicurativa

if __name__ == "__main__":

	def videoName (x, y, z):
		idd = x.strip().replace(" ", "").replace("\t", "")
		number = int(y.strip().replace(" ", "").replace("\t", ""))
		abc = z.strip().replace(" ", "").replace("\t", "")
		return "{0}{1:04d}{2}.mp4".format(idd, number, abc)

	def WBT ():
		wp = None

		f1 = codecs.open('C:/Users/Christian/Desktop/progLand_struttura_pt3.csv', 'r', encoding='utf-8', errors='replace')
		# f1 = open('C:/Users/Christian/Desktop/progLand_struttura.csv', 'rb')
		f1_reader = csv.reader(f1, delimiter='\t')

		Cwbt = CSld = CeSld = 0

		for row in f1_reader:

			if row[0] == 'FIN':
				break

			if CSld == 0:
				Cwbt += 1

				wp = WbtLAND("C:/Users/Christian/Desktop/progetto LAND/LAND_UD{0:02d}_NEW NEW".format(Cwbt), 'Nuove norme sulla distribuzione assicurativa')
				wp.onScene(0); wp.onSlide(0)
				wp.trig_pageNumber(wp.c_sld)
				logo = wp.curSld.insert_pic("__slide masters__/LAND_asset/logo.png", nick="logo")
				logo.scale(73, 73); logo.cord(266, 480)
				logo.StartTime(0); logo.retiming(0, 5000, shw_tilEnd=True)

				#wp.slide('Copertina', layout='copertina')

			if row[0] == '': # or CSld == 1
				wp.slide_FIN()
				logo = wp.curSld.insert_pic("__slide masters__/LAND_asset/logo.png", nick="logo")
				logo.scale(73, 73); logo.cord(266, 397)
				logo.StartTime(0); logo.retiming(0, 5000, shw_tilEnd=True)
				wp.link_slide()
				wp.save()
				CSld = CeSld = 0
				continue

			if row[0] in ('IDD', 'REG'):
				CSld += 1

				# row[0] ===> IDD/REG
				# row[1] ===> VIDEO NUMBER
				# row[2] ===> PILL LETTER
				# row[3] ===> NumberOfEs, SOLO SE row[2][0] E' "E"
				# row[4] ===> TITOLO SLIDE

				# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
				# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- # # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

				if row[2].strip().replace(" ", "").replace("\t", "")[0] == 'E':
					wp.JobStop()
					continue
				
				CeSld += 1
				vname = videoName(row[0], row[1], row[2])
				sldname = row[4]

				wp.slide(sldname)
				wp.video("C:/Users/Christian/Desktop/progetto LAND/compressed/{0}".format(vname), "video") # , pi=pi

				#if abc[0] == 'B':
				print vname
				# print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"


		print "{0} == {1}".format(CeSld, (45+29-1+27))

		f1.close()

	WBT()