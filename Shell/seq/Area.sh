#!/bin/bash -x
feet=1
inch=$(( 12 * feet ))
metre=`echo "0.304 * $feet" | bc`
echo "<This program gives following data"
echo "1.inch to feet conversion"
echo "2.Area of plot calculation in metresquare"
echo "3.Area of 25 such plots in acres"
read -p "Enter value in inches" value;
one_inch=`echo 1 / $inch | bc`
converted_ans=$(( `one_inch * value | bc` ))
echo $converted_ans "Feet"
len=60
bred=40
one_metre=$((`echo "1 / $metre" | bc`))
area_feet=$(( $one_metre * $len * $one_metre * $bred ))
echo "Area of rect plot is " $area_feet "sqft."
echo  "Area of 25 such plots is "
one_acre=$((43560 * $feet))
echo $(($one_acre * $area_feet * 25 |bc))
