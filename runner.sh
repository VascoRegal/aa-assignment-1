#!/bin/bash

#
# Auxiliary tool to conduct experiments
#


min_V=5
N=10
edges=50
file=""
greedy='false'

while getopts v:n:e:f:g: flag
do
    case "${flag}" in 
        v) min_V=${OPTARG};;
        n) N=${OPTARG};;
        e) edges=${OPTARG};;
        f) file=${OPTARG};;
        g) greedy='true';;
    esac
done

i=0

while [ $i -le $N ]
do
    command="python3 main.py $(($min_V+$i)) $edges "
    if [ "$file" != "" ]
    then
        command="$command -e $file "
    fi

    if [[ "$greedy" == 'true' ]]
    then
        command="$command -g"
    fi

    eval $command 
    i=$((i+1))
done
