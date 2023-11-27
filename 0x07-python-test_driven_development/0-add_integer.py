#!/usr/bin/python3
"""
	add integer module
"""

def add_integer(a, b=98):
	"""
	add_integer: make integer addition
	Only accept integers and if got floats, convert them
	b is defaulted to 98
	reutrn integer int(a) * int(b)
	"""
	if type(a) not in {int, float}:
		raise TypeError("a must be an integer")
	if type(b) not in {int, float}:
		raise TypeError("b must be an integer")

	return int(a) + int(b)
