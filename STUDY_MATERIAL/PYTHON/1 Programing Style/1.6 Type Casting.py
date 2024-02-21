'''
int(x, base=10): 
Converts x to an integer. The optional base parameter specifies the base of the number if x is a string. If base is not specified, x must be a string that represents an integer in base 10.
'''
x = "10"
integer_value = int(x)  # Converts string "10" to integer 10
print(integer_value)  # Output: 10


'''
float(x): 
Converts x to a floating-point number.
'''
x = "3.14"
float_value = float(x)  # Converts string "3.14" to float 3.14
print(float_value)  # Output: 3.14


'''
str(x): 
Converts x to a string.
'''
x = 123
string_value = str(x)  # Converts integer 123 to string "123"
print(string_value)  # Output: "123"


'''
bool(x): 
Converts x to a boolean value. Returns False if x is False, 0, None, or an empty sequence or dictionary; otherwise, returns True.
'''
x = 0
bool_value = bool(x)  # Converts integer 0 to boolean False
print(bool_value)  # Output: False


'''
list(x): 
Converts x to a list. x can be any iterable like a string, tuple, set, etc.
'''
x = "hello"
list_value = list(x)  # Converts string "hello" to list ['h', 'e', 'l', 'l', 'o']
print(list_value)  # Output: ['h', 'e', 'l', 'l', 'o']


'''
tuple(x): 
Converts x to a tuple. x can be any iterable like a string, list, set, etc.
'''
x = [1, 2, 3]
tuple_value = tuple(x)  # Converts list [1, 2, 3] to tuple (1, 2, 3)
print(tuple_value)  # Output: (1, 2, 3)


'''
set(x): 
Converts x to a set. x can be any iterable like a string, list, tuple, etc.
'''
x = [1, 2, 3]
set_value = set(x)  # Converts list [1, 2, 3] to set {1, 2, 3}
print(set_value)  # Output: {1, 2, 3}


'''
dict(x): 
Converts x to a dictionary. x can be an iterable containing key-value pairs, or a sequence of key-value pairs.
'''
x = [(1, 'one'), (2, 'two')]
dict_value = dict(x)  # Converts list of tuples to dictionary {1: 'one', 2: 'two'}
print(dict_value)  # Output: {1: 'one', 2: 'two'}


'''
complex(real, imag=0): 
Creates a complex number with the value real + imag * 1j.
'''
real = 1
imag = 2
complex_value = complex(real, imag)  # Creates complex number (1+2j)
print(complex_value)  # Output: (1+2j)