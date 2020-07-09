#!/usr/local/bin/python

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

print("Hello World!")

print('fib 0 ' + str(fib(0)))
print('fib 1 ' + str(fib(1)))
print('fib 2 ' + str(fib(2)))
print('fib 3 ' + str(fib(3)))

print('fib 5 ' + str(fib(5)))
print('fib 10 ' + str(fib(10)))
print('fib 30 ' + str(fib(30)))