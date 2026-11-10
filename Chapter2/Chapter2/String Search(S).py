# startswith()
phone = "+49-176-12435"
print(phone.startswith("+49")) 


# endswith()
email = "muhammad@gmail.com"
print(email.endswith("@gmail.com"))


# in 
email = "muhammad@gmail.com"
print("@" in email)

url = "https://api.company.com/v1/data"
print("/api" in url)


# find
phone1 = "+49-176-12435"
phone2 = "+49-541-19931"

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])


print(phone1.find("-"))


