#!/usr/bin/python

import sys

def fib(n):
	if n == 0:
		return []
	elif n == 1:
		return [1]
	elif n == 2:
		return [1,1]
	else:
		fibs = [1,1]
		for x in range(2, n):
			fibs.append(fibs[len(fibs)-1] + fibs[len(fibs)-2])
		return fibs

def fib2(n, fibs):
	if n < 3:
		return fibs
	else:
		fibs.append(fibs[len(fibs)-1] + fibs[len(fibs)-2])
		return fib2(n-1, fibs)

if len(sys.argv) < 2:
	print("Usage: ./fib.py 5 output: [1, 1, 2, 3, 5]")
else:
	print(str(fib(int(sys.argv[1]))))
