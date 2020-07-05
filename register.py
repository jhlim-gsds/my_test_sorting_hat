# register.py
# register information of students, seats, clusters into DB

import sqlite3
import csv
conn = sqlite3.connect('test.db')
c= conn.cursor()
def insert_from_csv(path, table):
    c= conn.cursor()
    if table =='1':
        usertable = open(path,'r')
        reader = csv.reader(usertable)
        user=[]
        for row in reader:
            user.append(tuple(row))
        c.executemany('''INSERT INTO users VALUES (?,?)''',user)
        print('insert user table completed')
        conn.commit()
        conn.close()
    elif table =='2':
        clustertable = open('clustertable.csv','r')
        reader = csv.reader(clustertable)
        cluster = []
        for row in reader:
            cluster.append(tuple(map(int,row)))
        
        c.executemany('''INSERT INTO cluster VALUES (?,?,?)''',cluster)
        print('insert cluster table completed')
        conn.commit()
        conn.close()
    
    elif table=='3':
        seattable = open('seattable.csv','r')
        reader= csv.reader(seattable)
        seat = []
        conv = lambda i : i or None
        for row in reader:
            try:
                seat.append(((int(row[0]),conv(row[1]),int(conv(row[2])))))
            except TypeError:
                seat.append(((int(row[0]),conv(row[1]),conv(row[2]))))
        
        c.executemany('''INSERT INTO seat VALUES (?,?,?)''',seat)
        print('insert cluster table completed')
        conn.commit()
        conn.close()
    else:
        print('error', ' ', 'please type 1 or 2 or 3' )
        #todo raise error
            
        
    return

def insert_from_command():
    conv = lambda i : i or None
    print("choose the table")
    cursor = conn.execute("SELECT name \
            FROM sqlite_master \
            WHERE type IN('table', 'view') AND name NOT LIKE 'sqlit_%' \
            UNION ALL \
              SELECT name FROM sqlite_temp_master \
              WHERE type IN ('table', 'view') ORDER BY 1;")
    for row in cursor:
        print(row)
    c = conn.cursor()
    print("what table? user(1), cluster(2), seat(3)")
    table= input()
    if table =='1':
        while True:
            print('please type user pid')
            pid = input()
            print('please type user full name')
            full_name = input()
            result = (pid,full_name)
            c.execute('''INSERT INTO users VALUES (?,?)''',result)
            print('insert completed')
            print('Do you want to quit?  (y/n)')
            answer = input()
            if answer =='y':
                conn.commit()
                conn.close()
                break
            
    elif table =='2':
        while True:
            print('please type cluster id (cid)')
            cid = int(input())
            print('please type number_of_seat')
            number_of_seat = int(input())
            print('please type number_owned')
            number_owned = int(input())
            result = (cid, number_of_seat, number_owned)
            c.execute('''INSERT INTO cluster VALUES (?,?,?)''', result)
            print('insert completed')
            print('Do you want to quit? (y/n)')
            answer = input()
            if answer =='y':
                conn.commit()
                conn.close()
                break
    
            
    elif table =='3':
        while True:
            print('please type seat id (sid)')
            sid  = int(input())
            print('please type owner_id')
            owner_id = input()
            print('please type cluster_id (cid)')
            cluster_id = input()
            try:
                cluster_id = int(cluster_id)
            except ValueError:
                print('cluster_id must be int')
            
            result = (sid,conv(owner_id),conv(cluster_id))
            c.execute('''INSERT INTO seat VALUES (?,?,?)''', result)
            print('insert completed')
            print('Do you want to quit? (y/n)')
            answer = input()
            if answer =='y':
                conn.commit()
                conn.close()
                break
    else:
        print('error')
        #todo raise error
                
    # TODO: remaining insert process. you can modify overall interface of course.

    return


def insert_interface():
    print("csv(1) or command(2)?")
    mode = input()
    if mode=='1': #CSV
        print("enter the file path")
        path = input()
        print("what table? user(1), cluster(2), seat(3)")
        table = input()
        insert_from_csv(path, table)
        # TODO


    elif mode=='2': #COMMAND
        insert_from_command()
        # TODO

    else:
        print("error")
        # TODO: raise error

if __name__=='__main__':
    insert_interface()
