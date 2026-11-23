# Create Lists
empty = []
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
mixed = [1, 'a', True, None]
print(mixed)
print(type(mixed))


# list()
empty = list()
print(empty)

letters = list('Python')
print(letters)

numbers = list(range(5))
print(numbers)


# Nested Lists 
matrix = [['a', 'b', 'c'], ['d', 'e', 'f']]
print(matrix)
print(type(matrix))


# Access & Read     **a
lst = ['a', 'b', 'c', 'd']
print(lst)
print(lst[0])
print(lst[-1])


# Access & Read Matrix(Nested List) (Indexing)  **b
matrix = [
    ['a', 'b', 'c'], # Row 0
    ['d', 'e', 'f'], # Row 1
    ['g', 'h', 'i']  # Row 2
]

print(matrix[2][2])
print(matrix[0][0])

# (Slicing)    **a
lst = ['a', 'b', 'c', 'd']
print(lst)
print(lst[0])
print(lst[-1])
print(lst[:2])
print(lst[:])


# **b
matrix = [
    ['a', 'b', 'c'], # Row 0
    ['d', 'e', 'f'], # Row 1
    ['g', 'h', 'i']  # Row 2 
]

print(matrix[:2])
print(matrix[1:])
print(matrix[2][:2]) 


# Unpacking Lists
person = ['Maria', 29, 'Data Engineer', 'Spain']
#name = person[0]
#age = person[1]
#role = person[2]
#country = person[3]

name, age, role, country, = person
print(role)

# Asterisk
person = ['Maria', 29, 'Data Engineer', 'Spain']
name, *details, country, = person

print(name)
print(details)
print(country)


# Rules
numbers = [1, 2, 3, 4]
first, *middle, last = numbers
print(numbers)


#underscore
person = ['Maria', 29, 'Data Engineer', 'Spain']
name, *_, country = person 
print(name)
print(country)


# Explore and Analyze 
numbers = [1, 3, 5, 2, 5]
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))

print("All:", all(numbers))
print("All:", all([1, 0, 2]))
print("All:", all(['a', '', 'b']))
print("All:", all(['a', 'c', 'b']))

print("Any:", any(numbers))
print("Any:", any([1, 0, 2]))
print("Any:", any(['a', '', 'b']))
print("Any:", any([0, 0, 0]))

print("Count:", numbers.count(5))
print("Index:", numbers.index(5))


numbers = [8, 3, 5, 2, 5]
print(5 in numbers)
print(8 not in numbers)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)

list1 = [5, 8, 3]
list2 = [5, 2, 3]
print(list1 < list2)

#Changing
#Adding
letters = ['a', 'b', 'c']
letters.append('x')
letters.append('y')
print(letters)


letters = ['a', 'b', 'c']
letters.insert(0, 'x')
letters.insert(3, 'y')
print(letters)

#Removing
letters = ['a', 'b', 'c']
letters.clear()
print(letters)

letters = ['a', 'b', 'a']
letters.remove('a')
letters.remove('a')
print(letters)


letters = ['a', 'b', 'c']
removed = letters.pop()
print(letters)
print('Removed Item:', removed)

#Updating
letters = ['a', 'b', 'c']
letters[0] = 'x'
letters[1] = 'y'
print(letters)


# Sorting
letters = ['c', 'a', 'b']
letters.sort()
print(letters)

letters = ['c', 'a', 'b']
letters.sort(reverse = True)
print(letters)


letters = ['c', 'a', 'b']
new_list = sorted(letters, reverse = True)
print('Original List:',letters)
print('Sorted List:', new_list)

#reverse()
letters = ['c', 'a', 'b']
letters.reverse()
print(letters)


letters = ['c', 'a', 'b']
new_list = list(reversed(letters))
print('Original List:', letters)
print('Reversed List:', new_list)


#copying
letters = ['a', 'b', 'c']
letters_copy = letters
letters.pop()
letters_copy.append('z')
print('Original:', letters)
print('Copy:', letters_copy)

#copy()
letters = ['a', 'b', 'c']
letters_copy = letters.copy()
#letters.pop()
letters_copy.append('z')
print('Original:', letters)
print('Copy:', letters_copy)


# is operator  

original = [
    ['a', 'b'],  # Row 0
    ['c', 'd'],  # Row 1
]

#Assigment
import copy
copy1 = original 
print("Same Object?", original is copy1, "\n")

#Shallow Copy
copy2 = original.copy()
print("Same Object?", original is copy2)
print("Shared Lists?", original[0] is copy2[0], "\n")

#Deep copy
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3)
print("Shared Lists?", original[0] is copy3[0], "\n")


#Combining
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = [letters, numbers]
print(comb)


letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
numbers.extend(letters)
print(letters)
print(numbers)


letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = list(zip(letters, numbers,))
print(comb)

#real time example
ids = [101, 102, 103]
names = ['Ali', 'Sara', 'John']
print(list(zip(ids, names)))


#Itertors and Iterables
letters = ['a', 'b', 'c']
for l in letters:                   # We use iteration to transform data
    print(l)    


# enumerate
letters = ['a', 'b', 'c']
for index, value in enumerate(letters):
    print(index, value)


# Reversed
letters = ['a', 'b', 'c']
for l in reversed(letters):
    print(l)

# Zip
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
print(list(zip(letters, numbers)))

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

for l, n in zip(letters, numbers):
    print(l, n)

# Map
letters = ['a', 'b', 'c']
print(list(map(str.upper, letters)))    # map is fast, clean way to do data transformations

numbers = ['1', '2', '3']
print(list(map(int, numbers)))

names = [' Maria ', ' John  ', 'kumar  ' ]
for n in map(str.strip, names):
    print(n)


# Filter 
letters = ['a', '', 'c', None , False]
print(list(filter(None, letters)))


items = ['sql', '123', 'python', '42']
for i in filter(str.isalpha, items ):
    print(i)


# lambda
multiple = lambda x: x * 2 
print(multiple(2))

add = lambda x, y : x + y 
print(add(1, 2))

check = lambda i: i in "python"
print(check('n'))

# lambda + map
prices = ['$12.50', '$9.99', '$100.00']
print(list(map(lambda p:  float(p.replace('$', '')), prices)))

# lambda + filter
prices = [120, 30, 300, 80]
print(list(filter(lambda p: p >= 100, prices)))



#example
students = [['Maria', 85], 
            ['Kuamr', 90],
            ['Max', 60]]

print(list(filter(lambda row: row [1] > 70, students)))



# comprehensions
domains = ['www.google.com', 
           'openai.com',
           'localhost',
           'WWW.DATAWITHBARAA.COM']

cleaned = [d for d in domains if '.' in d]
print(cleaned)
           