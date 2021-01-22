# Python Data Types-Each data type is a Python Class as Python is an OOP language
# The basics are int, float, complex numbers, strings

# Lists
a_list = []
a_list = list()  # if no agruement is given, the constructor creates an empty list
a_list = list((1, 2, 3))  # Does accepts only one arguement
# OPERATIONS/LIST METHODS
a_list.append(12)
a_list.count(2)  # occurence of a element
a_list.index(12, 2)  # returns index

# Dictionary
a_dict = {}
a_dict = dict()
a_dict = dict(name='bob', age=22)
# OPERATIONS/DICT METHODS
a_dict.items()
a_dict.get('name')
a_dict.popitem()  # removes/returns last key-value pair
a_dict.update(work_exp=5)  # adds new key-value pair

# Sets
a_set = {}
a_set = set()
a_set = set(['Mon', 'Tues', 'Wed'])
# OPERATIONS/SET METHODS
a_set.add('Fri')
a_set.discard('Mon')
a_set | {'Sat', 'Sun'}  # Union of two sets
a_set & {'Fri'}  # Intersection

# Tuple
a_tuple = ()
a_tuple = tuple()
a_tuple = tuple([1, 2, 3, ])
# OPERATIONS/TUPLE METHODS
a_tuple.index(1)  # Not much operations are supported by tuple
