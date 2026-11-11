#else + break in for loop
items = [1 , 2 ,4, 7]
for i in items:
    if i % 2 == 0:
        print("Even Nr. Found:", i)
        break
else:
    print("All numbers are odd")


#example 2
names = ['Kamara', 'Tuba', 'Maria', 'Mounika']

for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are avaiable")



