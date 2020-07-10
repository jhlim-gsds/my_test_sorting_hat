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

neo4j import 폴더에 usertable.csv, clustertable.csv, seattable.csv 넣기

dbconstraint.py 실행으로 constraint 설정

### register

usertable.csv, clutsertable.csv, seattable.csv 파일로부터 데이터를 읽어서 입력을 하고 싶은 경우

mytest.py 실행

commanline을 통해 입력을 하고 싶은 경우

register.py 실행



### search   

각 테이블에서 정보를 읽음.

search.py 실행
### update_info
update_seat_owner.py

### assign_seat
