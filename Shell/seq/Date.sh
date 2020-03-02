#1/bin/bash -x
echo $1
m=$1
d=$2
y=$3
y0=$(( y - ( 14 - m ) / 12))
x=$((y0 + y0 / 4 - y0 / 100 + y0 / 400))
m0=$((m + 12 * ((14 - m) / 12) -2))
d0=$(((d + x + 31 * m0 / 12) % 7))
echo $d0
declare -A arr
arr["0"]=Sunday
arr+=(["1"]=Monday ["2"]=Tuesday ["3"]=Wednesday ["4"]=Thursday ["5"]=Friday ["6"]=Saturday)
echo ${ arr[${d0}] } 
