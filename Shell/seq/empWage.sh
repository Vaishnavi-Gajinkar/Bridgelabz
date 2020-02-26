#!/bin/bash -x
isPresent=1;
randomCheck=$((RANDOM%3));
bool=False

isFulltime=1
isParttime=2
wage_rate=20
working_hrs=0
if [ $randomCheck -eq $isFulltime ];
then
	working_hrs=8
#	salary=$(($wage_rate * $working_days | bc))
elif [ $randomCheck -eq $isParttime ];
then
	working_hrs=4
else
	working_hrs=0
fi
$salary=$wage_rate*$working_hrs

echo "Employee salary is " $salary

