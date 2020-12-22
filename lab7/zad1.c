#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#define NUM_THREADS	10

void *PrintHello(void *threadid)
{
   long tid;
   tid = (long)threadid;
   printf("Hello World! It's me, thread #%ld!\n", tid);
   pthread_exit(NULL);
}

int main(int argc, char *argv[])
{
   pthread_t threads[NUM_THREADS];
   int rescode;
   long t;
   for(t=0;t<NUM_THREADS;t++){
     rescode = pthread_create(&threads[t], NULL, PrintHello, (void *)t);
     }

   pthread_exit(NULL);
}
