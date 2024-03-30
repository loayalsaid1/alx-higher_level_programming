#!/usr/bin/python3
"""Find a peak of a list"""


def find_peak(l):
	"""Find the peak of a list"""
	l = l.sort()
	return l[-1]
