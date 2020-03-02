#!/bin/bash -x
read -p "enter the value of n: " n
i=0
pow=0
while [ $pow -lt 256 ]
do
    pow=$((2**$i))
    echo Power 2 ^ $i is: $pow
    i=$(($i+1))
done
