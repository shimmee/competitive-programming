#!/bin/sh

#  mkdir_atcoder.sh
#  
#
#  Created by Keita Shimmei on 10/28/20.
#  

# $1=cource name(lower case)
# $2=number

make_files(){
    dir=`echo $1 | tr '[a-z]' '[A-Z]'`
    display_num=`printf %03d $2`
    if [ ! -e $dir ]; then mkdir $dir ; fi
    cd $dir
    if [ ! -e $1$display_num ];then
        mkdir $1$display_num
        cd $1$display_num
        touch input.txt
        if [[ $1 = "abc"  ]] ; then
            L=(A B C D E)
        elif [[ $1 = "agc" ]]; then
            L=(A B C D E F)
        elif [[ $1 = "arc" ]]; then
            if [[ "$2" -gt 57 ]]; then
                L=(A B C D)
            else
                L=(A B C D)
            fi
        fi
        for var in ${L[@]}
        do
            touch "$1$display_num$var.py"
        done
    fi
}
make_files $1 $2
