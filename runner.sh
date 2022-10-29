#!/bin/bash

#
# Auxiliary tool to conduct experiments
#


min_V=5
N=10
edges=50
file=""

while getopts v:n:e:f: flag
do
    case "${flag}" in 
        v) min_V=${OPTARG};;
        n) N=${OPTARG};;
        e) edges=${OPTARG};;
        f) file=${OPTARG}
    esac
done

i=0

while [ $i -le $N ]
do
    if [ "$file" = "" ]
    then
        python3 main.py $(($min_V+$i)) $edges
    else
        python3 main.py $(($min_V+$i)) $edges -e $file
    fi
    i=$((i+1))
done
