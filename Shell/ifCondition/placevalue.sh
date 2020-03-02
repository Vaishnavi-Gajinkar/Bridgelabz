#!/bin/bash -x

read -p "Enter a number" num

while [[ $num -gt 0 ]];
do
	num=$(($num/10))
	count=$(($count+1))
done

if [[ $count -eq 1 ]];
then
	echo "Unit number"
elif [[ $count -eq 2 ]];
then
	echo "Tens number"
elif [[ $count -eq 3 ]];
then
	echo "Hundreds number"
elif [[ $count -eq 4 ]];
then
	echo "Thousands number"
elif [[ $count -eq 5 ]];
then
	echo "TenThousands number"
elif [[ $count -eq 6 ]];
then
	echo "Lakhs number"
elif [[ $count -eq 7 ]];
then
	echo "TenLakhs number"
elif [[ $count -eq 8 ]];
then
	echo "Crore number"
elif [[ $count -eq 9 ]];
then
	echo "TenCrore number"
elif [[ $count -eq 10 ]];
then
	echo "Billion number"
else
	echo "NAN"
fi
