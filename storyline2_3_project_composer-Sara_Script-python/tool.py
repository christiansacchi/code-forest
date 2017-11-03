# -*- coding: utf-8 -*-

import copy
import xml.etree.ElementTree as Xml
import shutil
import os
from os import listdir
from os.path import isfile, join
import subprocess
import StringIO
import random
from datetime import datetime

class Tool (object):
	"""def __init__ (self):
		self.infoCount = 0
		self.LogCount = 0
		self.warningCount = 0
		self.ErrorCount = 0"""

	def videoConverter (self, input, output):
		#print input
		# envffmpeg = "ffmpeg 64bit/bin/ffmpeg_v1"
		envffmpeg = "ffmpeg"
		#envffmpeg = "ffmpeg_v1"
		cmd = '''"{exe}" -i "{_input}" -vcodec h264 -pix_fmt yuv420p -acodec aac -ar 44100 -ac 1 -ab 128k -strict -2 "{_output}"'''
		cmd = cmd.format(_input=input, _output=output, exe=envffmpeg)
		
		#res = os.system(cmd)
		res = subprocess.call(cmd, shell=True)

		return cmd, res
	def videoInfo (self, input):
		# envffprob = "ffmpeg 64bit/bin/ffprobe"
		envffprob = "ffprobe"
		# mediainfo.exe conduzione_01.mov
		# cmdErr = ''' "{exe}" -v error "{_input}" '''
		cmd1 = ''' "{exe}" -v error -show_format "{_input}" '''
		cmd2 = ''' "{exe}" -v error -show_streams "{_input}" '''
		# cmdPic = "ffprobe -v error -show_format -show_streams cubi.PNG"

		info = {}

		cmd = cmd1.format(_input=input, exe=envffprob)
		res = subprocess.check_output(cmd, shell=True)
		res = res.split('\n')
		for l in res:
			l = l.rstrip('\n'); l = l.rstrip('\r'); l = l.split('=')
			if l[0] not in ('duration', 'size', 'bit_rate'):
				continue
			info[l[0]] = l[1]
		if info['duration'] != 'N/A': # duration and bit_rate are N/A if a img is analized
			n = info['duration'].split('.')
			info['duration'] = int( (int(n[0])*1000) + (int(n[1])/1000) )

		# -=-=-=-=-=- # # -=-=-=-=-=- # # -=-=-=-=-=- # # -=-=-=-=-=- # 
		# -=-=-=-=-=- # # -=-=-=-=-=- # # -=-=-=-=-=- # # -=-=-=-=-=- # 
		
		cmd = cmd2.format(_input=input, exe=envffprob)
		res = subprocess.check_output(cmd, shell=True)
		res = res.split('\n')
		for l in res:
			l = l.rstrip('\n'); l = l.rstrip('\r'); l = l.split('=')
			if l[0] not in ('width', 'height'):
				continue
			info[l[0]] = l[1]
		info['width'] = int(info['width'])
		info['height'] = int(info['height'])

		return info

	def joke_loading (self, low, high):
		return random.randint(low, high)

	def printINFO (self, str):
		if hasattr(self, 'infoCount'):
			self.infoCount += 1
		else:
			self.infoCount = 1
		print "INF({0:2}) -> {1}".format(self.infoCount, str)
	def printLOG (self, str):
		if hasattr(self, 'LogCount'):
			self.LogCount += 1
		else:
			self.LogCount = 1
		print "LOG({0:2}) -> {1}".format(self.LogCount, str)
	def printWARN (self, str):
		if hasattr(self, 'warningCount'):
			self.warningCount += 1
		else:
			self.warningCount = 1
		print "WAR({0:2}) -> {1}".format(self.warningCount, str)
	def printERR (self, str):
		if hasattr(self, 'ErrorCount'):
			self.ErrorCount += 1
		else:
			self.ErrorCount = 1
		print "ERR({0:2}) -> {1}".format(self.ErrorCount, str)
	def printSYS (self, str):
		if hasattr(self, 'SysCount'):
			self.SysCount += 1
		else:
			self.SysCount = 1
		print "SYS({0:2}) -> {1}".format(self.SysCount, str)

	def xmlOpen (self, nome):
		return Xml.parse(nome)
	def xmlClose (self, f, nome, isRels=False):
		if isRels == True:
			Xml.register_namespace('', 'http://schemas.openxmlformats.org/package/2006/relationships')
		f.write(nome, encoding="utf-8", xml_declaration=True)
	def xmlGetRoot (self, xml):
		return xml.getroot()
	def xmlTag (self, nome, attrib):
		return Xml.Element(nome, attrib)
	def xmlShowBranch (self, branch):
		print Xml.dump( branch )
	def xmlGetBranch (self, branch):
		return Xml.tostring( branch )
	def xmltoTextedXml (self, xml):
		xml = self.xmlGetBranch( xml )
		#xml = xml.replace("<", "&lt;")
		#xml = xml.replace(">", "&gt;")
		xml = xml.replace("\t", "")
		xml = xml.replace("\n", " ")
		return xml
	def xmlBranchInfo (self, branch):
		print "{>---<} BRANCH INFO {>---<}"
		if branch is not None:
			print "branch Node: {0}".format( branch.tag )
			print "branch Attribs: {0}".format( len(branch.attrib) )
			print "branch Sons: {0}".format( len(branch) )
		else:
			print "branch is None"
		print "{>-----------------------<}"
	def xmlIsBranch(self, xml):
		return isinstance(xml, type(Xml.Element))
	def xmlIsRoot(self, xml):
		return isinstance(xml, type(Xml))

	def copia (self, obj):
		return copy.deepcopy(obj)
	def clone (self, obj):
		return copy.copy(obj)
	def ctrlC_ctrlV (self, ctrlC, ctrlV):
		return shutil.copytree(ctrlC, ctrlV)
	def dir (self, path):
		return [path+f for f in listdir(path) if isfile(join(path, f))]
	def dir2 (self, path):
		return [path+f for f in listdir(path)]
	def ctrlC_ctrlV_file (self, ctrlC, ctrlV):
		return shutil.copy(ctrlC, ctrlV)
	def path_assoluto (self, f):
		return os.path.abspath(f)
	def rinomina (self, fS, fE):
		return os.rename(fS, fE)
	def fileExist (self, path):
		return os.path.isfile(path)
	def dirExist (self, path):
		return os.path.isdir(path) 

	def takeAsset(self, f):
		return self.copia( self.xmlGetRoot( self.xmlOpen(f) ) )
	def getAsset(self, f):
		return self.copia( self.xmlGetRoot( f ) )

	def pressToContinue(self):
		self.printSYS("Press to continue")
		raw_input(">")

	def now (self):
		return str(datetime.now())

	def replaceAccentiVocali(self, text):
		text = text.replace("&amp;", "&")
		# ############################### #
		text = text.replace("&aacute;",u"á")
		text = text.replace("&Aacute;",u"Á")
		text = text.replace("&agrave;",u"à")
		text = text.replace("&Agrave;",u"À")
		# ############################### #
		text = text.replace("&eacute;",u"é")
		text = text.replace("&Eacute;",u"É")
		text = text.replace("&egrave;",u"è")
		text = text.replace("&Egrave;",u"È")
		# ############################### #
		text = text.replace("&iacute;",u"í")
		text = text.replace("&Iacute;",u"Í")
		text = text.replace("&igrave;",u"ì")
		text = text.replace("&Igrave;",u"Ì")
		# ############################### #
		text = text.replace("&oacute;",u"ó")
		text = text.replace("&Oacute;",u"Ó")
		text = text.replace("&ograve;",u"ò")
		text = text.replace("&Ograve;",u"Ò")
		# ############################### #
		text = text.replace("&uacute;",u"ú")
		text = text.replace("&Uacute;",u"Ú")
		text = text.replace("&ugrave;",u"ù")
		text = text.replace("&Ugrave;",u"Ù")
		return text