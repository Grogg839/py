# Boolean Values

While integar, floating-point and string data types have an unlimited number of possible values, the Boolean data type has only two values: True and False.

# Comparison Operators 

- == equal to
- != not equal to
- < less than
- < more than
- <= less than or equal to
- >= greater than or equal to

You should be aware that the = operator (assignment) puts the value on the right into the variable on the left.
The == operator (equal to) asks whether two values are the same as each other.

# Boolean Operators

There are 3 Boolean operators (and, or & not) are used to compare Boolean values. They evaluate to a Boolean value, same as comparison operators do. 

True and True --> True 
True and False --> False 
False and True --> False 
False and False --> False 

True or True --> True 
True or False --> False 
False or True --> True 
False or False --> False 

not True --> False 
not False --> True

You should be aware you can mix boolean and comparison operators: (4 < 5) and (5<6) would evaluat e to True.

# Elements of Flow Control

Flow control statements often start with a 'condition', and all are followed by a block of code called the 'clause'

if statement clauses will execute if the statemen'ts condition is True. The cluase is skipped if the condition is false.

'''python
if name == 'Alice':
    print('Hi, Alice.')
'''

The if statement can also be followed by an else statement. The else clause is executed only when the if statement's condition is False.

The elif statement that always follows another if or elif statement is a way of checking one of many possible clauses to execute. 
It provides another condition that is checked only if any of the previous conditions were False.

'''python
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
'''

# While loops

Blocks of code can execute over and over again with a 'while' statement.

You can stop a while loop early by using the 'break', which is added by just the workd break and that's it.

The 'continue' statement can be used similarly to the break, however when the program reaches a continue statement, it jumps back to the start of the loop and re-evaluates the loop's condition.

# Importing Modules

You should already know most things about importing modules, but you can cause a program to end early with sys.exit()
