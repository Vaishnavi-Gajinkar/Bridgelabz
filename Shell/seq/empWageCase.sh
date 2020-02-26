#!/bin/bash -x
fulltime=1
parttime=2
wageRate=20

empCode=$((RANDOM%3))

case $empCode in 
	$fulltime)
		empHrs=8;;
	$parttime)
		empHrs=4;;
	*)
	empHrs=0;;
esac

salary=$(($wageRate*$empHrs));

echo "Emp salary is " $salary
