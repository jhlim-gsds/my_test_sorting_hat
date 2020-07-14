# Sorting-hat: a seat assigning randomly considering social distance

there are 4 interfaces to deal with seat-assignment information.   
Please refer some websites about sqlite and python.
Start from here [https://www.sqlitetutorial.net/sqlite-sample-database/]

## Environment
- python 3.6 (recommended)
- sqlite3 (default included python)
- linux ubuntu 18.04 (please update your test log)

## Usage

pip install neo4j  를 통해 neo4j python driver 설치

neo4j에서 localgraph를 만들 때에 password를 letmein으로 설정

neo4j import 폴더에 usertable.csv, clustertable.csv, seattable.csv , cluster1.csv 넣기

dbconstraint.py 실행으로 constraint 설정

cluster1.csv 는 cluster에서 칸막이가 없는 자리끼리 near라는 relation으로 연결해주기 위함.

### register

usertable.csv, clutsertable.csv, seattable.csv 파일로부터 데이터를 읽어서 입력을 하고 싶은 경우

mytest.py 실행

commanline을 통해 입력을 하고 싶은 경우

register.py 실행



### search   

각 테이블에서 정보를 읽음.

search.py 실행
### update_info
update_seat_owner.py  <- 이미 자리가 배정되었을 경우 재배정. 
(1번은 random하게 재배정, 2는 seat를 지정해줌, 3은 전체 ownership relation을 없애거나 pid를 적을 경우 해당하는 사람의 자리가 없어짐. (유저는 계속 존재하고 :owned라는 relation만 없앰)


seat의 cluster id가 바뀌는 예외적인 상황 (1번 cluster에서 자리를 하나 빼서 2번 cluster에 추가하는 경우)


update_seat_cluster.py

### assign_seat
assign_seat.py

자리가 없는 사람 모두에게 자리를 배정하거나 아니면 pid를 적을 경우 해당하는 사람에게 자리를 배정함.(random)
