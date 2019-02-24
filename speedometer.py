#!/usr/bin/env python3

import sys
import time

# Thinkbroad offers: 

v = [
[ 5, 'http://download.thinkbroadband.com/5MB.zip' ],
[ 10, 'http://download.thinkbroadband.com/10MB.zip' ],
[ 20, 'http://download.thinkbroadband.com/20MB.zip' ],
[ 50, 'http://download.thinkbroadband.com/50MB.zip' ],
[ 100, 'http://download.thinkbroadband.com/100MB.zip' ],
[ 200, 'http://download.thinkbroadband.com/200MB.zip' ],
[ 512, 'http://download.thinkbroadband.com/512MB.zip' ]
]


# FWIW:
# url = 'http://ipv4.download.thinkbroadband.com/10MB.zip'
# url = 'http://ipv6.download.thinkbroadband.com/10MB.zip'

#url = 'https://www.appelboor.com/dump/testfile20MB.bin'
#url = 'https://www.appelboor.com/dump/testfile100MB.bin'
#url = 'https://www.appelboor.com/dump/testfile500MB.bin'


def measurespeed(url):

	# Download the specified url, and report back MB/s and Mbps

	print("URL is %s" % url)
	start = time.time()
	if sys.version_info[0] == 2:
		import urllib2	# python2 only
		req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
		downloadedbytes = len(urllib2.urlopen(req, timeout=4).read())
	elif sys.version_info[0] == 3:
		import urllib.request
		req = urllib.request.Request(url, data=None, headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh)' })
		downloadedbytes = len(urllib.request.urlopen(req,timeout=4).read())
	else:
		print("ERROR: no python version?!")
		return 0, 0

	print("Downloaded bytes: %d" % downloadedbytes)

	duration = time.time() - start

	MBps = (downloadedbytes/1000111) / duration # Bytes
	mbps =  8.05 * MBps # bits
	return MBps, mbps



############### MAIN #######################



# Do basic test

print("Basic measurement, with small download:")
urlbasic = v[0][1]
MBps, mbps = measurespeed(urlbasic)
print("Speed in MB/s: %.2f" % MBps)
print("Speed in Mbps: %.2f" % mbps)


'''
Based the first download, do a bigger download; the biggest download that still fits in 10 seconds
Rationale: a bigger download could yield higher MB/s because the 'starting delay' is relatively less
Calculation: 
If the 5MB download took 0.3 seconds, you can do a 30 times bigger download, so about 150 MB, will round to 100 MB
'''

print("\n\nMeasurement with bigger download, doable within 10 seconds")
maxtime = 10 # seconds

URLtoDO = None
for size,sizeurl in v:

	expectedtime = size / MBps
	#print(size,sizeurl, expectedtime)
	if expectedtime < maxtime:
		# ok, this one is feasible, so keep it in mind
		URLtoDO = sizeurl

if URLtoDO:
	print(URLtoDO)
	MBps, mbps = measurespeed(URLtoDO)
	print("Speed in MB/s: %.2f" % MBps)
	print("Speed in Mbps: %.2f" % mbps)



