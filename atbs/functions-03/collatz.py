# This program is going to explore the 'Collatz Sequence'

print('Pick any number you would like to start the Collatz Sequence!')

def collatz(number):

	while number != 1:

		if number % 2 == 0:
			number = number // 2

		else:
			number = 3 * number + 1

		print(number)

while True:
	try:
		number = int(input())
		break
	except ValueError:
		print('You must enter a whole number!')

collatz(number)
