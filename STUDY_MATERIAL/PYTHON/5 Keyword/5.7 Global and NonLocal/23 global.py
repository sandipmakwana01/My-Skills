'''
global, nonlocal: These are used to declare global and nonlocal variables inside functions respectively.
'''

x = 10

def func():
    global x
    x += 5
    print(x)

func()
