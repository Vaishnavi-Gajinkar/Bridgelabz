#!/bin/bash -x

read -p "Enter a number between 1-7" digit


if [[ $digit -eq 1 ]];
then
        echo "Sunday"
elif [[ $digit -eq 2 ]];
then
        echo "Monday"
elif [[ $digit -eq 3 ]];
then
        echo "Tuesday"
elif [[ $digit -eq 4 ]];
then
        echo "Wednesday"
elif [[ $digit -eq 5 ]];
then
        echo "Thursday"
elif [[ $digit -eq 6 ]];
then
        echo "Friday"
elif [[ $digit -eq 7 ]];
then
        echo "Saturday"
else
	echo "Invalid number"
fi
