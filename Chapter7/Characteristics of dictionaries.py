# Dictionaries
my_dict = { 
    'a' : 10,
    'b' : 20, 
    'c' : 20,
    'a' : 40 
}

print(my_dict) # Ordered 
# Keys are unique
# Value allow duplicates
print(my_dict['b']) # Not Indexed, it is keyed 
my_dict['c'] = 80
print(my_dict) # Mutable




user = {"id":1, "age": 30, "city": "berlin"}

#Access
#print(user["name"])
print(user.get("name", "Unknown"))

#Checks
print("age" in user)
print("name" not in user)

#View Objects
print(user.keys())
print(user.values())
print(user.items())



user = {"id":1, "age": 30, "city": "berlin"}

#Looping
for u in user:
    print(u, user[u])

for key, value in user.items():
    print(key, value)



user = {"id":1, "age": 30, "city": "berlin"}

# Add, Remove, Update 
user["name"] = "John" # Add 
user["age"] = 35 #Update
user.update({"age": 40, "city": "Paris"})
print(user)

age = user.pop("salary", "Not Found")
print(user)
print("Removed Item:", age)

user.popitem()
print(user)



# Creation 
user = {"id": None,
        "name": None,
        "age": None,
        "city": None 
        }

user = dict.fromkeys(["id", "name",  "age", "city"], None)
print(user)
user["age"] = 40
print(user)
# fromkeys() builds a new dictionary where all keys get the same default value
