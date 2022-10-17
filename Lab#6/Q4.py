#!/usr/bin/python3

try:
	a, b = input('input two number: ').split()
	c = int(a)/int(b)
	print(c)

except ZeroDivisionError:
	print('division by zero')
