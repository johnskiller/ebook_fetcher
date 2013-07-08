#!/bin/bash

url='http://www.shumilou.com/doukai/'
base=`basename $0 .sh`


echo $base
cd html_$base

rm -rf index.html
wget ${url}index.html

grep html index.html > allurls.txt
../parseIndex.py 0 $url
