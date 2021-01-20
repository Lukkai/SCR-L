#!/usr/bin/python3

import time
import signal
import sys
import os


def killProcess(signum, frame):
    pass


def receiveSigUsr1(signum, frame):
    pass


def receiveSigUsr2(signum, frame):
    pass

def receiveSig(signum, frame):
    pass


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