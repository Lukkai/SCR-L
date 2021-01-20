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

#define BUFFER_SIZE 32

int main(int argc, char *argv[])
{
    int pid;
    int file_descriptor[2];
    pipe(file_descriptor);

    if (pid==fork())
    {
        char buf[BUFFER_SIZE];
        while (read(file_descriptor[0], buf, BUFFER_SIZE))
        {
            if(buf[BUFFER_SIZE -1] == 0)
                break;
            buf[BUFFER_SIZE - 1] = '\0';
            printf("#%s#\n", buf);
        }
    }
    else
    {
        FILE *f = fopen(argv[1], "r");
        char buf[BUFFER_SIZE];

        while (fgets(buf, BUFFER_SIZE - 1, f))
        {
            buf[BUFFER_SIZE - 1] = 1;
            write(file_descriptor[1], buf, BUFFER_SIZE);
        }

        buf[BUFFER_SIZE - 1] = 0;
        write(file_descriptor[1], buf, BUFFER_SIZE);

        fclose(f);
    }

}