# and
print(3 > 1 and 5 < 1)
print(3 > 1 and 5 > 1)

# or 
print(3 > 1 or 5 < 1)
print(3 > 1 and 5 > 1)

#Example
#checks if the system is under pressure 
cpu_usage = 70
memory_usage = 50
print(cpu_usage > 90 or memory_usage > 90)


#Example
#Checking user credentials before login
email = True
password = True
print(email and password)


# not

print(not 3 > 2)
print(not True)
print(not False)
print(not not False)

name = ""
print(not name)
print(not 0)


#Example

# Allow access only if the user is logged in
# or they are a guest
# but they must not be banned

is_logged_in = True
is_guest = False
is_banned = True

print((is_logged_in or is_guest) and not is_banned)


