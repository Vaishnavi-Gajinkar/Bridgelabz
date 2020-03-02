#!/bin/bash 
max=0
declare -A arr
for ((i=1;$i<=5;$((i++))))
do
	arr[$i]=$((RANDOM%999+100));
	echo ${arr[$i]}
	if [ ${arr[$i]} > $max ];
	then
		max=${arr[$i]}
	fi
done
echo $max
