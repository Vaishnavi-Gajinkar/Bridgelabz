#!/bin/bash
read -p "Enter number of day: " d0
if [[ $d0 -le 6 ]]
then

    case "$d0" in
    "0") echo Sunday ;;
    "1") echo Monday ;;
    "2") echo Tuesday ;;
    "3") echo Wednesday;;
    "4") echo Thusday ;;    
    "5") echo Friday ;;
    "6") echo Saturday ;;
    esac
else
    echo not a valid input
fi
