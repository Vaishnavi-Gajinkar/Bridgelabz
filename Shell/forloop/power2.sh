#!/bin/bash -x
echo Enter the range
read n
echo 2^n values are:
for i in `seq $n`
do
    echo power of 2 ^ $i is: $((2**$i))
done
