#!/bin/bash -x

val1=$((RANDOM%99+1))
lower_limit=10
upper_limit=99
diff=$(($upper_limit-$lower_limit+1))

for (( i=1; i<=5; i++))
do
	rand_val=$(($((RANDOM%$diff))+$lower_limit))
	score=$(($score+$rand_val))
done

echo "Sum of 5 two digit numbers is "$score
