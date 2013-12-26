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


################## CHECK IF NUMBER IS EVEN OR ODD ###################
def checkIfEvenOrOdd(number):
    if number%2==0:
        return "even"
    else:
        return "odd"

def mergeRingsToReel(offset, positions, ring1, ring2):
	reel = []
	
	for position in positions:
		if checkIfEvenOrOdd(position+offset) == "even":
			reel.append(ring2[position])
			
		else:
			reel.append(ring1[position])
	return reel


def addReels(numbers, reelA, reelB):
	sum = []
	
	for number in numbers:
		sum.append(reelA[number] + reelB[number])
	
	return sum
	
	

def rotateRing(times, ring):
	ring2 = ring[:]
	
	# rotate clockwise
	for number in range(0,times):
		# Don't operate on ring directly, it will actually rotate the input ring which we want to leave immutable!
		ring2.insert(0, ring2.pop())
	
	return ring2


# There are 5 rings
# All rotations are clockwise, and ordering of ring values is also clockwise

ring0a = [0, 16, 8, 4, 15, 7, 10, 1, 10, 4, 5, 3, 15, 16, 4, 7]
ring0b = [13, 11, 13, 10, 18, 10, 10, 10, 10, 15, 7, 19, 18, 2, 9, 27]

ring1a = [6, 0, 10, 0, 8, 0, 10, 0, 9, 0, 8, 0, 8, 0, 9, 0]


ring1b = [5, 1, 24, 8, 10, 20, 7, 20, 12, 1, 10, 12, 22, 0, 5, 8]

ring2a = [0, 0, 11, 0, 8, 0, 8, 0, 8, 0, 10, 0, 11, 0, 10, 0]

ring2b = [20, 8, 19, 10, 15, 20, 12, 20, 13, 13, 0, 22, 19, 10, 0, 5]

ring3a = [3, 0, 8, 0, 10, 0, 14, 0, 11, 0, 8, 0, 12, 0, 11, 0]

ring3b = [10, 17, 10, 5, 6, 18, 8, 17, 4, 20, 4, 14, 4, 5, 1, 14]

ring4a = [19, 0, 8, 0, 17, 0, 6, 0, 6, 0, 8, 0, 8, 0, 16, 0]






positions = range(0,16)
positions2 = range(0,16)
positions3 = range(0,16)
positions4 = range(0,16)
positions5 = range(0,16)

counter = 0


for ring1position in positions:

	register0 = ring0a
	register1 = rotateRing(ring1position, ring1a)
	
	# print "ROTATE RING1 " + str(ring1position) + " times"
	# print "register1: " + str(register1)
	
	if checkIfEvenOrOdd(ring1position) == "even":
		offset = 0
	else:
		offset = 1
	
	reel1 = mergeRingsToReel(offset, positions, ring0b, register1)
	
	# print "reel1: " + str(reel1)
	
	sum1 = addReels(positions, register0, reel1)
	
	# print "SUM1 IS: " + str(sum1)
	# # print ""
	
	for ring2position in positions:
		register2 = rotateRing(ring2position, ring2a)
		
		# print "ROTATE RING2 " + str(ring2position) + " times"
		# print "register2: " + str(register2)
		# print "ring1b: " + str(ring1b)
		
		if checkIfEvenOrOdd(ring2position) == "even":
			# # print "EVEN"
			offset = 0
		else:
			# # print "ODD"
			offset = 1

		reel2 = mergeRingsToReel(offset, positions2, rotateRing(ring1position, ring1b), register2)

		# print "reel2: " + str(reel2)
		
		sum2 = addReels(positions2, sum1, reel2)
		
		# print "SUM2 IS: " + str(sum2)
		# # print ""
		
		for ring3position in positions:
			register3 = rotateRing(ring3position, ring3a)

			if checkIfEvenOrOdd(ring3position) == "even":
				# # print "EVEN"
				offset = 0
			else:
				# # print "ODD"
				offset = 1

			reel3 = mergeRingsToReel(offset, positions3, rotateRing(ring2position, ring2b), register3)

			# print "reel3: " + str(reel3)

			sum3 = addReels(positions3, sum2, reel3)

			# print "SUM3 IS: " + str(sum3)
			# print ""

			for ring4position in positions:
				register4 = rotateRing(ring4position, ring4a)

				if checkIfEvenOrOdd(ring4position) == "even":
					# # print "EVEN"
					offset = 0
				else:
					# # print "ODD"
					offset = 1

				reel4 = mergeRingsToReel(offset, positions4, rotateRing(ring3position, ring3b), register4)

				# print "reel3: " + str(reel3)

				sum4 = addReels(positions4, sum3, reel4)
				counter += 1

				if sum4 == [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]:
				# if sum4[0] == 50 and sum4[1] == 50 and sum4[2] == 50:
					print "ring1Position: " + str(ring1position)
					print "ring2Position: " + str(ring2position)
					print "ring3Position: " + str(ring3position)
					print "ring4Position: " + str(ring4position)
					print "reel1: " + str(reel1)
					print "SUM1 IS: " + str(sum1)
					print "reel2: " + str(reel2)
					print "SUM2 IS: " + str(sum2)
					print "reel3: " + str(reel3)
					print "SUM3 IS: " + str(sum3)
					print "reel4: " + str(reel4)
					print "SOLUTION FOUND IS: " + str(sum4)
					# print ""
			


print ""
print "OUT OF " + str(counter) + " COMBINATIONS TESTED"



# rings = [ring0a, ring0b, ring1a]
# 
# 
# 
# 
# # for ring in rings:
# 	# print ring
# 	
# 
# 
# # print positions
# 
# reel0 = ring0a
# 
# 
# 
# # we are now going to do a mapping
# # ring0a:	 0, 	16,	...,	7
# # ring0b:	13, 	11,	...,	27
# # ring1a:	 6, 	0,	...,	0
# 
# # we need to condense ring0b and ring1a into one array called reel1
# 
# reel1 = mergeRingsToReel(0, positions, ring0b, ring1a)
# 
# # print reel1
# 
# sum1 = addReels(positions, reel0, reel1)
# 
# # print sum1
# 
# 
# # rotate function
# 
# # print ring1a
# # ringRotated = rotateRing(0, ring1a)
# # print ringRotated
# # print ""
# # print ring1a
# # ringRotated = rotateRing(1, ring1a)
# # print ringRotated
# # print ""
# # print ring1a
# # ringRotated = rotateRing(2, ring1a)
# # print ringRotated
# # print ""
# # print ring1a
# # ringRotated = rotateRing(3, ring1a)
# # print ringRotated
# # print ""
# # print ring1a
# # ringRotated = rotateRing(4, ring1a)
# # print ringRotated
# 
# # print ringRotated
# 



# reels = range(0,1)
# print reels
# 
# for position in positions:
# 	# print ring0a[position]
# 
# 
# 	# reel 1 is a combination of ring0b and ring1a
# 	# position of reel 1 is chosen from EITHER ring 0b or ring1a at each wedge slot
# 	
# 	for reel in reels:
# 		# show possibilities of values at wedge 0 slot 1
# 		if checkIfEvenOrOdd(position) == "even":
# 			print ring1a[position]
# 		else:
# 			print ring0b[position-1]
# 		
# 



























