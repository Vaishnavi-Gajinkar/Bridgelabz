#!/bin/bash -x

a=$1
b=$2
c=$3

calc1=$(( a + b * c ))
calc2=$(( a % b + c ))
calc3=$(( c + a / b ))
calc4=$(( a * b + c ))

max=$calc1

for i in ' $calc1 , $calc2 , $calc3, $calc4 '
do
	if [[ $i -gt $max ]];
	then
		
