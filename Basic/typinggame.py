# 업그레이드 타이핑 게임 만들기!

import random, time
import winsound
import sqlite3, datetime

# DB 생성 & Auto Commit
conn = sqlite3.connect('./resource/records.db',isolation_level=None)
# Cursor 연결
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS records( id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record TEXT, regdate TEXT)"
)

words = [] # 영어 단어 리스트(1000개 로드)

n=1              #게임 시도 횟수
cor_cnt=0        # 정답 개수

with open("./resource/word.txt",'r') as f:
    for c in f:
        words.append(c.strip())
#print(words)  # 단어 리스트 확인

input("R U READY?? PRESS ENTER KEY!") 

start = time.time() # 게임 시작 시간




while n <= 7 :
    random.shuffle(words)
    q = random.choice(words)

    print()

    print("**QUESTION** {}번".format(n))
    print(q)    # 문제 출력

    x =  input(">>>")    # 타이핑 입력
    print()
    if str(q).strip() == str(x).strip(): # 공백을 제거한 후 입력을 확인
        print("GOOD!!(●'◡'●)")
        # 정답 소리 재생
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        cor_cnt += 1
    else:
        print("WRONG....ಥ_ಥ")
                # 정답 소리 재생
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)  
    
    n += 1      # 다음 문제 출력

end = time.time() # 게임 끝난 시간
et = end - start # 총 게임 시간
et = format(et,".3f") # 총 게임 시간을 소수 셋째 자리까지 표현

if cor_cnt >=5:
    print("❤❤ 합 격 ❤❤")
else:
    print("✖✖ 불 합 격 ✖✖")

# 기록 DB 삽입
cursor.execute("INSERT INTO records('cor_cnt','record','regdate') VALUES (?,?,?)",\
    (cor_cnt,et,datetime.datetime.now().strftime('%Y-%m-%d & %H:%M:%S'), )
    )

# 총 게임 시간 출력
print("게임 시간 : ", et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작 지점 (main에서만 실행 가능)
if __name__ == '__main__':
    pass
