names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        print("Empty value detected!")
        continue
    print(f'Name = {name}')


    #example

#skip weekends in calendar loop
days = ['Mon', 'Sun', 'Wed' , 'Tue']
weekends = ['Sat', 'Sun']
for day in days:
    if day in weekends:
        continue 
    print(F'Workday: {day}') 


    