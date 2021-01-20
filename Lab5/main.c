/* 1. (8p.) Napisz program, który:
* utworzy potok (funkcją pipe), uruchomi podproces, z którym proces nadrzędny będzie komunikował się przez ten potok (funkcja fork),
* proces nadrzędny otworzy plik tekstowy podany w argumencie wywołania programu, a następnie wyśle procesowi 
* potomnemu zawartość tego pliku przez potok, proces potomny odczyta dane z potoku, 
* a następnie wyświetli je na standardowym wyjściu dodając znak '#' na początku 
* i końcu każdej odebranej paczki danych. Wielkość paczek jest dowolna.
*/

#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define MAX_BUFFFER 64

int main(int argc, char *argv[])
{

}