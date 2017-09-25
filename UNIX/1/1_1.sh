#!/bin/bash
if test $# -lt 3 
then
	echo "Format P(Rs) Rate Time in years"
	exit
fi
echo "SI : Rs" $(bc <<< "scale=2; $1 * $2 * $3 / 100" )
