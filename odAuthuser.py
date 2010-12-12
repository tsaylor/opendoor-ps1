#!/usr/bin/env python

from time import time
import sys,string,json,hashlib
import odSettings

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
		file = str(f.read())
		self.card = json.loads(file)
	
	def printCard(self):
		print json.dumps(self.card,sort_keys=True,indent=4)

class odLocalCache:
	def __init__(self):
		self.__internal = dict()

	def add(self,tuple):
		self.__internal[tuple[0]] = (tuple[1],tuple[2])
	
	def get(self,uid):
		print self.__internal[uid]
		return self.__internal[uid]
	
	def cleanExpired(self):
		current_time = int(time())
		for key in self.__internal.iterkeys():
			deltatime = current_time - int(self.__internal[key][1])
			if ( odSettings.OD_CACHE_TIME*60*60 < deltatime ):
				del self.__internal[key]
	
	def isExpired(self,key):
		current_time = int(time())
		deltatime = current_time - int(self.__internal[key][1])
		if ( odSettings.OD_CACHE_TIME*60*60 < deltatime ):
			return True
		else:
			return False

	def exists(self,key):
		if (key in self.__internal):
			return True
		else:
			return False
		
authtoken = odCard(sys.argv[1])
cache = odLocalCache()
print authtoken.card['data']['uid']
if ( cache.get(authtoken.card['data']['uid'])[0] == authtoken.card['meta']['pgp-signature'] ):
	if not cache.isExpired(authtoken.card['data']['uid']):
		exit(0)

cache.add((authtoken.card['data']['uid'],authtoken.card['meta']['pgp-signature'],time()))
