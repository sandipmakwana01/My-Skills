# USING RANGE FUNCTION
my_string = "Hello, World!"

# for a in range(len(my_string)):
#     print(my_string[a])

# for a in range(len(my_string)-1,-1,-1):
#     print(my_string[a])

# WITHOOUT USING RANGE FUNCTIN
# my_string2 = "Hellow, World!"

# for b in my_string2:
#     print(b)

# a = my_string2[-1::-1]
# for b in a:
#     print(b)



# a = 0
# while a <len(my_string):
#     print(my_string[a])
#     a+=1
a = -1
while a >= -len(my_string):
    print(my_string[a])
    a-=1