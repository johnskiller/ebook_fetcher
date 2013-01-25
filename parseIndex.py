#!/usr/bin/env python

import re,sys

def getLastNum():
	last = 0
	if len(sys.argv) > 1:
		last = int(sys.argv[1])

	return last
	
def output(last):

	p=re.compile('(\d{7})\.html')
	for line in open('allurl.txt').readlines():
		m=p.search(line)
		if m and int(m.group(1)) > last:
			print m.group(0), m.group(1) 


output(getLastNum())
