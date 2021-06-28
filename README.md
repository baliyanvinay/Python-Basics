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

## Literals
- List - []
- Tuple - ()
- Dicts - {}
- Sets - {}

<b>Insight:</b> Dictionaries and Sets are actually related and are implemented very similarly. Both sets and dictionaries are hashed maps. Dictionaries are key-value pairs but sets are keys(as value) only.

## Callables in Python 
Anything that can be called using ().
-  User Defined functions
-  Generators
-  Classes
-  Instance Methods
-  Class Instances
-  Built-in Functions (len(), open())
-  Build-in Methods (my_list.append())
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
