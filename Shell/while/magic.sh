#!/bin/bash -x
echo "think of a number between 1 to 100"
l=0
u=100
while [ $u -gt '0' ]
do
	guess=$(( ( u + l ) / 2 ))
	echo $guess
	read -p "Is it the correct number? y/n" ans
	if [[ $ans -eq 'y' ]];
	then
		break
	elif [[ $ans -eq 'n' ]];
	then
		read -p "type s if number is smaller than or g if its greater than guessed number" ans
		if [[ $ans -eq "s" ]];
		then
			l=$l
			u=$guess
		elif [[ $ans -eq "g" ]];
		then
			l=$guess
			u=$u
		fi
	else
		echo "Invalid input"
		break
	fi
done
echo "Congrats! We guessed your number"

