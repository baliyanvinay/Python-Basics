# Python Data Types
Python Data types are categorized into -
* Numbers
  * Integrals - Integers, Booleans
  * Non-Integrals - Floats, Complex, Decimals, Fractions
* Collections
  * Sequences - Mutuable - Lists | Immutable - Tuples, Strings
  *  Sets - Mutuable - Sets | Immutable - Frozen Sets 
  *  Mappings - Dictionaries 
* Singletons
  * None
  * NotImplemented

<b>Insight:</b> Dictionaries and Sets are actually related and are implemented very similarly. Both sets and dictionaries are hashed maps. Dictionaries are key-value pairs but sets are keys(as value) only. <br>
<b>Insight:</b> Unpacking also works with dictionaries and sets but because both are unsorted, the order of unpacking is random each time. 


## Callables in Python 
Anything that can be called using ().
-  User Defined functions
-  Generators
-  Classes
-  Instance Methods
-  Class Instances
-  Built-in Functions (len(), open())
-  Build-in Methods (my_list.append())

# Python Optimization: String Interning 
When string object is creted with no spaces, then any other name referring to the object will point to the same memory location.
```python
>>> text_01 = 'Hello'
>>> text_02 = 'Hello'
>>> text_01 is text_02 # returns True
```
However when strings are created with spaces, containing the same text, it will be stored in a different memory location. 
```python
>>> text_01 = 'Hello World'
>>> text_02 = 'Hello World'
>>> text_01 is text_02 # returns False
>>> text_01 == text_02 # returns True
```

<b>Insight:</b> Lists and Tuples are ordered sequences while sets are not. Because sets store the values in form of hash keys. 

# Function Parameters
- Every parameter after default parameter in a function defination must be a default parameter. Same principle goes with named argument. 

# Higher-Order Functions
- takes a function as an argument
- returns a function

# First call objects in Python
- can be passed to a function as an argument
- can be returned from a function
- can be assigned to a variable
- can be stored in a data structure(such as list, tuple, dictionaary etc)
- Types such as int, float, string, tuple, list and many more are first-class objects
- Functions(function) are also first-class objects

------------------------------------------------------------------------------------------------------------------------------------------------------
_my_var = 'private variable'. convention to indicate private variables | Objects imported this way shall not be imported into another module like.. from module import _my_var --> Fail

__my_var --> Class attributes mangle

__init__ --> Used for system defined names, that has special meaning to interpreter. 

Packages: short, all lowercase names. Preferably no underscore utilities
Modules: short, all lowercase names. Can have underscores db_utils
Classes: Camel Case convention, BankAccount
Functions, variables: lowercase, words separeted by underscores, account_id
Constants: All upercase, words separated by underscores, REP_COUNT

Loops has else statements.
Iterable is an object capable to returning values, one at a time
