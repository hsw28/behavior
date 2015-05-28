#!/usr/bin/env python
import string
from random import randint


right = 0
left = 0

inrowR = 0
inrowL = 0

barrier = 0


while right+left < 50:
    raw_input("Press Enter to continue...")
    #assigns random direction
    barrier=randint(1,2)

	#checks to make sure animal hasn't turned same direction > 3 times
    if inrowR == 3:
        barrier = 2
    if inrowL == 3:
        barrier = 1

	#returns direction
    if barrier == 1:
        right = right+1
        inrowR = inrowR+1
        inrowL = 0
        print "barrier goes on right"

    if barrier == 2:
        left = left+1
        inrowL = inrowL+1
        inrowR = 0
        print "barrier goes on left"
