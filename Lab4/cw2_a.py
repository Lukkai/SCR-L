#!/usr/bin/python3

import time
import signal
import sys
import os


def killProcess(signum, frame):
    print(f'Caught: {signum}. process killed')
    sys.exit()

def getSig(signum, frame):
    print("Caught:", signum)
    sys.exit()



def sigDefine():
    signal.signal(signal.SIGTERM, killProcess)
    signal.signal(signal.SIGALRM, getSig)
    signal.signal(signal.SIGUSR1, getSig)
    signal.signal(signal.SIGUSR2, getSig)


if __name__ == '__main__':
    pid=os.getpid()
    print("PID: "+ str(pid))
    
    sigDefine()
    

    i = 0

    while True:
       i = i + 1
       time.sleep(1)