#!/usr/bin/python3
if __name__== "__main__":
	"""prints the number of a list of arguments."""
	import os

	count = len(sys.argv0 - 1
	if count == 0:
		print("0 arguments.")
	elif count == 1:
		print("1 argument:")
	else:
		print("{} arguments:".format(count))
	for i in range(count):
		print("{}: {}".format(i + 1, sys.argv[i + 1]))
