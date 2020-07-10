from neo4j import GraphDatabase
host = 'bolt://localhost:7687'
user = 'neo4j'
password = 'letmein'
driver = GraphDatabase.driver(host,auth=(user, password))
seat_pool1= []
cluster_pool = []
with driver.session() as session:
    seat_result= session.run("""match (s:seat) return s.sid""")
    seat_result = seat_result.values()
    for row in seat_result:
        seat_pool1.append(row[0])
    cluster_result = session.run("""match (c:cluster) return c.cid""")
    cluster_result = cluster_result.values()
    for row in cluster_result:
        cluster_pool.append(row[0])

#print(cluster_pool)
while True:
    while True:
        print('current we have following seat', seat_pool1)
        print('please type sid')
        user_answer =input()
        if user_answer not in seat_pool1:
            print('please check sid')
            continue
        break

    with driver.session() as session:
        result = session.run("""match (s:seat)-[:BELONGSTO]-(c:cluster) where s.sid ={} return s.sid, c.cid""".format("'"+user_answer+"'"))
        result =result.values()
        if result:
            print(user_answer,' belongs to cluster ',result[0][1])
            print('do you want to change? (y/n)')
            mmm = input()
            if mmm =='y':
                while True:
                    print('current cid list: ', cluster_pool)
                    print('please type cid')
                    user_cid = input()
                    if user_cid not in cluster_pool:
                        print("please type cid properly, cid must be in above list")
                        continue
                    break
                session.run("""match (s:seat)-[r:BELONGSTO]->(c:cluster) where s.sid ={} delete r """.format("'"+user_answer+"'"))
                session.run("""match (s:seat), (c:cluster) where s.sid = {} and c.cid ={} create (s)-[r:BELONGSTO]->(c)"""
                            .format("'"+user_answer+"'","'"+user_cid+"'"))
                print(user_answer, 'belongs to cluster', user_cid)
            elif mmm =='n':
                print('good bye')

            else:
                print('mmm please type(y) or (n) next time')


        else:
            print("currently seat ",user_answer," does not belong anywhere")
            print('do you want to assign cluster? (y/n)')
            mmm = input()
            if mmm=='y':
                while True:
                    print('current cid list: ', cluster_pool)
                    print('please type cid')
                    user_cid = input()
                    if user_cid not in cluster_pool:
                        print("please type cid properly, cid must be in above list")
                        continue
                    break
                session.run("""match (s:seat), (c:cluster) where s.sid = {} and c.cid ={} create (s)-[r:BELONGSTO]->(c)"""
                            .format("'" + user_answer + "'", "'" + user_cid + "'"))

                print(user_answer,'belongs to cluster', user_cid)



            elif mmm =='n':
                print('good bye')
            else:
                print('mmm please type (y) or (n) next time')

    print('do you want to quit? (y/n)')
    quit_answer = input()
    if quit_answer =='y':
        break
    else:
        continue