#! /usr/bin/bash
# set up the structure of the directory



for dir in `cat folder-structure.txt`;
do
    if [ ! -d $dir ]; then
        mkdir $dir
    fi
done
