# Functions 

## Defining Statements with Parameters

When you define a function, say 'deff hello(name)', you're creating your own argument inside the hello function.

In Python, there is a value called NOne, which represent the absence of a value, and is the only value of the NoneType data type.
It must be typed with a capital N.

Summary of the scope section: Variables in a local scope and variables in the global scope are NOT the same.

## Exception Handling 

If you want a program to carry on running, even with an error so it doesn't just crash, you can use 'try' and 'except' statements:

'''python
def spam(divideBy)
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		print('Error: INvalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
'''

## Summary

- Functions can be thought of as black boxes in your code

- Variables that existin their own local scope cannot affect global scope variables

- They have inputs in the forms of parameters, and give some chosen output

- 'try' and 'except' statements allow code to still run when an error is detected, making your programs more resilient to common error cases.
