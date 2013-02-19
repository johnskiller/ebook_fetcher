#!/bin/bash

url='http://www.woqudu.com/files/article/html/2/2216/'
base=`basename $0 .sh`


echo $base

rm -rf index.html
wget ${url}index.html

grep html index.html > allurls.txt
./parseIndex.py 0 $url
