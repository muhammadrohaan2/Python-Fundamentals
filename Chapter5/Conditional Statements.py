
# if
score = 100
if score >= 90:
    print("A")


# else
score = 100
if score >= 90:
    print("A")
else:
    print("F")


# elif
score =86
submitted_project = True 
if score >= 90 and submitted_project:      #Connecting Conditions
    print("A+")
elif score >= 90:
    print("A")
elif score >=80:     #elif elif 
    print("B")
elif score >=70:
    print("C")
elif score >=60 or submitted_project:
    print("D")
else:   
    print("F")



# Independent if
score = 50
submitted_project = True

if score >= 90:
    print("High Score")
else:
    print("Low Score")

if submitted_project:
    print("Project is submitted")
else:
     print("Project is not submitted")



#Inline If (Ternary)

score = 100
if score >= 90:
    print("A")
else:
    print("F")

score = 100
print("A" if score >= 90 else "F")


#Example 2
score = 100 
if score >= 90:     
    print("A")
elif score >=80:     #elif elif 
    print("B")
else:
    print("F")


score = 100 
grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)


#match case
country = "United States"
if country == "United States":
    print("US")
elif country == "Egypt":
    print("EG")
elif country == "Germany":
    print("GE")
else:
    print("Unknown Country")


country = "USA"
match country:             #match case
    case "United States" | "USA":
        print("US")
    case "Egypt":
        print("EG")
    case "Germany":
        print("GE")
    case _:
         print("Unknown Country")