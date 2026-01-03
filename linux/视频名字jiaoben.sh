#!/bin/bash
#索引提取脚本
#Author：pokes（pokes@163.com）
#注意：需要先安装yum -y install dos2unix

mulu=mp4suoyin009

mkdir $mulu
cat 4501596.txt | awk -F'\' '{print $NF}'>1.txt
sed 's/ /-/g' 1.txt>2.txt
dos2unix 2.txt


for var in $(cat 2.txt)
        do
                touch $mulu/$var >nul
        done

tar -cvf $mulu.tar $mulu
