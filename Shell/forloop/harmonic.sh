#!/bin/bash
echo Enter a number
read n
i=1
sum=0
while [ $i -le $n ]
do
sum=$(($sum + ( 10000 / $i ))) 
i=$(($i +1))
done
echo $sum/10000 | bc -l
