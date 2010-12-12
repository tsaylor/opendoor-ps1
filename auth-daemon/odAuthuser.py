#!/usr/bin/env python

from time import time
import sys,string,json,hashlib,urllib2
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
		self.card = json.loads(str(f.read()))
	
	def printCard(self):
		print json.dumps(self.card,sort_keys=True,indent=4)

class odCache:
	def __init__(self):
		self.cache = dict()

	def add(self,uid,stamped_sig):
		self.cache[uid] = (stamped_sig[0],stamped_sig[1])
	
	def get(self,uid):
		if self.exists(uid):
			return self.cache.get(uid,None)
	
	def cleanExpired(self):
		current_time = int(time())
		for key in self.cache.iterkeys():
			deltatime = current_time - int(self.cache[key][1])
			if ( odSettings.CACHE_TIME*60*60 < deltatime ):
				del self.cache[key]
	
	def isExpired(self,key):
		current_time = int(time())
		deltatime = current_time - int(self.cache[key][1])
		if ( odSettings.CACHE_TIME*60*60 < deltatime ):
			return True
		else:
			return False

	def exists(self,key):
		if (key in self.cache):
			return True
		else:
			return False
		
authtoken = odCard(sys.argv[1])
cache = odCache()

cache.add(authtoken.card['data']['uid'],(authtoken.card['meta']['pgp-signature'],time()))

if cache.exists(authtoken.card['data']['uid']):
	if not cache.isExpired(authtoken.card['data']['uid']):
		if ( cache.get(authtoken.card['data']['uid'])[0] == authtoken.card['meta']['pgp-signature'] ):
			print "USER IS AUTHORIZED"
			exit (0)
			
url = authtoken.card['data']['url']
url = url + '/opendoor/user/'+ authtoken['data']['uid']
response = urllib2.urlopen(url).read()
authorizetoken = json.loads(response)

if authorizetoken.
