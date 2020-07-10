from neo4j import GraphDatabase


host = 'bolt://localhost:7687'
user = 'neo4j'
password = 'letmein'
driver = GraphDatabase.driver(host,auth=(user, password))
with driver.session() as session:
    #session.run("""load csv from 'file:///usertable.csv' as row merge (u:user {pid:row[0],full_name:row[1] })""")
    #session.run("""load csv from 'file:///clustertable.csv' as row merge (c:cluster {cid:row[0],cluster_size:row[1]})""")
    #session.run("""load csv from 'file:///seattable.csv' as row merge (s:seat {sid:row[0],cid:row[2]})""")
    session.run("""create constraint on (u:user) assert u.pid is unique""")       #uncomment for the first time
    session.run("""create constraint on (c:cluster) assert c.cid is unique""")     #uncomment for the first time
    session.run("""create constraint on (s:seat) assert s.sid is unique""")        #uncomment for the first time

print('db constraint done')