# db_init.py
# db initialize at the first time, only once.
import sqlite3

conn = sqlite3.connect('test.db')
c= conn.cursor()
#create user table
c.execute('''CREATE TABLE users (pid varchar(100) NOT NULL PRIMARY KEY, full_name VARCHAR(100))''')

print('user table created')

#create cluster table

c.execute('''CREATE TABLE cluster (cid int NOT NULL PRIMARY KEY, number_of_seat int, number_owned int)''')

print('cluster table created')

#create seat table

c.execute('''CREATE TABLE seat (sid int NOT NULL PRIMARY KEY, owner_id VARCHAR(100) unique, cluster_id int,near int,
        FOREIGN KEY (owner_id) REFERENCES user (pid) ON DELETE SET NULL ON UPDATE SET NULL, FOREIGN KEY (cluster_id)
        REFERENCES cluster (cid) ON DELETE SET NULL ON UPDATE SET NULL)''')

print('seat table created')

conn.commit()
conn.close()


