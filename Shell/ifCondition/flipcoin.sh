#!/bin/bash -x

read -p "enter number of times to flip the coin" n

while [[ i -lt $n ]];
do
	rand=$(($RANDOM % 2 ))
	if [[ $rand -eq 1 ]];
	then
		echo "Tails"
		heads=$(( heads + 1 ))
	else
		echo "Heads"
		tails=$(( tails + 1 ))
	fi
	i=$(( $i + 1 ))
done

headcount=$(($heads * 100 / $n))
tailcount=$(($tails * 100 / $n))

echo "Heads percentage = " $headcount
echo "Tail percentage = " $tailcount
