# Lists and Tuples

## The List Data Type

Definition: A *list* is a value that contains multiple values in an ordered sequence.

It begins and ends with a closing square bracket, [].

Values inside the list are called *items*, which must be seperated with commas. 

```python3
spam = ['cat', 'dog', 'bird']
spam[0]    # Returns cat
spam[1]    # Returns dog
```
Notice how in the code above, the first item has an index of 0.

Lists can contain other lists, indented with more square brackets.

You can also have negative indexes:

```python3
spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1]	# Returns elephant
spam [-3]	# Returns bat
print('The ' spam[-1] + ' is afraid of the ' + spam[-3] + '.')
```

## Getting a sublist with Slices

A slice can get several values from a list, in the form of a new list.

'spam[2]' is a list with an index, 'spam[1:4]' is a list with a slice. This will print a list from the element with index 1 to the 4th element (not index 4!)

You can get a list's length with 'len()'.

You can also swap values in a list with indexes: i.e specify 'spam[1] = spam[2]' then print spam to see the change. 

You can remove a value from lists with 'del()'

## Working with Lists
