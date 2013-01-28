#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup, Comment
VALID_TAGS = {'html': [],
              'head': [],
              'p': [],
              'body': [],
              'title': [],
              'h1': [],
              'br': [],
              #'a': ['href', 'title'],
              'div':['id']
              }
FILE='html/4966416.html'

def sanitize_html(value, valid_tags=VALID_TAGS):
    soup = BeautifulSoup(value,'lxml')
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    [comment.extract() for comment in comments]
    # Some markup can be crafted to slip through BeautifulSoup's parser, so
    # we run this repeatedly until it generates the same output twice.
    newoutput = soup.renderContents()
    while 1:
        oldoutput = newoutput
        soup = BeautifulSoup(newoutput,'lxml')
        for tag in soup.findAll(True):
            if tag.name not in valid_tags:
                tag.hidden = True
            else:
		if tag.name == 'div' and tag.attrs.get(u'id','') != u'content':
			tag.hidden = True
        newoutput = soup.renderContents()
        if oldoutput == newoutput:
            break
    return newoutput

def filte(file=FILE):
	v=open('html/%s'%file).read()
	f=open('newhtml/%s'%file,'w+')
    	f.write(sanitize_html(v))
	f.close()

def test():
	v=open(FILE).read()
	soup = BeautifulSoup(v)
	cont=soup.findAll('div',attrs={'id':'content'})
	print cont

def loop_all():
	import os
	for f in os.listdir('html'):
		filte(f)


loop_all()
	
