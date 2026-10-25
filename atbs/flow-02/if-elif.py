print('Hello, what is your name?')
name = input()
print('Hello ' + name + ', how old are you?')
age = int(input())

if name == 'grogg':
    print('Hi, grogg.')
elif age <= 20:
    print('You are not grogg, kiddo!')
elif age >= 1000:
    print('Unlike you, grogg is not an undead, immortal vampire!')
elif age >= 100:
    print('You are not grogg, gramps!')
