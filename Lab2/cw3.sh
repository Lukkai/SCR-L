#!/bin/bash

#3) (3p.) Ćwiczenia z programem find: napisz skrypt znajdujący programem find wszystkie pliki o zadanym
#   rozszerzeniu lub masce, które były modyfikowane w ciągu ostatnich N dni i tworzący z nich archiwum tar 
#   o zadanej nazwie. Mamy tu trzy parametry: maskę nazwy pliku, liczbę N i nazwę archiwum.
#   Parametry są zadawane przez argumenty, to znaczy skrypt zawsze będzie wywołany z trzema parametrami. 

echo -n > "$3"
for found_file in $(find . -name "&*$1" -print); 
do  #gets the number of days since files last modification
    mod=$(date -r $found_file +%s)
    now=$(date +%s)
    days=$(expr \( $now - $mod \) / 86400)
    #checks if file modification date is in range
    [ "$days" -le "$2" ] && echo "$found_file" >> "$3"
done

# -le = is less than or equal to
# \( or \) is a bash syntax that allows us to use signs