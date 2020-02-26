#!/bin/bash -x
is_fullTime=1
is_partTime=2
wageRate=20
totaldays=22

for (( date=1; date<=$totaldays; date++))
do
	empCode=$((RANDOM%3));
	if [ $empCode -eq $is_fullTime ];
	then
		empHrs=8
	elif [ $empCode -eq $is_partTime ];
	then
		empHrs=4
	else
		empHrs=0
	fi
	salary=$(($wageRate*$empHrs))
	total_sal=$(($total_sal+$salary))
done
