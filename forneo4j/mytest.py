from neo4j import GraphDatabase


host = 'bolt://localhost:7687'
user = 'neo4j'
password = 'letmein'
driver = GraphDatabase.driver(host,auth=(user, password))

with driver.session() as session:
    session.run("""load csv from 'file:///usertable.csv' as row merge (u:user {pid:row[0],full_name:row[1] })""")
    session.run("""load csv from 'file:///clustertable.csv' as row merge (c:cluster {cid:row[0],cluster_size:row[1]})""")
    session.run("""load csv from 'file:///seattable.csv' as row merge (s:seat {sid:row[0],cid:row[2]})""")
    session.run("""create constraint on (u:user) assert u.pid is unique""")       #uncomment for the first time
    session.run("""create constraint on (c:cluster) assert c.cid is unique""")     #uncomment for the first time
    session.run("""create constraint on (s:seat) assert s.sid is unique""")        #uncomment for the first time
    session.run("""match (s:seat), (c:cluster) where s.cid = c.cid merge (s) -[r:BELONGSTO]->(c) return type(r)""")
    #match (u:user), (s:seat) where u.pid="1" and s.sid="3" create (u)-[r:owned] ->(s) return type(r)
    #session.run("""load csv from 'file:///relation.csv' as row match (u:user {pid:row[0]}),(s:seat {sid:row[1]})
    #merge (u)-[r:owned]-(s)""")

print('import completed')
'''
with driver.session() as session:
    result= session.run(""""""match (u:user) where not (u)-[:owned]-() return u.pid""")
    result = result.values()
    print(result)
    #print(type(result.values()[0][0]))
    print(bool(result))
'''