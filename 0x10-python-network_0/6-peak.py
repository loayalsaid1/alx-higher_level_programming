#!/usr/bin/python3
"""Find a peak of a list"""


def find_peak(l):
	"""Find the peak of a list"""
	if not l:
		return None
	found = False
	length = len(l)
	if length == 1:
		return l[0]
	elif length == 2:
		return max(l)
	else:
		for idx in range(1, length-1):
			if l[idx-1] <= l[idx] >= l[idx+1]:
				found = True
				break
		if found:
			return l[idx]
		else:
			if l[0] > l[1]:
				return l[0]
		
