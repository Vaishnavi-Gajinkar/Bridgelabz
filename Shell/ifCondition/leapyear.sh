#!/bin/bash -x

read -p "Enter a year" year
temp=year

while [[ $temp -ne 0 ]];
do
	temp=$(($temp/10))
	count=$(($count+1))
done

if [[ $count -eq 4 ]];
then
	if [[ $year%4 -eq 0 ]];
	then
		if [[ $year%100 -eq 0 ]];
		then
			if [[ $year%400 -eq 0 ]]
			then
				flag=1
			else
				flag=0
			fi
		else
			flag=1
		fi
	else
		flag=0
	fi
else
	echo "Enter valid year"
fi

if [[ $flag -eq 1 ]];
then
	echo "Leap Year!"
else
	echo "Non-Leap Year!"
fi
