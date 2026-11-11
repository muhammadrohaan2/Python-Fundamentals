names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        print("Empty value detected!")
        break
    print(f'Name = {name}')



#example
emails = [
    'data@gmail.com'
    'python@outlook.com'
    'DROP TABLE USERS;'
    'maria@gmail.com'
]

for email in emails:
    if ';' in email:
        print('SQL injection: Hacker Attack')
        break
    print(f'Processing Email: {email}')
    