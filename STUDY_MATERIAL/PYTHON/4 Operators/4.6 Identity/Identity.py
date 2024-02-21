'''
Identity Operators:
    (is, is not) are used to compare the memory locations of two objects. 
    is - Returns True if both variables are the same object 
    is not - Returns True if both variables are not the same object

'''

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)     # Output: True
print(x is y)     # Output: False
print(x is not y) # Output: True
