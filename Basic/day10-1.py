# 파일 읽기, 쓰기

# 읽기 모드 r, 쓰기 모드(기존 파일 삭제) w, 추가 모드(파일 생성 또는 추가) a
# 상대 경로('../', './'), 절대 경로 확인('C:\...')
# 기타 : https://docs.python.org/3.7/library/functions.html#open


print("1 ===================================================")
#1-1. 파일읽기 open(파일경로,'r') + read
f = open('./resource/review.txt','r')
content = f.read()
print(content)
#반드시 close 리소스 반환 필요~!!!!!!!
f.close()

print("\n\n 2 ===================================================")
# 1-2. 파일읽기 with open(파일경로,'r') as f: 
    # close가 필요없다!
with open('./resource/review.txt','r') as f:
    c=f.read()
    print(c)
    print(list(c))
    print(iter(c))

print("\n\n 3 ===================================================")
# 1-3. 파일읽기 for문 사용
with open('./resource/review.txt','r') as f:
    for c in f: 
        print(c.strip()) #줄바꿈과 양쪽 공백 제거

print("\n\n 4 ===================================================")
# 1-4. 파일읽기
with open('./resource/review.txt','r') as f:
    content = f.read()
    print(">",content)
    # 마지막 커서가 끝으로 가기 때문에 재읽기가 불가능!!!
    # 내용이 없는 것!
    content = f.read()
    print(">",content)


print("\n\n 5 ===================================================")
# 1-5. 파일읽기 => 한줄씩 읽어오기 readline
with open('./resource/review.txt','r') as f:
    line = f.readline()
    # print(line)
    # 전체 읽어오려면 while문 돌리자!
    while line:
        print(line, end='라인바꿈->')
        line = f.readline()



print("\n\n 6 ===================================================")
# 1-6. 파일읽기=> lines는 전체 내용 읽어옴 
 # 단, \n 줄바꿈을 기준으로 분리하여 list형태로 읽어온다
with open('./resource/review.txt','r') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line, end='라인바꿈->')


print("\n\n 7 ===================================================")

score = []
with open('./resource/score.txt','r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('AVERAGE: {:6.3}' .format(sum(score)/len(score)))


