from neo4j import GraphDatabase


host = 'bolt://localhost:7687'
user = 'neo4j'
password = 'letmein'
driver = GraphDatabase.driver(host,auth=(user, password))

print('what do you want to input? user(1), cluster(2), seat(3)')

answer = input()
if answer =='1':
    while True:
        while True:
            print('please type pid for user pid must be integer')
            answer1= input()
            try:
                answer1 = int(answer1)
            except:
                print('pid must be integer')
                continue
            answer1 = str(answer1)
            break
        print('please type fullname for user')
        answer2 = input()
        print('{'+'pid : {answer1} , full_name: {answer2}'.format(answer1= answer1,answer2= answer2)+'}')

        with driver.session() as session:
            session.run("""merge (u:user {hello})""".format(hello ='{'+'pid : {answer1} , full_name: {answer2}'
                                                        .format(answer1= str(answer1),answer2="'"+answer2+"'" )+'}' ))
        print('insert done')
        print('do you want to quit? (y/n)')
        qq = input()
        if qq == 'y':
            break
elif answer =='2':
    while True:
        while True:
            print('please type cid for user cid must be integer')
            answer1= input()
            try:
                answer1 = int(answer1)
            except:
                print('cid must be integer')
                continue
            answer1 = str(answer1)
            break
        while True:
            print('please type cluster size for cluster, cluster size must be integer')
            answer2= input()
            try:
                answer2= int(answer2)
            except:
                print('cluster size must be integer')
                continue
            answer2= str(answer2)
            break
        print('{'+'cid : {answer1} , cluster_size: {answer2}'.format(answer1= answer1,answer2= answer2)+'}')
        with driver.session() as session:
            session.run("""merge (c:cluster {hello})""".format(hello ='{'+'cid : {answer1} , cluster_size: {answer2}'
                                                        .format(answer1= str(answer1),answer2="'"+answer2+"'" )+'}' ))
        print('insert done')
        print('do you want to quit? (y/n)')
        qq = input()
        if qq == 'y':
            break




elif answer =='3':
    while True:
        while True:
            print('please type sid for seat sid must be integer')
            answer1= input()
            try:
                answer1 = int(answer1)
            except:
                print('sid must be integer')
                continue
            answer1 = str(answer1)
            break
        while True:
            print('please type cid for seat cid must be integer')
            answer2= input()
            try:
                answer2 = int(answer2)
            except:
                print('cid must be integer')
                continue
            answer2 = str(answer2)
            break
        print('{' + 'sid : {answer1} , cid: {answer2}'.format(answer1=answer1, answer2=answer2) + '}')
        with driver.session() as session:
            session.run("""merge (s:seat {hello})""".format(hello ='{'+'sid : {answer1} , cid: {answer2}'
                                                        .format(answer1= str(answer1),answer2="'"+answer2+"'" )+'}' ))
        print('insert done')
        print('do you want to quit? (y/n)')
        qq = input()
        if qq == 'y':
            break
else:
    print('please type (1),(2),(3), you can restart the program')
'''
with driver.session() as session:
    session.run("""load csv from 'file:///usertable.csv' as row merge (u:user {pid:row[0],full_name:row[1] })""")
    session.run("""load csv from 'file:///clustertable.csv' as row merge (c:cluster {number_of_seat:row[1],number_owned:row[2],cid:row[0]})""")
    session.run("""load csv from 'file:///seattable.csv' as row merge (s:seat {cluster_id:row[2],sid:row[0]})""")
    #session.run("""create constraint on (u:user) assert u.pid is unique""")
    #session.run("""create constraint on (c:cluster) assert c.cid is unique""")
    #session.run("""create constraint on (s:seat) assert s.sid is unique""")
    session.run("""match (s:seat), (c:cluster) where s.cluster_id = c.cid merge (s) -[r:BELONGSTO]->(c) return type(r)""")
    #match (u:user), (s:seat) where u.pid="1" and s.sid="3" create (u)-[r:owned] ->(s) return type(r)
    #session.run("""load csv from 'file:///relation.csv' as row match (u:user {pid:row[0]}),(s:seat {sid:row[1]})
    #merge (u)-[r:owned]-(s)""")
'''
'''with driver.session() as session:
    result= session.run("""match (u:user) where not (u)-[:owned]-() return u.pid""")
    result = result.values()
    print(result)
    #print(type(result.values()[0][0]))
    print(bool(result))
'''