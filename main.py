#!/usr/bin/env python

import signal,sys

ctrlC = 0

def catch_ctrl_C(sig,frame):
    global ctrlC
    if ctrlC < 5:
        print("Not gonna quit !!")
    else:
        exit()
    ctrlC += 1

signal.signal(signal.SIGINT, catch_ctrl_C)

while True:
        pass
