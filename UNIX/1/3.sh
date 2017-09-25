#!/bin/bash
if test $# -lt 1
then
    echo "More args"
    exit
fi
sum=0
count=0
for arg in $@
do
	((sum=sum+arg))
	((count=count+1))
done
echo "Avg = " $(bc <<< "scale=2; $sum / $count")