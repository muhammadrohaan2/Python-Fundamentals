my_set = {10, 30, 20, 10}

print(my_set)   # Unordered # No duplicates (unique)
#print(my_set[1]) # Not indexed
my_set.remove(20)
print(my_set) # Mutable




#**
a = {10, 20, 30, 40}

a.add(50)
#a.update({1,2})
a |= {1, 2}

#a.remove(100)
a.discard(100)
#a.pop()
print(a)


#Math set
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

# union() combines all unique items from both sets
print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a - b)
print(b - a)

print(a.symmetric_difference(b))
print(a ^ b)

# issubset() returns true if all items in this set exist in the order
# issuperset() returns true when it includes all items of the other set 
a = {10, 80}
b = {30, 40, 50, 60}

print(a.issubset(b))
print(b.issuperset(a))

print(a.isdisjoint(b))




