# 복습_제어문

# 1 ~ 5 문제 if 구문 사용

# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
    # 방법 1
if q1['가을']: print( q1['가을'])
    # 방법 2
print(''.join(q1[s] for s in q1 if s == '가을'))
    # 방법 3
for k,v in q1.items():
    if k == '가을':
        print(v)


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
    # 방법 1
if "사과" in q2.values(): print("포함됨")
    # 방법 2
for k,v  in q1.items():
    if v == '사과':
        print(k,v)
        break
    else:
        print("없음")
    # 방법 3
print(' '.join(k +"에는 "+ v for k,v in q2.items() if v == '사과'))


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = -10
grade = ''

if score > 100 or score <0:
    grade = '점수 이상 있음'
elif score> 80 : grade = 'A'
elif score> 60 : grade = 'B'
elif score> 40 : grade = 'C'
elif score> 20 : grade = 'D'
else : grade = 'E'
print(grade)

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a = 12
b = 6
c = 18
best = 0

best = a
if b > a:
    best = b
if c > b:
    best = c

print(best)

# 4-1. 입력을 받아서 가장 큰수를 출력 해보기
'''
a = list(map(int,input().split()))
print(a)
j=0
for i in a:
    if i > j :
        j = i
    else:
        pass
print(j)
'''
# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
q5 = '891022-3473837'
if int(q5[q5.index('-')+1])%2 == 1:
    print( q5[q5.index('-')+1])
    print("남자")
else:
    print('여자')

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "정" , "을", "병"]
    # 방법 1
for i in q3:
    if i == '정': continue
    else : print(i,end='')
    # 방법 2
print(''.join([s for s in q3 if s != '정']))

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
print(' & '.join([str(s) for s in range(1,101) if int(s)%2 == 1]))

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
print(' & '.join([s for s in  q4 if len(s)>=5]))

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
    # 방법 1
print([s for s in q5 if s.islower()])
    # 방법 2
for i in q5:
    if i.isupper(): continue
    else : print(i,end=' & ')

print('\n')
# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for i in q6:
    if i.isupper():
        i = i.lower()
        print(i,end=' ')
    else:
        i = i.upper()
        print(i,end=' ')
