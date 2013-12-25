#!/usr/bin/env python
# encoding: utf-8
"""
safecracker.py

Jordan and Rich


"""

##### NEED TO FIX DIVISION OPERATOR!!!!!
from __future__ import division
#http://docs.python.org/release/2.2.3/whatsnew/node7.html
#The most controversial change in Python 2.2 heralds the start of an effort to fix an old design flaw that's been in Python from the beginning. Currently Python's division operator, /, behaves like C's division operator when presented with two integer arguments: it returns an integer result that's truncated down when there would be a fractional part. For example, 3/2 is 1, not 1.5, and (-1)/2 is -1, not -0.5. This means that the results of divison can vary unexpectedly depending on the type of the two operands and because Python is dynamically typed, it can be difficult to determine the possible types of the operands.



import os
# import shutil
import time
from time import gmtime, strftime
import re
import math




def done_at(file):
	print file + " done at " + strftime("%I:%M:%S %p %Z", gmtime())
	return


# FROM http://stackoverflow.com/questions/1191374/subprocess-with-timeout
import subprocess, threading



# There are 5 rings
# All rotations are clockwise, and ordering of ring values is also clockwise

ring0a = [0, 16, 8, 4, 15, 7, 10, 1, 10, 4, 5, 3, 15, 16, 4, 7]
ring0b = [13, 11, 13, 10, 18, 10, 10, 10, 10, 15, 7, 19, 18, 2, 9, 27]

ring1a = [6, 0, 9, 0, 8, 0, 8, 0, 9, 0, 10, 0, 8, 0, 10, 0]


rings = [ring0a, ring0b, ring1a]


for ring in rings:
	print ring
	































