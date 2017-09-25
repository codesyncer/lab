	#!/bin/bash
if test $# -lt 2
then
    echo "Enter dimensions in cm"
    exit
fi
echo "Area in cmsq :" $(bc<<<"$1 * $2")