#!/usr/bin/python

from enum import Enum

class State(Enum): 
    IDLE = 1
    COUNTDOWN = 2
    ACTIVE = 3
    END = 4