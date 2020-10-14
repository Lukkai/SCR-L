#!/bin/bash
#przykladowy skrypt wykonujcy porownanie dwoch wartosci i zwracajacy prawde/falsz

a=10
b=20

if [ $a==$b ]
then
    echo "a is equal to b"
else
    echo "a is not equal to b"
fi