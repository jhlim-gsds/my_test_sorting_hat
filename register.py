# register.py
# register information of students, seats, clusters into DB

import sqlite3

conn = sqlite3.connect('test.db')

def insert_from_csv(path, table):
    
    return

def insert_from_command():
    print("choose the table")
    cursor = conn.execute("SELECT name \
            FROM sqlite_master \
            WHERE type IN('table', 'view') AND name NOT LIKE 'sqlit_%' \
            UNION ALL \
              SELECT name FROM sqlite_temp_master \
              WHERE type IN ('table', 'view') ORDER BY 1;")
    for row in cursor:
        print(row)
    # TODO: remaining insert process. you can modify overall interface of course.

    return


def insert_interface():
    print("csv(1) or command(2)?")
    mode = input()
    if mode=='1': #CSV
        print("enter the file path")
        path = input()
        print("what table?")
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
