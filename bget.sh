#!/bin/bash

for f in `cat surls.txt`
 do
 wget $f --header="User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.0.16" --referer="http://www.baikm.com"
# sleep 5
done
