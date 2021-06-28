# Python Data Types
Python Data types are categorized into -
1. Numbers
a. Integrals - Integers, Booleans
b. Non-Integrals - Floats, Complex, Decimals, Fractions
2. Collections
a. Sequences - Mutuable - Lists | Immutable - Tuples, Strings
b. Sets - Mutuable - Sets | Immutable - Frozen Sets
c. Mappings - Dictionaries 

<b>Insight:</b> Dictionaries and Sets are actually related and are implemented very similarly. Both sets and dictionaries are hashed maps. Dictionaries are key-value pairs but sets are keys(as value) only.


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