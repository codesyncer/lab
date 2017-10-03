#!/bin/bash
echo 'Enter marks'
echo -n 'UNIX : '
read unix
echo -n 'POP  : '
read pop
echo -n 'DSA  : '
read dsa
avg=$(bc <<< "scale=2; ($unix+$pop+$dsa)/3")
if test $(bc <<< "$avg >= 70") -eq 1; then
	echo 'Distinction'
elif test $(bc <<< "$avg >= 60") -eq 1; then
	echo 'First Class'
elif test $(bc <<< "$avg >= 50") -eq 1; then
	echo 'Second Class'
elif test $(bc <<< "$avg >= 40") -eq 1; then
	echo 'Third Class'
else
	echo 'Fail'
fi