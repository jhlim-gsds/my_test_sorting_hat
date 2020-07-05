# assign_seat.py
# assign randomly to students person by person, keeping distance each other.
import sqlite3
import csv
import random
conn = sqlite3.connect('test.db')
c = conn.cursor()
# 여기에서 사람수가 좌석수보다 많으면 에러 메세지 출력,
first_pool = []
for row in c.execute('SELECT distinct cid from cluster where number_of_seat-number_owned >0'):
    first_pool.append(*row)
    
user_list = []
for row in c.execute('SELECT users.pid, users.full_name, seat.owner_id from users left join seat on users.pid = seat.owner_id where \
                     seat.owner_id is null'):
    user_list.append(row)
    
while user_list:
    a= user_list.pop()
    b= random.choice(first_pool)
    first_pool.remove(b) 
    #a[0],b 활용해서 seat update
    seat_pool = []
    for row in c.execute(f'SELECT * from seat where cluster_id = {b} and owner_id is null'):
        seat_pool.append(row[0])
    selected_seat = random.choice(seat_pool)
    
    c.execute(f'''UPDATE seat SET owner_id ={str(a[0])} WHERE sid={selected_seat}''')
    
    c.execute(f'''UPDATE cluster SET number_owned =number_owned +1 WHERE cid ={b}''')
    
    if not first_pool:
        first_pool = []
        for row in c.execute('SELECT distinct cid from cluster where number_of_seat-number_owned >0'):
            first_pool.append(*row)
print('done')
conn.commit()
conn.close()
