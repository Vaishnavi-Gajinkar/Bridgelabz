#!/bin/bash
echo Enter a Number:
read n
f=1
echo factors are:
for ((i=1;i<=$n;i++));
do 
	if [[ $(($n % $i)) -eq 0 ]]
	then
		echo $i
	fi
done
