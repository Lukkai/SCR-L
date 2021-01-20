#!/usr/bin/python3

import time
import signal
import sys
import os


def killProcess(signum, frame):
    i = 0
    while i<1000:
        i = i + 1
    print(f'Received: {signum}')
    return


def receiveSigUsr1(signum, frame):
    i = 0
    while i<1000:
        i = i + 1
    print(f'Received: {signum}')
    return


def receiveSigUsr2(signum, frame):
    i = 0
    while i<1000:
        i = i + 1
    print(f'Received: {signum}')
    return

def receiveSig(signum, frame):
    i = 0
    while i<1000:
        i = i + 1
    print(f'Received: {signum}')
    return


def sigDefine():
    signal.signal(signal.SIGTERM, killProcess)
    signal.signal(signal.SIGALRM, receiveSig)
    signal.signal(signal.SIGUSR1, receiveSigUsr1)
    signal.signal(signal.SIGUSR2, receiveSigUsr2)


if __name__ == '__main__':
    pid=os.getpid()
    print("PID: "+ str(pid))
    
    sigDefine()
    
    i = 0

    while True:
       i = i + 1
       time.sleep(1)