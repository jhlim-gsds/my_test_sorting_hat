# assign_seat.py
# assign randomly to students person by person, keeping distance each other.
import sqlite3
import csv
import random
conn = sqlite3.connect('test.db')
c = conn.cursor()
# 여기에서 사람수가 좌석수보다 많으면 에러 메세지 출력,
first_pool = []
for row in c.execute('SELECT distinct cid FROM cluster WHERE number_of_seat-number_owned >0'):
    first_pool.append(*row)
    
user_list = []
for row in c.execute('SELECT users.pid, users.full_name, seat.owner_id FROM users LEFT JOIN seat ON users.pid = seat.owner_id WHERE \
                     seat.owner_id is null'):
    user_list.append(row)

pid_list = []
for row in c.execute('SELECT users.pid FROM users LEFT JOIN seat ON users.pid = seat.owner_id WHERE \
                     seat.owner_id is null'):
    pid_list.append(*row)

print('what do you want to do? bulk insert(1), individual insert(2)')
print("(cf. type 'q' to exit!!)")
users_reaction = input()

if users_reaction =='1':
    while user_list:
        a= user_list.pop()
        b= random.choice(first_pool)
        first_pool.remove(b) 
        #a[0],b 활용해서 seat update
        seat_pool = []
        for row in c.execute('''SELECT * from seat where cluster_id = ? and owner_id is null''', (b,) ):
            seat_pool.append(row[0])
        occupied_seat = []
        for row in c.execute('''SELECT * from seat where cluster_id = ? and owner_id is not null''',(b,) ):
            occupied_seat.append(row[0])
        sd_pool = []
        for xx in occupied_seat:
            for row in c.execute('''SELECT * from seat where cluster_id = ? and near = ?''',(b,xx)):
                sd_pool.append(row[0])
        mmm_test = set(seat_pool) - set(sd_pool)
        mmm_test = list(mmm_test)
        if len(occupied_seat) <=4:
            selected_seat = random.choice(mmm_test)
        else:
            selected_seat = random.choice(seat_pool)

        c.execute('''UPDATE seat SET owner_id =? WHERE sid=?''', (str(a[0]),selected_seat) )
        print(f'assign {a[1]} to seat {selected_seat}')

        c.execute('''UPDATE cluster SET number_owned =number_owned +1 WHERE cid =?''', (b,) )

        if not first_pool:
            first_pool = []
            for row in c.execute('SELECT distinct cid from cluster where number_of_seat-number_owned >0'):
                first_pool.append(*row)
    print('done')
    conn.commit()
    conn.close()
    
elif users_reaction=='2':
    first_pool = []
    for row in c.execute('SELECT distinct cid from cluster where number_of_seat-number_owned >0'):
        first_pool.append(*row)

    while True:
        print('students that do not have a seat:', pid_list)
        
        if pid_list:            
            print('please type pid')
            mm = input()
            if mm == 'q':
                print('goodbye')
                break            
            elif mm not in pid_list:
                print('select a pid in the list!!')
                continue
                        
            b= random.choice(first_pool)
            first_pool.remove(b)
            seat_pool = []
            for row in c.execute('''SELECT * from seat WHERE cluster_id = ? AND owner_id IS NULL''', (b,) ):
                seat_pool.append(row[0])
            occupied_seat =[]
            for row in c.execute('''SELECT * from seat WHERE cluster_id = ? AND owner_id is not NULL''',(b,)):
                occupied_seat.append(row[0])
            sd_pool =[]
            for xx in occupied_seat:
                for row in c.execute('''SELECT * from seat WHERE cluster_id = ? AND near = ?''',(b,xx)):
                    sd_pool.append(row[0])
            mmm_test = set(seat_pool) - set(sd_pool)
            mmm_test = list(mmm_test)
            if len(occupied_seat) <=4:
                selected_seat = random.choice(mmm_test)
            else:
                selected_seat = random.choice(seat_pool)

            c.execute('''UPDATE seat SET owner_id =? WHERE sid=?''', (str(mm), selected_seat))
            print(f'assign {mm} to seat {selected_seat}')
            c.execute('''UPDATE cluster SET number_owned =number_owned +1 WHERE cid =?''', (b,) )
            conn.commit()
            if not first_pool:
                first_pool = []
                for row in c.execute('SELECT distinct cid from cluster where number_of_seat-number_owned >0'):
                    first_pool.append(*row)

            pid_list.remove(mm)
            if not pid_list:
                print('Every student has a seat. Goodbye.')
                break    

            print('insert done, do you want to quit? (y/n)')
            mmm = input()
            if mmm == 'y':
                print('goodbye')
                break
        else:
            print('Every student has a seat. Goodbye.')
            break
    conn.close()

elif users_reaction == 'q':
    print('goodbye')
