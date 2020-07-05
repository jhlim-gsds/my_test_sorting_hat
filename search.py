# search.py
# search registered information from DB tables
import sqlite3
conn = sqlite3.connect('test.db')
c= conn.cursor()
print('what do you want to see? all student table(1), all seat table(2), student with seat(3)')
query = input()
if query =='1':
    for row in c.execute('''SELECT * FROM users'''):
        print(row)
elif query =='2':
    for row in c.execute('''SELECT * FROM seat'''):
        print(row)
elif query =='3':
    for row in c.execute('''SELECT * FROM users LEFT JOIN seat ON users.pid = seat.owner_id'''):
        print(row)
        
else:
    print('error')
