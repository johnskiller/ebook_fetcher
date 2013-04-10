#!/bin/bash

url='http://www.blygo.com/xiaoshuo/1/1389/'
base=`basename $0 .sh`


echo $base

rm -rf index.html
wget ${url}index.html

grep html index.html > allurls.txt
./parseIndex.py 0 $url
./bget.sh $base $url
