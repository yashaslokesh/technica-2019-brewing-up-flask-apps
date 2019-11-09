x = 4

# Conditionals
if x > 5:
    print('Greater')
else:
    print('Lesser or Equal To')
print()

# Prints all even numbers between 0 and 10 (not including 10)
for i in range(0, 10, 2):
    print(i)
print()

# Strings
s = "Technica"

print(len(s))
print(s[5:])
print(s[:5])
print(s[::-1])
print()

# Lists
l = ['Zebra', 2, 3, ['Nested List', 5.0], 2.0]

print('Zebra' in l)
print('Nested List' in l)
print('Nested List' in l)
print()

# Dictionaries (like maps or hash tables)
d = {1: 'one', 2: 'two', 3: 'three'}
print(type(dict))
print()

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Built in functions
print(sum(l))
print(sum(range(10)))

print(max([3, 4, 8, 1, 2, 6, 8]))

# Lambda x is a function with a parameter of x. It returns True or False depending
# on whether a number is even or not
# We map this function to each element of the list, so map returns a list of
# True and False values
print(list(map(lambda x: x % 2 == 0, l)))
# We filter the list, keeping only the elements that are even.
print(list(filter(lambda x: x % 2 == 0, l)))
