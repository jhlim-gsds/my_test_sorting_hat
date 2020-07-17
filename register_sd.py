# register.py
# register information of students, seats, clusters into DB

# no.    path
# 1      'usertable.csv'
# 2      'clustertable.csv'
# 3      'seattable.csv'

import sqlite3
import csv
conn = sqlite3.connect('test.db')
c= conn.cursor()
def insert_from_csv(path, table):
    try:
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
            usertable.close()
            flag = False

        elif table =='2':
            clustertable = open(path,'r')
            reader = csv.reader(clustertable)
            cluster = []
            for row in reader:
                cluster.append(tuple(map(int,row)))
            
            c.executemany('''INSERT INTO cluster VALUES (?,?,?)''',cluster)
            print('insert cluster table completed')
            conn.commit()
            conn.close()
            clustertable.close()
            flag = False

        elif table=='3':
            seattable = open(path,'r')
            reader= csv.reader(seattable)
            seat = []
            conv = lambda i : i or None
            for row in reader:
                try:
                    seat.append(((int(row[0]),conv(row[1]),int(conv(row[2]),conv(row[3])))))
                except TypeError:
                    seat.append(((int(row[0]),conv(row[1]),conv(row[2]),conv(row[3]))))
            
            c.executemany('''INSERT INTO seat VALUES (?,?,?,?)''',seat)
            print('insert seat table completed')
            conn.commit()
            conn.close()
            seattable.close()
            flag = False

        elif table == 'q':
            print('goodbye')
            flag = False

        else:
            print('error', ' ', 'please type 1 or 2 or 3' )
            flag = True            

    except Exception as e:
        print('### ERROR!! ###')
        print(e, '\n')
        flag = True

    finally:
        return flag

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

    flag = True
    def ask_to_end():
        print('Do you want to quit?  (y/n)')
        answer = input()
        if answer =='y':
            conn.commit()
            conn.close()
            print('goodbye')
            flag = False
        else:
            flag = True
        return flag

    print("what table? user(1), cluster(2), seat(3)")
    table= input()

    while flag:
        if table =='1':
            print('please type user pid')
            pid = input()
            if pid == 'q':
                print('goodbye')
                flag = False
                break

            print('please type user full name')
            full_name = input()
            if full_name == 'q':
                print('goodbye')
                flag = False
                break

            result = (pid,full_name)
            c.execute('''INSERT INTO users VALUES (?,?)''', result)
            print('insert completed')
            flag = ask_to_end()
                
        elif table =='2':
            print('please type cluster id (cid)')
            try:
                tmp = input()
                if tmp == 'q':
                    print('goodbye')
                    flag = False
                    break

                cid = int(tmp)
            except ValueError as e:            
                print('### ERROR!! ###')
                print(e)
                print('cid must be an INTEGER\n')
                continue                        
            
            print('please type number_of_seat')
            try:
                tmp = input()
                if tmp == 'q':
                    print('goodbye')
                    flag = False
                    break
                
                number_of_seat = int(tmp)
            except ValueError as e:
                print('### ERROR!! ###')
                print(e)
                print('number_of_seat must be an INTEGER\n')
                continue
            
            print('please type number_owned')
            try:
                tmp = input()
                if tmp == 'q':
                    print('goodbye')
                    flag = False
                    break

                number_owned = int(tmp)
            except ValueError as e:
                print('### ERROR!! ###')
                print(e)
                print('number_owned must be an INTEGER\n')
                continue
            
            result = (cid, number_of_seat, number_owned)
            c.execute('''INSERT INTO cluster VALUES (?,?,?)''', result)
            print('insert completed')
            flag = ask_to_end()      
                
        elif table =='3':
            print('please type seat id (sid)')
            try:
                tmp = input()
                if tmp == 'q':
                    print('goodbye')
                    flag = False
                    break
                
                sid = int(tmp)
            except ValueError as e:
                print('### ERROR!! ###')
                print(e)
                print('sid must be an INTEGER\n')
                continue
            
            print('please type owner_id')
            owner_id = input()
            if owner_id == 'q':
                print('goodbye')
                flag = False
                break
            
            print('please type cluster_id (cid)')
            try:
                tmp = input()
                if tmp == 'q':
                    print('goodbye')
                    flag = False
                    break
                
                cluster_id = int(tmp)
            except ValueError as e:
                print('### ERROR!! ###')
                print(e)
                print('cluster_id must be an INTEGER\n')
                continue
            print('please type adjacent sid if it doesnt have adjacent seat just type enter')
            adjacency_sid = input()
            if adjacency_sid =='q':
                print('goodbye')
                flag =False
                break

            result = (sid,conv(owner_id),conv(cluster_id),conv(adjacency_sid))

            c.execute('''INSERT INTO seat VALUES (?,?,?,?)''', result)
            print('insert completed')
            flag = ask_to_end()

        elif table == 'q':
            print('goodbye')
            flag = False
            
        else:
            print('error', ' ', 'please type 1 or 2 or 3' )
            flag = True
                
        # TODO: remaining insert process. you can modify overall interface of course.
    return

def insert_interface():
    print("csv(1) or command(2)?  (cf. type 'q' to exit!!)")
    mode = input()
    if mode=='1': #CSV
        flag = True
        while flag:
            print("enter the file path (ex: usertable.csv, ../usertable.csv, etc.)")
            path = input()
            if path == 'q':
                print('goodbye')
                break
            print("what table? user(1), cluster(2), seat(3)")
            table = input()
            flag = insert_from_csv(path, table)
            # TODO

    elif mode=='2': #COMMAND
        insert_from_command()

    elif mode=='q':
        print('goodbye')

    else:
        print('error', ' ', 'please type 1 or 2\n')
        insert_interface()
        # TODO: raise error

if __name__=='__main__':
    insert_interface()
