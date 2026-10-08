# Lists and Tuples

## The List Data Type

Definition: A *list* is a value that contains multiple values in an ordered sequence.

It begins and ends with a closing square bracket, [].

Values inside the list are called *items*, which must be seperated with commas. 

If you had some list 'spam = ['cat', 'dog']', the Python code spam[0] would evaluate to cat, and spam[1] to dog. The integars 0 and 1 here are the lists *index*.

Lists can also contain other lists, indented with more square brackets.

You can also have negative indexes:

'''python
spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1]	# Returns elephant
spam [-3]	# Returns bat
'The ' spam[-1] + ' is afraid of the ' + spam[-3] + '.'
'''

## Getting a sublist with Slices

A slice can get several values from a list, in the form of a new list.

'spam[2]' is a list with an index, 'spam[1:4]' is a list with a slice. This will print a list from element with index 1 to the 4th element (not index 4!)

You can get a list's length with 'len()'.

You can also swap values in a list with indexes: i.e specify 'spam[1] = spam[2]' then print spam to see the change. 

You can remove a value from lists with 'del()'

## Working with Lists
