"""
1. (8p.) Napisz program, który:
#wykona mapowanie obszaru pamięci do pliku na dysku (funkcja mmap), w taki sposób, aby zapisy do pamięci były widoczne w pliku,
#będzie wykonywał w pętli nieskończonej następujące operacje na plikach tekstowych:
   -odpyta użytkownika o nazwę pliku,
   -obliczy długość pliku i zmieni odpowiednio wielkość obszaru pamięci wspólnej i zmapowanego pliku (funkcje stat, mmap, ftruncate),
   -wczyta podany plik do zmapowanego obszaru pamięci.
"""


import mmap
import os

while True:
    
    filename = input("Nazwa pliku: ")
    with open(filename, "r+b") as f:
        # memory-map the file, size 0 means whole file
        memorysnap = mmap.mmap(f.fileno(), 0)
        # read content via standard file methods
        print(memorysnap.read())  # prints out file content
        
        test = input("test: ")
        memorysnap.seek(0)
        print(memorysnap.read())  
        # close the map
        memorysnap.close()