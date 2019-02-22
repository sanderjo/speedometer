#!/usr/bin/env python

import urllib2
import time

start = time.time()

url = 'http://download.thinkbroadband.com/100MB.zip'
url = 'http://download.thinkbroadband.com/20MB.zip'
url = 'http://download.thinkbroadband.com/5MB.zip'

#url = 'https://www.appelboor.com/dump/testfile20MB.bin'
#url = 'https://www.appelboor.com/dump/testfile100MB.bin'
#url = 'https://www.appelboor.com/dump/testfile500MB.bin'

req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
download = urllib2.urlopen(req, timeout=4).read()
downloadedbytes = len(download)

#download = urllib2.urlopen(url)
#downloadedbytes = len(download.read())
print  "Downloaded bytes: ", downloadedbytes

end = time.time()
diff = end - start
#print "Time:", diff
print("Time: %.2f" % diff)

MBps = (downloadedbytes/1000111) / diff # Bytes
mbps =  8.05 * MBps # bits

print("Speed in MB/s: %.2f" % MBps)
print("Speed in Mbps: %.2f" % mbps)
