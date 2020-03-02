read -p "Enter a digit: " num
while [[ $num -gt 0 ]];
do
	num=$(($num/10))
	count=$(($count+1))
done

case "$count" in
"1") echo unit
;;
"2") echo Ten
;;
"3") echo Hundred
;;
"4") echo Thousand
;;
"5") echo Ten Thousand
;;    
esac
