# -*- coding: utf-8 -*-

# ASSETs
# gid = Gid(); gid.get()
# gid = Gid(); gid.get("slide")
# gid = Gid(); gid.get("slide", True)

import random

class gidError (Exception):
	def __str__(self):
		return "gidError"
class gEnotContext (gidError):
	def __str__(self):
		return "gEnotContext"

class Gid (object):
	scene = 0
	slide = 0
	shapes = 0
	media = 0
	var = 0; tit = 0
	trig = 0
	text = 0
	timeProbe = 0
	group = 0
	state = 0
	quiz = 0
	altro = 0
	mids = []

	def __init__ (self):
		self.struct = { "head":0, "mid1":0, "mid2":0, "mid3":0, "foot":0 }

	def resetStruct (self):
		self.struct = { "head": 0, "mid1":0, "mid2":0, "mid3":0, "foot":0 }

	def compose (self):
		gid = "{head:08x}-{mid1:04x}-{mid2:04x}-{mid3:04x}-{foot:012x}"
		gid = gid.format(	head=self.struct["head"],
							mid1=self.struct["mid1"],
							mid2=self.struct["mid2"],
							mid3=self.struct["mid3"],
							foot=self.struct["foot"]	)
		return gid

	''' 0000 0000 - 0000 - 4000 - 0000 - 0000 0000 0000 '''


	def iD (self, type):
		# "R5{0:010x}".format(self.SlideCounter).upper()
		id = None
		if type != None:
			if type == "media":
				id = "R6{0:08x}{1:02x}".format(self.media, 1).upper()
			else:
				raise gEnotContext

		return id

	def make (self, head, mid1, mid3, foot, mid2=0):
		self.struct["head"] = head
		self.struct["mid1"] = mid1
		self.struct["mid2"] = 16384 + mid2 # 4000
		self.struct["mid3"] = mid3
		self.struct["foot"] = foot

		friz = self.compose()
		self.struct["mid2"] = 16537 # 4099, id of a verG
		frez = self.compose()
		friz_and_frez_friends_4ever = (friz, frez)

		return friz_and_frez_friends_4ever

	def set (self, type, num):
		if type == "slide":
			self.slide += num
		elif type == "media":
			self.media += num
		elif type == "var":
			self.var += num
		elif type == "tit":
			self.tit += num
		elif type == "trig":
			self.trig += num
		elif type == "text":
			self.text += num
		elif type == "scene":
			self.scene += num
		elif type == "timeProbe":
			self.timeProbe += num
		elif type == "group":
			self.group += num
		else:
			raise gEnotContext

	def get (self, type=None, verG=False):
		self.resetStruct()
		if type != None:
			self.struct["mid2"] = 16384 # 4000
		
			if type == "slide":
				self.slide += 1
				self.struct["head"] = self.slide
				self.struct["foot"] = 17592186044416 	# (100000000000)16 = (17592186044416)10
			elif type == "media":
				self.media += 1
				self.struct["head"] = self.media + 4026531840 # (F0000000)16 = (4026531840)10
				self.struct["foot"] = 18691697672192 	# (110000000000)16 = (18691697672192)10
			elif type == "var":
				self.var += 1
				self.struct["head"] = self.var
				self.struct["foot"] = 18760417148928 	# (111000000000)16 = (18760417148928)10
			elif type == "tit":
				self.tit += 1
				self.struct["head"] = self.tit
				self.struct["foot"] = 187604171489280 	# (AAA000000000)16 = (187604171489280)10
			elif type == "trig":
				self.trig += 1
				self.struct["head"] = self.trig
				self.struct["foot"] = 18764712116224	# (111100000000)16 = (18764712116224)10
			elif type == "text":
				self.text += 1
				self.struct["head"] = self.text + 2952790016 # (B0000000)16 = (2952790016) 10
				self.struct["foot"] = 18764980551680 	# (111110000000)16 = (18764980551680)10
			elif type == "scene":
				self.scene += 1
				self.struct["head"] = self.scene
				self.struct["foot"] = 18764997328896 	# (111111000000)16 = (18764997328896)10
			elif type == "timeProbe":
				self.timeProbe += 1
				self.struct["head"] = self.timeProbe
				self.struct["foot"] = 18764998377472 	# (111111100000)16 = (18764998377472)10
			elif type == "group":
				self.group += 1
				self.struct["head"] = self.group + 2684354560 # (A0000000)16 = (2684354560) 10
				self.struct["foot"] = 186916976721920 	# (AA0000000000)16 = (186916976721920)10
			elif type == "state":
				self.group += 1
				self.struct["head"] = self.group
				self.struct["foot"] = 187604171489280 	# (AAA000000000)16 = (187604171489280)10
			elif type == "quiz":
				self.quiz += 1
				self.struct["head"] = self.quiz + 2881486848 # (ABC00000)16 = (2881486848) 10
				self.struct["foot"] = 188841122070528 	# (ABC000000000)16 = (188841122070528)10
			elif type == "altro":
				self.altro += 1
				self.struct["head"] = self.altro + 2881486848 # (CCC00000)16 = (3435134976) 10
				self.struct["foot"] = 188841122070528 	# (CCC000000000)16 = (225125005787136)10
			else:				raise gEnotContext

			if verG and False:
				self.struct["mid2"] = 16537 # 4099, id of a verG

		# -=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=- #
		
		while True:
			mid1 = random.randint(0, 65535)
			if mid1 in self.mids:
				continue
			self.mids.append(mid1)
			break
		self.struct["mid1"] = mid1

		# -=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=- #

		friz = self.compose()
		self.struct["mid2"] = 16537 # 4099, id of a verG
		frez = self.compose()
		friz_and_frez_friends_4ever = (friz, frez)

		# print friz_and_frez_friends_4ever

		return friz_and_frez_friends_4ever











