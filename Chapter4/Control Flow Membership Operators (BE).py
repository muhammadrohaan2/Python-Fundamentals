#in
print("o" in  "python")

print("f" not in  "python")

print(3  in [1,2,3])

#Example

# Security check: ensure the domain is not banned 
domain = "@gmail.com"
banned_domains = ["spam.com", "fake.org" , "bot.net"]
print(domain not in banned_domains)