#!/usr/bin/env python

import sys,json


class odCard:
	def __init__(self,file):
		try: 
			f = open(file,'r')
			self.parseCard(f)
			self.authorization = dict()
    		except IOError as (errno, strerror):
    			print "I/O error({0}): {1}".format(errno, strerror)
		except:
			print "Unexpected error:", sys.exc_info()[0]
    			raise
	
	def parseCard(self,f):
		self.card = json.loads(str(f.read()))
	
	def printCard(self):
		print json.dumps(self.card,sort_keys=True,indent=4)

