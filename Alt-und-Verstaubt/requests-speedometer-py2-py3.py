#!/usr/bin/env python

#import urllib2	# python2 only
import time

import requests


# Thinkbroad offers: 

'''
url = 'http://download.thinkbroadband.com/1GB.zip'
url = 'http://download.thinkbroadband.com/512MB.zip'
url = 'http://download.thinkbroadband.com/200MB.zip'
url = 'http://download.thinkbroadband.com/100MB.zip'
url = 'http://download.thinkbroadband.com/50MB.zip'
url = 'http://download.thinkbroadband.com/20MB.zip'
url = 'http://download.thinkbroadband.com/10MB.zip'
url = 'http://download.thinkbroadband.com/5MB.zip'
'''

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

	print("URL is", url)

	start = time.time()

	'''
	req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
	download = urllib2.urlopen(req, timeout=4).read()
	downloadedbytes = len(download)
	'''
	#download = urllib2.urlopen(url)
	#downloadedbytes = len(download.read())

	#url = 'http://download.thinkbroadband.com/10MB.zip'
	r = requests.get(url, allow_redirects=True)
	downloadedbytes = len(r.content)

	print("Downloaded bytes: ", downloadedbytes)

	end = time.time()
	duration = end - start
	#print "Time:", duration
	#print("Time: %.2f" % duration)

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
Based the first download, do a bigger download; the biggest download that still fits in 5 (or 10) seconds
If the 5MB doenload took 0.3 seconds, you can do a 15 times bigger download, so about 75 MB
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



