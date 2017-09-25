#!/bin/bash
if test $# -lt 3
then
    echo "A op B"
    exit
fi
case $2 in 
	"+")
		echo $((($1+$3)))
	;;
	"-")
		echo $((($1-$3)))
	;;
	"x")
		echo $((($1*$3)))
	;;
	"/")
		if test $3 -eq 0
		then
			echo "Cannot divide by zero"
		else
			echo $((($1/$3)))
		fi
	;;
	"%")
		if test $3 -eq 0
		then
			echo "Cannot divide by zero"
		else
			echo $((($1%$3)))
		fi
	;;
	*)
		echo "Invalid operand"
esac