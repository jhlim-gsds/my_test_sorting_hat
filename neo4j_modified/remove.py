from neo4j import GraphDatabase
host = 'bolt://localhost:7687'
user = 'neo4j'
password = 'letmein'
driver = GraphDatabase.driver(host,auth=(user, password))
#while True로 계속 반복?
print('what do you want to remove? (user (1), seat(2), cluster (3)', 'if you want to quit type q')
user_answer = input()

if user_answer =='1':
    print('please type pid for user')
    with driver.session() as session:
        result_list = []
        result = session.run("""match (u:user) return u.pid""")
        result = result.values()
        for row in result:
            result_list.append(row[0])
        print(result_list)
        while True:
            user_type_pid = input()
            if user_type_pid not in result_list:
                print('please type pid in above list')
                continue
            break
        result_list1 =[]
        result1 = session.run("""match (u:user)-[r:owned]-(s:seat) where u.pid ={} return s.sid"""
                              .format("'"+user_type_pid+"'"))
        result1 = result1.values()
        if result1:
            for row in result1:
                result_list1.append(row[0])
            print('currently',user_type_pid,'has seat', result_list1)
            print('If you delete the node, relationship(owned) also removed.')
            print('Do you want to remove', user_type_pid ,'node? (y/n)')
            remove_user_node = input()
            if remove_user_node =='y':
                session.run("match (u:user)-[r:owned]-(s:seat) where u.pid ={} delete r,u".format("'"+user_type_pid+"'"))
                print('remove done')
            elif remove_user_node == 'n':
                print('okay', user_type_pid, 'is not removed')
            else:
                print('please type (y) or (n)')



        else:
            print('currently',user_type_pid,'has no seat')
            print('do you want to remove', user_type_pid,'user node? (y/n)')
            remove_user_node = input()
            if remove_user_node == 'y':
                session.run("match (u:user) where u.pid = {} delete (u)".format("'"+user_type_pid+"'"))
                print('remove done')
            elif remove_user_node =='n':
                print('okay', user_type_pid,'is not removed')
            else:
                print('please type (y) or (n)')







elif user_answer =='2':
    print("please type sid")
    with driver.session() as session:
        result_list = []
        result = session.run("""match (s:seat) return s.sid""")
        result = result.values()
        for row in result:
            result_list.append(row[0])
        print(result_list)
        while True:
            user_type_sid = input()
            if user_type_sid not in result_list:
                print('please type sid in above list')
                continue
            break
        result_list1= []
        result1 = session.run("""match (c:cluster)-[r:BELONGSTO]-(s:seat) where s.sid = {} return c.cid"""
                              .format("'"+user_type_sid+"'"))
        result1 = result1.values()
        print(user_type_sid, 'belongs to', result1)
        result_list2= []
        result2 = session.run("""match (u:user)-[r1:owned]-(s:seat) where s.sid ={} return u.pid"""
                              .format("'"+user_type_sid+"'"))
        result2= result2.values()
        print(result2, 'owned', user_type_sid)
        while True:
            print('If you delete the node, relationship(owned) also removed.')
            print('Do you want to remove', user_type_sid, 'node? (y/n)')
            remove_seat_node = input()
            if remove_seat_node == 'y':
                session.run("match (s:seat)-[r:BELONGSTO]->(c:cluster) where s.sid ={} delete r".format(
                    "'" + user_type_sid + "'"))
                session.run("""match (u:user)-[r1:owned]-(s:seat) where s.sid ={} delete r1"""
                            .format("'" + user_type_sid + "'"))
                session.run("""match (s:seat) where s.sid = {} delete s""".format("'"+user_type_sid+"'"))
                print('remove done')
                break
            elif remove_seat_node == 'n':
                print('okay', user_type_sid, 'is not removed')
                break
            else:
                print('please type (y) or (n)')
                continue


elif user_answer =='3':
    print("please type cid")
    with driver.session() as session:
        result_list = []
        result = session.run("""match (c:cluster) return c.cid""")
        result = result.values()
        for row in result:
            result_list.append(row[0])
        print(result_list)
        while True:
            user_type_cid = input()
            if user_type_cid not in result_list:
                print('please type cid in above list')
                continue
            break
        result_list1= []
        result1 = session.run("""match (c:cluster)-[r:BELONGSTO]-(s:seat) where c.cid = {} return s.sid"""
                              .format("'"+user_type_cid+"'"))
        result1 = result1.values()
        if result1:
            for row in result1:
                result_list1.append(row[0])
            while True:
                print('currently',user_type_cid,'has seat', result_list1)
                print('If you delete the node, relationship(owned) also removed.')
                print('Do you want to remove', user_type_cid ,'node? (y/n)')
                remove_cluster_node = input()
                if remove_cluster_node =='y':
                    session.run("match (s:seat)-[r:BELONGSTO]->(c:cluster) where c.cid ={} delete r,c".format("'"+user_type_cid+"'"))
                    print('remove done')
                    break
                elif remove_cluster_node == 'n':
                    print('okay', user_type_cid, 'is not removed')
                    break
                else:
                    print('please type (y) or (n)')
                    continue


        else:
            while True:
                print('currently', user_type_cid, 'has no seat')
                print('do you want to remove', user_type_cid, 'cluster node? (y/n)')
                remove_cluster_node = input()
                if remove_cluster_node == 'y':
                    session.run("match (c:cluster) where c.cid = {} delete (c)".format("'" + user_type_cid + "'"))
                    print('remove done')
                    break
                elif remove_cluster_node == 'n':
                    print('okay', user_type_cid, 'is not removed')
                    break
                else:
                    print('please type (y) or (n)')
                    continue


elif user_answer =='q':
    print('good bye')

else:
    print('please type (1) or (2) or (3)')