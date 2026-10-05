# Operators

These are all in order of presedence (like BODMAS)

- ** Exponent --> 2 ** 3 = 8
- % Modulus/remainder --> 22 % 8 = 6
- // Integar division/floored quotient --> 22 // 8 = 2
- / Division --> 22 / 8 = 2.75
- * Multiplication
- + and - are obvious

# Data Types

## Common data types 

- Integars: -2, -1, 0, 1, 2, 3, 4, 5
- Floating-point numbers: -1.25, -1.0. --0.5, 0.0, 0.5
- Strings: 'a', 'aa', 'aaa', 'Hello!', '11 cats'

## First Functions 

print() is obvious 

input() waits for the user to type some text and then press ENTER
i.e myName = input() means the user defines the variable 'myName'

len() takes a string value that you pass, or some variable containing a string, and evaluates to the integar value of the number of characters in that string

str(), int(), float() turns one data type into another so it can be used properly in another function
i.e str(29) turns 29 into '29' so that prunt('I am ' + str(29) + ' years old.') works properly
