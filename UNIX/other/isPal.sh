#!/bin/bash
if test $# -lt 1
then
	echo "Enter string!"
	exit
fi
n=${#1}
((hn=$n/2))
pal='True'
for i in `seq 0 $hn`
do
	if test ${1:$i:1} != ${1:$n-$i-1:1}
	then
		pal='False'
		break
	fi
done
echo $pal