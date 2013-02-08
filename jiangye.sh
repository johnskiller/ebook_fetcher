#!/bin/bash

url='http://www.baikm.com/xiaoshuo/11/11686/'

rm -rf index.html
wget ${url}index.html

grep html index.html > allurls.txt
./parseIndex.py 5427700 $url
