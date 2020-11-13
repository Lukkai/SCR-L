#!/bin/python3

import time
import signal
import sys
import os

def receiveSigUsr1(sigNum, frame):
    print(f'Catched: {sigNum}. terminating the process')
    sys.exit()

def receiveSigUsr2(sigNum, frame):
    print(f'Catched: {sigNum}. terminating the process')
    sys.exit()

def terminateProcess(sigNum, frame):
    print(f'Catched: {sigNum}, terminating the process')
    sys.exit()

def receiveSig(sigNum, frame):
    print("Catched:", sigNum)
    sys.exit()



if __name__ == '__main__':
    print("PID: "+ str(os.getpid()))
    signal.signal(signal.SIGALRM, receiveSig)
    signal.signal(signal.SIGTERM, terminateProcess)
    signal.signal(signal.SIGUSR1, receiveSigUsr1)
    signal.signal(signal.SIGUSR2, receiveSigUsr2)

    i = 0

    while True:
        i = i + 1
        time.sleep(1)