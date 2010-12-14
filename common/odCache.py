#!/usr/bin/env python

from time import time
import string
import odSettings

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
		
