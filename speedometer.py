#!/usr/bin/env python

import urllib2
import time

start = time.time()


url = 'http://download.thinkbroadband.com/20MB.zip'
url = 'https://www.appelboor.com/dump/testfile20MB.bin'
url = 'https://www.appelboor.com/dump/testfile20MB.bin'
url = 'https://www.appelboor.com/dump/testfile100MB.bin'
#url = 'https://www.appelboor.com/dump/testfile500MB.bin'


download = urllib2.urlopen(url)
downloadedbytes = len(download.read())
print  "Downloaded bytes: ", downloadedbytes

end = time.time()
diff = end - start
print "Time:", diff
MBps = (downloadedbytes/1000111) / diff

mbps =  8.1 * (downloadedbytes/1000111) / diff

print("Speed in MB/s: %.2f" % MBps)
print("Speed in Mbps: %.2f" % mbps)
