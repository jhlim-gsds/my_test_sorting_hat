from neo4j import GraphDatabase
import random
host = 'bolt://localhost:7687'
user = 'neo4j'
password = 'letmein'
driver = GraphDatabase.driver(host,auth=(user, password))


with driver.session() as session:
    result11_list= []
    result11_list1 = []
    result11 = session.run("""match (n:user)-[r:owned]-(s:seat) return n.pid,s.sid""")
    result11 = result11.values()
    for row in result11:
        result11_list.append(row)
        result11_list1.append(row[0])
print('pid, sid: ',result11_list)

seat_pool1= []
with driver.session() as session:
    seat_result= session.run("""match (s:seat) return s.sid""")
    seat_result = seat_result.values()
    for row in seat_result:
        seat_pool1.append(row[0])
while True:
    print("how do you want to reassign seat? random(1), manual(2). If you just want to remove relationship type (3)")

    mmmm = input()
    if mmmm =='1':
        while True:
            print('who do you want to reassign seat? please type pid','if  you want to quit type q')
            with driver.session() as session:
                result11_list= []
                result11_list1 = []
                result11 = session.run("""match (n:user)-[r:owned]-(s:seat) return n.pid,s.sid""")
                result11 = result11.values()
                for row in result11:
                    result11_list.append(row)
                    result11_list1.append(row[0])
                seat_pool2 = []
                seat_result2 = session.run("""match (u:user)-[r:owned]-(s:seat) return s.sid""")
                seat_result2 = seat_result2.values()
                # print(seat_result2)
                for row in seat_result2:
                    seat_pool2.append(row[0])
                seat_pool = set(seat_pool1) - set(seat_pool2)
                seat_pool = list(seat_pool)
                selected_seat = random.choice(seat_pool)
            a = input()
            if a =='q':
                break
            if a not in result11_list1:
                print('please check pid')
                continue
            with driver.session() as session:
                session.run("""match (u:user)-[r:owned]-(s:seat) where u.pid ={} delete r""".format("'"+a+"'"))
                session.run("""match (s:seat),(u:user) where u.pid={a} and s.sid={selected_seat} merge (u)-[r:owned]-(s)"""
                            .format(a="'" + a + "'", selected_seat="'" + selected_seat + "'"))
                print(a, ' assigned to seat', selected_seat)
    elif mmmm =='2':
        while True:
            print('who do you want to reassign seat? please type pid', 'if  you want to quit type q')
            with driver.session() as session:
                result11_list= []
                result11_list1 = []
                result11 = session.run("""match (n:user)-[r:owned]-(s:seat) return n.pid,s.sid""")
                result11 = result11.values()
                for row in result11:
                    result11_list.append(row)
                    result11_list1.append(row[0])
                seat_pool2 = []
                seat_result2 = session.run("""match (u:user)-[r:owned]-(s:seat) return s.sid""")
                seat_result2 = seat_result2.values()
                # print(seat_result2)
                for row in seat_result2:
                    seat_pool2.append(row[0])
                seat_pool = set(seat_pool1) - set(seat_pool2)
                seat_pool = list(seat_pool)
                #selected_seat = random.choice(seat_pool)
            a = input()
            if a =='q':
                break
            if a not in result11_list1:
                print('please check pid')
                continue
            while True:
                print('empty seat: ',seat_pool)
                print('please type cid for seat.','If you want to quit type q')
                print('If you type -1 then just delete relationship')
                user_manual_seat = input()
                if user_manual_seat=='q':
                    break
                elif user_manual_seat =='-1':
                    with driver.session() as session:
                        session.run("""match (u:user)-[r:owned]-(s:seat) where u.pid ={} delete r""".format("'" + a + "'"))
                        print('delete complete')
                        break
                if user_manual_seat not in seat_pool:
                    print('please check sid', ' sid must be in above list')
                    continue
                with driver.session() as session:
                    session.run("""match (u:user)-[r:owned]-(s:seat) where u.pid ={} delete r""".format("'"+a+"'"))
                    session.run("""match (s:seat),(u:user) where u.pid={a} and s.sid={user_manual_seat} merge (u)-[r:owned]-(s)"""
                                .format(a="'" + a + "'", user_manual_seat="'" + user_manual_seat + "'"))
                    print(a, ' assigned to seat', user_manual_seat)
                    break

    elif mmmm=='3':
        print('how do you want to delete relationship? all the student ownership(1) or individual(2)')
        how_delete_relation = input()
        if how_delete_relation =='1':
            with driver.session() as session:
                session.run("""match (u:user)-[r:owned]-(s:seat) delete r""")
                print('delete complete')

        elif how_delete_relation =='2':
            while True:
                print('who do you want to delete seat? please type pid', 'if  you want to quit type q')
                with driver.session() as session:
                    result11_list = []
                    result11_list1 = []
                    result11 = session.run("""match (n:user)-[r:owned]-(s:seat) return n.pid,s.sid""")
                    result11 = result11.values()
                    for row in result11:
                        result11_list.append(row)
                        result11_list1.append(row[0])
                    seat_pool2 = []
                    seat_result2 = session.run("""match (u:user)-[r:owned]-(s:seat) return s.sid""")
                    seat_result2 = seat_result2.values()
                    # print(seat_result2)
                    for row in seat_result2:
                        seat_pool2.append(row[0])
                    seat_pool = set(seat_pool1) - set(seat_pool2)
                    seat_pool = list(seat_pool)
                    # selected_seat = random.choice(seat_pool)
                a = input()
                if a == 'q':
                    break
                if a not in result11_list1:
                    print('please check pid')
                    continue
                with driver.session() as session:
                    session.run("""match (u:user)-[r:owned]-(s:seat) where u.pid ={} delete r""".format("'" + a + "'"))
                    print('delete done')
        else:
            print('please type (1) or (2)')


    else:
        print('please type (1) or (2)')

    print('do you want to quit? (y/n)')
    quit_answer = input()
    if quit_answer =='y':
        print('goodbye')
        break
    else:
        continue