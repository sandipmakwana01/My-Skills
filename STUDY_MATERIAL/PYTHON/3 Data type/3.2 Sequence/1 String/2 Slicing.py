'''string[start:end:step]'''

my_string = "Hello, World!"

# Extracting characters from index 0 to index 4 (exclusive)
substring1 = my_string[0:5]
print(substring1)  # Output: Hello

# Extracting characters from index 7 to the end of the string
substring2 = my_string[7:]
print(substring2)  # Output: World!

# Extracting characters from the beginning to index 5 (exclusive)
substring3 = my_string[:5]
print(substring3)  # Output: Hello

# Extracting every second character
substring4 = my_string[::2]
print(substring4)  # Output: Hlo ol!

# Reversing the string
substring5 = my_string[::-1]
print(substring5)  # Output: !dlroW ,olleH

print(my_string[::-1])
print(my_string[-1:-13:])
