'''list[start:end:step]'''

my_string = [1,2,3,4,5,[6,7,8],9,10]

# Extracting characters from index 0 to index 4 (exclusive)
substring1 = my_string[0:5]
print(substring1)

# Extracting characters from index 7 to the end of the string
substring2 = my_string[5:]
print(substring2)  

# Extracting characters from the beginning to index 5 (exclusive)
substring3 = my_string[:5]
print(substring3) 

# Extracting every second character
substring4 = my_string[::2]
print(substring4) 

# Reversing the string
# print(my_string[::-1])
print(my_string[-1::-1])
