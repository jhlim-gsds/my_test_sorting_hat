from neo4j import GraphDatabase
import random
host = 'bolt://localhost:7687'
user = 'neo4j'
password = 'letmein'
driver = GraphDatabase.driver(host,auth=(user, password))
first_pool = []
second_pool = []
cluster_pool= []
with driver.session() as session:
    answer= session.run("""match (u:user)-[r:owned]-(s:seat)-[r1:BELONGSTO]->(c:cluster)  return c.cid,count(c.cid) ,c.cluster_size""")
    answer = answer.values()
    clusteranswer = session.run("""match (c:cluster) return c.cid,c.cluster_size""")
    clusteranswer = clusteranswer.values()
    for row1 in clusteranswer:
        cluster_pool.append(row1[0])
    for row in answer:
        second_pool.append(row[0])
        if int(row[2])-row[1]>0:
            first_pool.append(row[0])
our_pool= set(cluster_pool)-set(second_pool)
for x in our_pool:
    first_pool.append(x)

user_list = []
with driver.session() as session:
    result_list = []
    result11_list= []
    result = session.run("""match (u:user) return u.pid""")
    result = result.values()
    result11 = session.run("""match (n:user)-[r:owned]-(s:seat) return n.pid""")
    result11 = result11.values()
    for row in result:
        result_list.append(row[0])
    for row in result11:
        result11_list.append(row[0])
    res = set(result_list) - set(result11_list)
    for row in res:
        user_list.append(row)

print('what do you want to do? bulk insert(1), individual insert(2)')
seat_pool1= []
with driver.session() as session:
    seat_result= session.run("""match (s:seat) return s.sid""")
    seat_result = seat_result.values()
    for row in seat_result:
        seat_pool1.append(row[0])

#print(seat_pool1)
users_reaction = input()
if users_reaction =='1':
    while user_list:
        a= user_list.pop()
        b = random.choice(first_pool)
        first_pool.remove(b)
        #seat_pool = []
        #print(seat_pool)
        #print('hello')
        with driver.session() as session:
            seat_pool2 = []
            seat_result2 = session.run("""match (s:seat) where s.cid = {} return s.sid""".format("'"+b+"'"))
            seat_result2 = seat_result2.values()
            #print(seat_result2)
            for row in seat_result2:
                seat_pool2.append(row[0])
            seat_pool3 = []
            seat_result3 = session.run("""match (u:user) -[r:owned]-(s:seat) where s.cid = {} return s.sid""".format("'"+b+"'"))
            seat_result3 = seat_result3.values()
            for row in seat_result3:
                seat_pool3.append(row[0])
            seat_pool4 = []
            for x in seat_pool3:
                seat_result4 = session.run("""match (s:seat)-[r:near]-(s2:seat) where s.cid = {} and s.sid = {} return s2.sid""".format("'"+b+"'","'"+x+"'"))
                seat_result4 = seat_result4.values()
                try:
                    for row in seat_result4:
                        seat_pool4.append(row[0])
                except:
                    print('error')
                    print('check it')

            seat_pool = set(seat_pool2) -set(seat_pool3)
            if len(seat_pool3) <=4:
                seat_pool = set(seat_pool) - set(seat_pool4)

            seat_pool = list(seat_pool)
            selected_seat = random.choice(seat_pool)
            session.run("""match (s:seat),(u:user) where u.pid={a} and s.sid={selected_seat} merge (u)-[r:owned]-(s)"""
                        .format(a="'"+a+"'", selected_seat = "'"+ selected_seat + "'") )
            print(a,' assigned to seat', selected_seat)
            if not first_pool:
                first_pool = []
                second_pool = []
                cluster_pool = []
                answer = session.run("""match (u:user)-[r:owned]-(s:seat)-[r1:BELONGSTO]->(c:cluster)  return c.cid,count(c.cid) ,c.cluster_size""")
                answer = answer.values()
                clusteranswer = session.run("""match (c:cluster) return c.cid,c.cluster_size""")
                clusteranswer = clusteranswer.values()
                for row1 in clusteranswer:
                    cluster_pool.append(row1[0])
                for row in answer:
                    second_pool.append(row[0])
                    if int(row[2]) - row[1] > 0:
                        first_pool.append(row[0])
                our_pool = set(cluster_pool) - set(second_pool)
                for x in our_pool:
                    first_pool.append(x)
elif users_reaction =='2':
    first_pool = []
    second_pool = []
    cluster_pool = []
    with driver.session() as session:
        answer = session.run("""match (u:user)-[r:owned]-(s:seat)-[r1:BELONGSTO]->(c:cluster)  return c.cid,count(c.cid) ,c.cluster_size""")
        answer = answer.values()
        clusteranswer = session.run("""match (c:cluster) return c.cid,c.cluster_size""")
        clusteranswer = clusteranswer.values()
        for row1 in clusteranswer:
            cluster_pool.append(row1[0])
        for row in answer:
            second_pool.append(row[0])
            if int(row[2]) - row[1] > 0:
                first_pool.append(row[0])
        our_pool = set(cluster_pool) - set(second_pool)
        for x in our_pool:
            first_pool.append(x)
    while True:
        user_list = []
        with driver.session() as session:
            result_list = []
            result11_list = []
            result = session.run("""match (u:user) return u.pid""")
            result = result.values()
            # print('hi',result)
            result11 = session.run("""match (n:user)-[r:owned]-(s:seat) return n.pid""")
            result11 = result11.values()
            for row in result:
                result_list.append(row[0])
            for row in result11:
                result11_list.append(row[0])
            res = set(result_list) - set(result11_list)
            # print('res',res)
            for row in res:
                user_list.append(row)
        print('user list without seat: ',user_list)
        print('please type pid')
        a = input()
        if a == 'q':
            break
        if a not in user_list:
            print(a, ' is not in the list', 'if you want to quit program type q')
            continue

        b = random.choice(first_pool)
        first_pool.remove(b)
        seat_pool2 = []
        seat_result2 = session.run("""match (s:seat) where s.cid = {} return s.sid""".format("'"+b+"'"))
        seat_result2 = seat_result2.values()
        # print(seat_result2)
        for row in seat_result2:
            seat_pool2.append(row[0])
        seat_pool3 = []
        seat_result3 = session.run("""match (u:user) -[r:owned]-(s:seat) where s.cid = {} return s.sid""".format("'" + b + "'"))
        seat_result3 = seat_result3.values()
        for row in seat_result3:
            seat_pool3.append(row[0])
        seat_pool4 = []
        for x in seat_pool3:
            seat_result4 = session.run("""match (s:seat)-[r:near]-(s2:seat) where s.cid = {} and s.sid = {} return s2.sid""".format("'"+b+"'","'"+x+"'"))
            seat_result4= seat_result4.values()
            try:
                for row in seat_result4:
                    seat_pool4.append(row[0])
            except:
                print('error')
                print('check it')

        seat_pool = set(seat_pool2) - set(seat_pool3)
        if len(seat_pool3) <=4:
            seat_pool = set(seat_pool) - set(seat_pool4)
        seat_pool = list(seat_pool)
        selected_seat = random.choice(seat_pool)
        session.run("""match (s:seat),(u:user) where u.pid={a} and s.sid={selected_seat} merge (u)-[r:owned]-(s)"""
                    .format(a="'" + a + "'", selected_seat="'" + selected_seat + "'"))
        print(a, ' assigned to seat', selected_seat)
        if not first_pool:
            first_pool = []
            second_pool = []
            cluster_pool = []
            answer = session.run(
                """match (u:user)-[r:owned]-(s:seat)-[r1:BELONGSTO]->(c:cluster)  return c.cid,count(c.cid) ,c.cluster_size""")
            answer = answer.values()
            clusteranswer = session.run("""match (c:cluster) return c.cid,c.cluster_size""")
            clusteranswer = clusteranswer.values()
            for row1 in clusteranswer:
                cluster_pool.append(row1[0])
            for row in answer:
                second_pool.append(row[0])
                if int(row[2]) - row[1] > 0:
                    first_pool.append(row[0])
            our_pool = set(cluster_pool) - set(second_pool)
            for x in our_pool:
                first_pool.append(x)
        print('insert done, do you want to quit? (y/n)')
        mmm =input()
        if mmm =='y':
            break
        elif mmm=='n':
            continue
        else:
            print('please type (y) or (n)')



else:
    print('please type(1) or (2)')
