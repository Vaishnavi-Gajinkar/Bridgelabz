#!/bin/bash
read -p "Give a value " num
echo "1) Feet to Inch"
echo "2) Feet to Meter"
echo "3 Inch to Feet"
echo "4) Meter to Feet"
read -p "Choice the converter " c
case $c in
    1) res=$((12*$num))
    ;;
    2) res=`echo "scale=2; 0.305*$num" | bc`
    ;;
    3) res=`echo "scale=2; 0.0833*$num" | bc`
    ;;
    4) res=`echo "scale=2; 3.28*$num" | bc`
    ;;
esac
echo $res 
