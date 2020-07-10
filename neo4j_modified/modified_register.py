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
        with driver.session() as session:
            my_result = session.run("""match (u:user) where u.pid = {} return u.pid""".format("'"+answer1+"'"))
            my_result = my_result.values()
            if my_result:
                print(answer1,'already exists')
                print('do you want to replace it? (y/n)')
                replace_answer = input()
                if replace_answer =='y':
                    session.run("""match (u:user)-[r:owned]-(s:seat) where u.pid = {} delete r""".format("'"+answer1+"'"))
                    session.run("""match (u:user) where u.pid = {} delete u""".format("'"+answer1+"'"))
                    print('delete done')
                elif replace_answer =='n':
                    break                            #or continue? design problem.
                else:
                    print("please type (y) or (n)")
            else:
                pass


        print('please type fullname for user')
        answer2 = input()
        print('{'+'pid : {answer1} , full_name: {answer2}'.format(answer1= answer1,answer2= answer2)+'}')

        with driver.session() as session:
            #session.run("""merge (u:user {hello})""".format(hello ='{'+'pid : {answer1} , full_name: {answer2}'
             #                                           .format(answer1= str(answer1),answer2="'"+answer2+"'" )+'}' ))
            session.run("""merge (u:user {hello})""".format(hello='{' + 'pid : {answer1} , full_name: {answer2}'
                                                       .format(answer1= "'"+answer1+"'",answer2="'"+answer2+"'" )+'}' ))

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
        with driver.session() as session:
            my_result = session.run("""match (c:cluster) where c.cid= {} return c.cid""".format("'"+answer1+"'"))
            my_result = my_result.values()
            if my_result:
                print(answer1, 'already exists')
                print('do you want to replace it? (y/n)')
                replace_answer = input()
                if replace_answer =='y':
                    session.run("""match (s:seat)-[r:BELONGSTO]->(c:cluster) where c.cid = {} delete r""".format("'"+answer1+"'"))
                    session.run("""match (c:cluster) where c.cid= {} delete c""".format("'"+answer1+"'"))
                    print("delete done")
                elif replace_answer =='n':
                    break
                else:
                    print('please type (y) or (n)')
            else:
                pass
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
                                                        .format(answer1= "'"+answer1+"'"),answer2="'"+answer2+"'" )+'}' )
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
        with driver.session() as session:
            my_result = session.run("""match (s:seat) where s.sid ={} return s.sid""".format("'"+answer1+"'"))
            my_result = my_result.values()
            if my_result:
                print(answer1,'already exists')
                print('do you want to replace? (y/n)')
                replace_answer = input()
                if replace_answer =='y':
                    session.run("""match (s:seat)-[r:BELONGSTO]-(c:cluster) where s.sid ={} delete r""".format("'"+answer1+"'"))
                    session.run("""match (u:user)-[r1:owned]-(s:seat) where s.sid = {} delete r1""".format("'"+answer1+"'"))
                    session.run("""match (s:seat) where s.sid= {} delete s""".format("'"+answer1+"'"))
                    print('delete done')
                elif replace_answer =='n':
                    break
                else:
                    print('please type (y) or (n)')
            else:
                pass
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
                                                        .format(answer1= "'"+answer1+"'"),answer2="'"+answer2+"'" )+'}' )
        print('insert done')
        print('do you want to quit? (y/n)')
        qq = input()
        if qq == 'y':
            break
else:
    print('please type (1),(2),(3), you can restart the program')