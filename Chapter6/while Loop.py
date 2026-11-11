count = 1
while count <=10:
    print(count)
    count += 2


#example
answer = ""
while answer != "yes":
    answer = input ("Do you agree? (yes/no)")
    print("Thank you")


#while True 

while True: 
    answer = input ("Do you agree? (yes/no): ")
    if answer == "yes":
        break
    print("Thank you!")


#example
# 3 attempts
# yes within  three attempts -> "Glad we're on the same page"
# Otherwise "3 strikes. You're out!"
attempts = 0
while attempts < 3: 
    answer = input ("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we're on the same page")
        break
    attempts += 1
else:
    print("3 strikes. You're out!")
