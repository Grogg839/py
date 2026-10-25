def spam(divideBy):
	return 42 / divideBy

try:
	print(spam(2))
	print(spam(12))
	print(spam(0))
	print(spam(1))
except ZeroDivisionError:
	print('Error: Invalid argument.')

# This will go through the prints, and instead of crashing at spam(0), it prints the error msg.
