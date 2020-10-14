#!/bin/bash

# 4) (5p.) Zmodyfikuj skrypt napisany w poprzednim punkcie tak, aby miał rozbudowany i wygodny
# interfejs użytkownika. Po pierwsze, pozycyjne parametry wywołania zamień na opcjonalne z jednoliterowymi
# słowami kluczowymi (poprzedzonymi znakiem minus), według wzoru:

# find_and_tar.sh -n 5 -m '*.c' -a progarch.tar

#Każdy z parametrów -n, -m, i -a może wystąpić lub nie, i mogą one być zadane w dowolnej kolejności
# (ale w parach ze słowem kluczowym). Jest to ogólnie przyjęta konwencja pisania skryptów
# i programów w systemie Unix.

#Następnie dodaj mechanizm pobierania wartości parametru w przypadku, gdyby nie wystąpił
# jako argument wywołania. Jeśli dany parametr nie wystąpił, a istnieje zmienna środowiskowa 
# zadająca wartość danego parametru (wymyśl dobre nazwy dla tych zmiennych), to będzie użyta wartość
# tej zmiennej. Jeśli nie ma ani argumentu wywołania ani zmiennej środowiskowej, to skrypt powinien
# zapytać się użytkownika o wartość danego parametru, i wykorzystać tę wartość. Do zadania pytania 
# użytkownikowi wykorzystaj polecenie echo, a do odczytania odpowiedzi użytkownika polecenia read
# lub programu line.

#Wskazówka: można usprawnić czytanie i analizę (parsing) wektora argumentów z parametrami opcjonalnymi za pomocą programu getopt. Jego użycie jest proste, a daje przenośność i odporność na błędy. Dobry jest przykład w dokumentacji man getopt (na niektórych wersjach Linuksa man nie ma tego przykładu, patrz man getopt na systemie Solaris). 