#!/bin/bash
if test $# -lt 1
then
	echo "Enter basic pay"
	exit
fi
echo "Salary : Rs" $(bc<<<"scale=2; 2.04 * $1") 