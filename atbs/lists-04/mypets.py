# This program will ask for a pet name and then check if it's in a list of known pets or not

mypets = ['Fly', 'Jazz', 'Diesel', 'Rupert', 'Monty']
print('Enter a pet name:')
name = input()
if name not in mypets:
	print('I do not have a pet named ' + name)
else:
	print(name + ' is my pet.')
