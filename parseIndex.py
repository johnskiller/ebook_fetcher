#!/usr/bin/env python

import re,sys
url=''

def getLastNum():
	last = 0
	print "sys.argv ",len(sys.argv)
	if len(sys.argv) > 1:
		last = int(sys.argv[1])
	if len(sys.argv) > 2:
		url = sys.argv[2]
		print url
		print "last=",last,"url=",url
	return (last,url)
	
def output(last,url):
	print "last=",last,"url=",url
	f=open('surls.txt')
	p=re.compile('(\d{7})\.html')
	for line in open('allurls.txt').readlines():
		m=p.search(line)
		if m and int(m.group(1)) > last:
			#print "%s/%s   %s"%(url,m.group(0), m.group(1)) 
			f.write("%s/%s",(url,m.group(0)))
			pass

	f.close()

last,url = getLastNum()
output(last,url)
