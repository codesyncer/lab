#!/bin/bash
if test $# -lt 1
then
    echo "More args"
    exit
fi
echo "Sum =" $((($1*($1+1)/2)))