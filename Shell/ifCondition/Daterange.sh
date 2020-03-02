#!/bin/bash 

read -p "Enter date " date
read -p  "Enter month " month
flag=0

if [[ $month -ge 3 && $month -le 6 ]];
then
	if [[ $month -eq 3 ]];
	then
		if [[ $date -ge 20 && $month -le 31 ]];
		then
			flag=1
		fi
	elif [[ $month -eq 4 ]];
	then
		if [[ $date -ge 1 && $date -le 30 ]];
		then
			flag=1
		fi
	elif [[ $month -eq 5 ]];
	then
		if [[ $date -ge 1 && $date -le 31 ]];
		then
			flag=1
		fi
	else
		if [[ $date -ge 1 && $date -le 20 ]];
		then
			flag=1
		fi
	fi
else
	flag=0
fi

if [[ $flag -eq 1 ]];
then
	echo "Date in range"
else
	echo "Date out of range"
fi
