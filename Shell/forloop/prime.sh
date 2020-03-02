#!/bin/bash -x
primefactor()
{
    number=$1
i=2
flag=0
while [ $i -le $(($number / 2)) ]
do
if [[ $(($number % $i)) -eq 0 ]]
then
flag=1
fi

i=`expr $i + 1`
done 
if [[ $flag -eq 1 ]]
then
echo "The number is Not Prime"
else
echo "The number is Prime"
fi
}

read -p "Enter a number: " number
primefactor $number
