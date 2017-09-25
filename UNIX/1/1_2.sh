#!/bin/bash
if test $# -lt 1
then
	echo "Enter radius in cm"
	exit
fi
echo "Area in cmsq :" $(bc<<<"3.14159 * $1 * $1") 