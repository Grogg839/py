# Goal is to make a program that asks for a name and password

while True: 
    print('Who are you?')
    name = input()
    if name != 'grogg':
        continue
    print('Hello, grogg. What is the password? (It is an instrument.)')
    password = input()
    if password == 'Piano':
        break
print('Access granted')
