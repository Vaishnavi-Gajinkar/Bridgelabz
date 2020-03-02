#!/bin/bash 
read -p "Enter a range of prime number: " number
for ((j=2;j<$number;j++))
do
    i=2
    flag=0
    while [ $i -le $(($j / 2)) ]
    do
        if [[ $(($j % $i)) -eq 0 ]]
        then
            flag=1
            break
        else
            flag=0
        fi

        i=`expr $i + 1`
    done 
    if [[ $flag -eq 0 ]]
        then
        echo "Prime number is: $j"
    fi
done
