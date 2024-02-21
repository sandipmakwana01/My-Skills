'''
`dict`: Dictionary type, unordered collection of key-value pairs (e.g., {'name': 'John', 'age': 30}).
'''
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

print(person)

print(person['age'])

for a in person:
    print(person[a])
