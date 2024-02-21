'''
try, except, finally, raise: These are used for exception handling.
'''
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")

raise ValueError("This is a custom error")
