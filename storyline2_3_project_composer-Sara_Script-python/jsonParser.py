# -*- coding: utf-8 -*-
import simplejson as json

js = "C:/christian_lavoro/wbt/_b_docebo_bcc/antiriciclaggio/config/config.json"

with open(js) as data_file:

	data = data_file.read()
	print type(data)

	data2 = json.loads(data)
	print data2
	print type(data2)