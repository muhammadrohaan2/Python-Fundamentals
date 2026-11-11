print("Round: 1")
print("Round: 2")
print("Round: 3")
print("Round: 4")
print("Round: 5")

# for loop
for i in (1,2,3,4,5) :
    print(f"Round: {i}")

#Example
items = [1,2,3,4,"Hi"]
for item in items:
    print(f"Round: {item}")


#Example
items = "Python"
for item in items:
    print(f"Round: {item}")

#range
for item in range(2, 10, 2):
    print(f"Round: {item}")


# real time example
scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score
    print("Current Total:", total)
print("Final Total:", total)


# real time example 2
files = ['  Report.csv',  'DaTA.csv' , ' final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(f"Processing {file}")


#Nested loop
for x in range(3): #outer loop
    for y in range(2): #inner loop
        for z in range (2):
            print(f"({x}, {y}, {z})")


#example 2
colors = ['red', 'blue', 'green']
sizes = ['L', 'M', 'S']
for color in colors:
    for size in sizes:
        print(f'{color} -Size {size}')


#example 3
years = [2026, 2027]
months = ['Jan', 'Feb']
days = range(1, 29)

for y in years: 
    for m in months:
        for d in days:
            print(f'report_{y}_{m}_{d}.csv')


#example 4

# SELECT count(*) FROM customers where id IS NULL;
tables = ['customers', 'orders', 'products', 'prices']
columns = [ 'id', 'create_date']
for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')