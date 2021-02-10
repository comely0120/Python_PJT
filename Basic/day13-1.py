# 파이썬 데이터베이스 연동(SQLite)

import datetime
import sqlite3

# 버전 확인
print('sqlite3.ver : ', sqlite3.version)
print('sqlite3.sqlite.ver : ', sqlite3.sqlite_version)

# 작업 날짜 생성
now = datetime.datetime.now()
print('지금 몇년+월+일+시+분+초 인지 알려죵!! : ',now)
# strftime을 통해 원하는 형식으로 변형 가능!!
# 월은 m/ 분은 M => 헷갈리지 말쟈!!!
time = now.strftime('%H:%M:%S')
print(time)
Day = now.strftime('%Y년 %m월 %d일')
print(Day)

# DB 생성 & Auto Comit(Rollback)
conn = sqlite3.connect("./resource/database.db", isolation_level=None)

#Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성( Data Type : Text, NUMERIC, INTEGER, REAL, BLOB)
c.execute(
   "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT,\
       email TEXT, phone TEXT, website TEXT, regdate TEXT)")
# 데이터 삽입
c.execute(
    "INSERT INTO users VALUES(1, 'OH', 'comely0120@naver.com','010-1234-5678',\
        'OH.com', ?)", (Day,)
)
c.execute(
    "INSERT INTO users(id,username,email,phone,website,regdate) \
        VALUES(?,?,?,?,?,?)" ,(2,'HU','mingdi@naver.com','010-6789-1234','Hu.com',Day)
)

# Many 삽입(튜플,리스트) executemany()
userList=(
    (3,'Kim','Kim@gmail.com','010-1212-3434','Kim.com',Day),
    (4,'Lee','Lee@gmail.com','010-5656-7878','Lee.com',Day),
    (5,'Cho','Kim@daum.com','010-5555-0000','Kim.net',Day)
)

c.executemany(
    "INSERT INTO users(id,username,email,phone,website,regdate) VALUES (?,?,?,?,?,?)",userList
)

# 테이블 데이터 삭제
#print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

# 커밋 : isolation_level=None 일 경우 자동 반영(Auto Commit)
conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
conn.close()
