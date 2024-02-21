'''
del, with: These are used for deleting objects and resource management using context managers respectively.
'''
x = 1
del x

with open("file.txt", "r") as file:
    data = file.read()
