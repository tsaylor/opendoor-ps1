#!/usr/bin/env python

from time import time
import sys,string,json,hashlib,urllib2
from common.odCard import odCard
from common.odCache import odCache
from common.odSettings import *

authtoken = odCard(sys.argv[1])
cache = odCache()

uid = authtoken.card['data']['uid']
authurl = authtoken.card['resa']['authurl']
sig = authtoken.card['meta']['sig-all']

# If the user has an unexpried entry in the local cache with the same pgp
# signature the user is authenticated


if cache.exists(uid):
	if not cache.isExpired(uid):
		if ( cache.get(uid)[0] == sig ):
			print "USER IS AUTHENTICATED"
			exit (0)
			

