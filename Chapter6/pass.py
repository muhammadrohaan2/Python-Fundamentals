names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        pass #todo: Handle Empty Value
    print(f'Name = {name}')


#Step 2
names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
         name = name.replace('', 'unknown')
    print(f'Name = {name}')


    