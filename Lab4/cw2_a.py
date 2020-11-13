#!/bin/python3

import time
import signal
import sys
import os

def getSigUsr1(sigNum, frame):
    print(f'Catched: {sigNum}. terminating the process')
    sys.exit()

def getSigUsr2(sigNum, frame):
    print(f'Catched: {sigNum}. terminating the process')
    sys.exit()

def killProcess(sigNum, frame):
    print(f'Catched: {sigNum}, terminating the process')
    sys.exit()

def getSig(sigNum, frame):
    print("Catched:", sigNum)
    sys.exit()



if __name__ == '__main__':
    print("PID: "+ str(os.getpid()))
    signal.signal(signal.SIGALRM, getSig)
    signal.signal(signal.SIGTERM, killProcess)
    signal.signal(signal.SIGUSR1, getSigUsr1)
    signal.signal(signal.SIGUSR2, getSigUsr2)

    i = 0

    while True:
        i = i + 1
        time.sleep(1)