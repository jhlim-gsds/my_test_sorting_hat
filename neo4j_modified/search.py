from neo4j import GraphDatabase
#wtd: incase of individual include cluster information.

host = 'bolt://localhost:7687'
user = 'neo4j'
password = 'letmein'
driver = GraphDatabase.driver(host,auth=(user, password))

print('what do you want to know? user(1), seat(2), cluster(3)')
user_answer= input()
if user_answer =='1':
    print("what do you want to know? all the student table(1) or individual(2)?" )
    user_answer1= input()
    if user_answer1 =='1':
        with driver.session() as session:
            student = session.run("""match (u:user)-[r:owned]-(s:seat) return u.pid, u.full_name, s.sid""")
            student = student.values()
            if student:
                for row in student:
                    print('pid: ',row[0],'full name: ',row[1],'has seat',row[2])
            else:
                print('all the students have no seat')
            student_noseat = session.run("""match (u:user) where not (u)-[:owned]-() return u.pid,u.full_name""")
            student_noseat = student_noseat.values()
            print('---------------------------------------')
            if not student_noseat:
                print('all the students have seat')
            else:
                for row in student_noseat:
                    print('pid: ',row[0],'full name: ',row[1], 'has no seat')



    elif user_answer1 =='2':
        with driver.session() as session:
            all_pid_list = []
            all_pid= session.run("""match (u:user) return u.pid""")
            all_pid = all_pid.values()
            for row in all_pid:
                all_pid_list.append(row[0])
            while True:
                print(all_pid_list)
                print('please type pid for user, if you want to quit type q')
                user_pid = input()
                if user_pid == 'q':
                    break
                elif user_pid in all_pid_list:
                    user_pid_list= session.run('''match (u:user)-[r:owned]-(s:seat) where u.pid= {} return u.pid, u.full_name, s.sid'''
                                               .format("'"+user_pid+"'"))
                    user_pid_list = user_pid_list.values()
                    if user_pid_list:
                        for row in user_pid_list:
                            print('pid: ', row[0], 'full name: ', row[1], 'has seat', row[2])
                    else:
                        user_pid_list1 = session.run("""match (u:user) where u.pid = {} return u.pid,u.full_name"""
                                                     .format("'"+user_pid+"'"))
                        user_pid_list1 = user_pid_list1.values()
                        for row in user_pid_list1:
                            print('pid: ', row[0], 'full name: ', row[1], 'has no seat')
                else:
                    print('please type pid in above list','if you want to quit please type q')



    else:
        print('please type (1) or (2)')

elif user_answer =='2':
    print("what do you want to know? all the seat table(1) or individual(2)?" )
    user_answer1= input()
    if user_answer1 =='1':
        with driver.session() as session:
            seat = session.run('match (u:user)-[r:owned]-(s:seat) return u.pid, u.full_name,s.sid')
            seat = seat.values()
            if seat:
                for row in seat:
                    print('seat: ',row[2], 'owned by','pid: ',row[0],'full_name: ', row[1])
            else:
                print('there all the seat are empty')
            print('-------------------------------')
            seat_1 = session.run('match (s:seat) where not ()-[:owned]-(s) return s.sid')
            seat_1 = seat_1.values()
            if seat_1:
                for row in seat_1:
                    print('sid: ',row[0],'is empty')
            else:
                print('all the seats are occupied')
    elif user_answer1 =='2':
        with driver.session() as session:
            all_sid_list = []
            all_sid= session.run("""match (s:seat) return s.sid""")
            all_sid = all_sid.values()
            for row in all_sid:
                all_sid_list.append(row[0])
            while True:
                print(all_sid_list)
                print('please type sid for seat, if you want to quit type q')
                user_sid = input()
                if user_sid == 'q':
                    break
                elif user_sid in all_sid_list:
                    user_sid_list= session.run('''match (u:user)-[r:owned]-(s:seat) where s.sid= {} return u.pid, u.full_name, s.sid'''
                                               .format("'"+user_sid+"'"))
                    user_sid_list = user_sid_list.values()
                    if user_sid_list:
                        for row in user_sid_list:
                            print('pid: ', row[0], 'full name: ', row[1], 'has seat', row[2])
                    else:
                        user_sid_list1 = session.run("""match (s:seat) where s.sid = {} return s.sid"""
                                                     .format("'"+user_sid+"'"))
                        user_sid_list1 = user_sid_list1.values()
                        for row in user_sid_list1:
                            print('sid: ', row[0], 'is empty')
                else:
                    print('please type sid in above list','if you want to quit please type q')
    else:
        print('please type (1) or (2)')

elif user_answer =='3':
    print("what do you want to know? all the cluster table(1) or individual(2)?")
    user_answer_1 = input()
    if user_answer_1 =='1':
        with driver.session() as session:
            cluster_session = session.run('match (u:user)-[r:owned]-(s:seat)-[r1:BELONGSTO]-(c:cluster) return c.cid,count(*),tointeger(c.cluster_size) - count(*)')
            cluster_session = cluster_session.values()
            if cluster_session:
                for row in cluster_session:
                    print('cid :',row[0],'has ',row[1],'seats. Currently',row[2],'available')
            else:
                print('all the clusters are available')
            print('--------------------------')
            cluster_session1 = session.run('match (c:cluster) where not ()-[:owned]-()-[:BELONGSTO]-(c) return c.cid')
            cluster_session1 = cluster_session1.values()
            if cluster_session1:
                for row in cluster_session1:
                    print(row[0],'is empty')
            else:
                pass         #굳이 처리할 필요 없는 듯.

    elif user_answer_1 =='2':
        with driver.session() as session:
            all_cid_list = []
            all_cid= session.run("""match (c:cluster) return c.cid""")
            all_cid = all_cid.values()
            for row in all_cid:
                all_cid_list.append(row[0])
            while True:
                print(all_cid_list)
                print('please type cid for cluster, if you want to quit type q')
                user_cid = input()
                if user_cid == 'q':
                    break
                elif user_cid in all_cid_list:
                    my_cid_list = session.run("match (u:user)-[r:owned]-(s:seat)-[r1:BELONGSTO]-(c:cluster) where c.cid= {} return u.pid,c.cluster_size"
                                              .format("'"+user_cid+"'"))
                    my_cid_list = my_cid_list.values()
                    my_cluster_size_list=[]
                    if my_cid_list:
                        for row in my_cid_list:
                            print('user pid:',row[0],'has seat in ',user_cid )
                            my_cluster_size_list.append(row[1])
                        my_cluster_size_list = set(my_cluster_size_list)
                        for x in my_cluster_size_list:
                            print(int(x) - len(my_cid_list),'seat left in', user_cid)


                    else:
                        mm_cid_list = session.run("match (c:cluster) where c.cid= {} return c.cluster_size".format("'"+user_cid+"'"))
                        mm_cid_list = mm_cid_list.values()
                        print('cluster size:' ,mm_cid_list)
                        print('cluster',user_cid,'is available')

                else:
                    print('please type cid in above list', 'if you want to quit please type q')
    else:
        print('please type (1) or (2)')

else:
    print("please type (1) or (2) or (3)")