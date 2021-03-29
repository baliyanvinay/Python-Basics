# Python Basics
Python is named after the BBC show “Monty Python’s Flying Circus” and has nothing to do with reptiles.

## Python Data Types
- Numbers
- Strings
- Lists
- Sets
- <b>Tuple: </b>Immutable, indexing/slicing supported, addition-update not supported. Use case?
- Dictionary

## Python Conditionals
Like other programming langauges control flow statements are similar in Python as well.

# If Else Elif

# Exception Handling
Errors detected during execution are called Exceptions. 
### try
- If an exception occurs during execution of the try clause, the rest of the clause is skipped
- Try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed.

### except
- An except clause may name multiple exceptions as a parenthesized tuple

## else
- Else clause is executed when there are no exceptions raised by try block. 
- Useful in avoid catching accidental exceptions raised in try block. The part that should not throw an error.

## finally
- Clause runs whether or not the try statement produces an exception.

## User defined errors
- Define a class inherited from Exception class.

# Collections module
## NamedTuple
Tuple does not support item assignment means they are immutable object, with namedtuple functions such as 'replace' function, item assignment is possible

## DefaultDict
- defaultdict is the subclass of built in dict class. It overrides one method and adds one writable instance variable.
- Dictionary throws a KeyError if you try to get an item with a key that is not currently in the dictionary. 
- defualtdict never raises a KeyError. It provides a default value for the key that does not exists.
- The remaining functionality is the same as dictionary
 


### Sources: 
https://docs.python.org/ <br>
https://www.tutorialspoint.com/python_data_structure/
