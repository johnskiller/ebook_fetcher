#!/bin/bash

url='http://www.99reader.cn/files/article/html/2/2098/'
base=`basename $0 .sh`


echo $base

rm -rf index.html
wget ${url}index.html

grep html index.html > allurls.txt
./parseIndex.py 0 $url
