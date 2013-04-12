#!/bin/bash

url='http://www.baikv.com/xiaoshuo/12/12404/'
base=`basename $0 .sh`


echo $base

rm -rf index.html
wget ${url}index.html

grep html index.html > allurls.txt
./parseIndex.py 0 $url
./bget.sh $base $url
