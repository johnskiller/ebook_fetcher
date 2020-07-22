from bs4 import BeautifulSoup, Comment
import os
SOURCE="/Users/john/Documents/诡秘之主/"
DEST="tmp/gm/"


def process_html(filename):
	soup=BeautifulSoup(open(SOURCE+filename,encoding="gbk"))
	content=soup.select("#content")
	title=soup.select("title")
	print(len(s))
	if len(s) != 1:
		print(s)

process_html('1000039.html')
#for root, dirs, files in os.walk(SOURCE):
#    for filename in files:
#        print(filename)