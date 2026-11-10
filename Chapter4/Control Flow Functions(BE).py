# bool()
print(bool(123))
print(bool("Hi"))
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))

# any()
email = ""
phone = "017-788334"
username = ""
#Allows registration
#if any field is filled
print(any([email, phone, username]))


# all()
email = "Muhammad4@gmail.com"
phone = "017-788334"
username = "Muhammad"
#Allows registration
#only if all fields is filled
print(all([email, phone, username]))


# isinstance()
print(isinstance(123, int))
print(isinstance(True, str))

print("Hello".endswith("o"))
print("Hello".startswith("H"))


