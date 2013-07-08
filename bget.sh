#!/bin/bash

# surls.txt is a file contans full urls
base=$1
ref=$2

echo $base, $ref
# mkdir html_$base
cd html_$base

for f in `cat surls.txt`
 do
 wget $f --header="User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.0.16" --referer="$ref"
# sleep 5
done
