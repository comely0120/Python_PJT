# 반복문 실습

# 기본 반복문 사용(while, for)
v1 = 1

while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10):
    # 0~9까지
    print("v2 is :", v2)

for v3 in range(1, 11):
    # 0부터 10
    print("v3 is :", v3)

for v4 in range(1, 11, 2):
    # 1,3,5,7,9
    print("v4 is :", v4)

# 1 ~ 100합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 합 : ', sum1)
print('1 ~ 100 합 : ', sum(range(1, 101)))  # sum(리스트)
print('1 ~ 100 안에 3의 배수의 합 : ', sum(range(1, 101, 3)))

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1 리스트
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

for name in names:
    print("You are", name)

# 예제2 리스트
lotto_numbers = [11, 19, 21, 28, 36, 37]

for number in lotto_numbers:
    print("Your number", number)

# 예제3 문자열
word = 'dreams'

for s in word:
    print('word : ', s)

# 예제4 딕셔너리
my_info = {
    "name": "Kim",
    "age": 33,
    "city": "Seoul"
}
 #딕셔너리의 key값으로 돌리기
for key in my_info:
    print(key, ":", my_info[key])

  #딕셔너리의 value값으로 돌리기
for val in my_info.values():
    print(val)

# 예제5 문자열
name = 'coMEly'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# break_1
for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : ", num)
# break_2
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33: 
        print("found : 33!")
        break
    else:
        print("not found : ", num)
else:
    print("Not Found 39...")

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue

    print("type:", type(v))
    print("multiply by 2:", v * 3)



# flag 사용
f = True
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

while f:
    for v in numbers:
        if v == 33:
            print("found : 33!")
            f = False
        print("not found : ", v)



# else 구문 정리(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
# 예제1

i = 1 #while 안의 if문
#i = 20 , while조건을 만족하지 않으므로 else로 감
while i <= 10:
    print('i : ', i)
    if i == 10:
        break
    i += 1
else:
    print('else block run!')

# 예제2
j = 1
while j <= 10:
    print('j : ', j)
    if j == 11:
        break
    j += 1
else:
    print('else block run!')

# 중첩 for 문 구구단 출력

for i in range(1, 11):
    print("======={:4d}단======".format(i))
    for j in range(1, 11):
        print('{:4d} * {:4d} = {:4d}'.format(i,j,i * j))
    print()

# 자료 구조 변환 예제
name = 'Niceman'
print('reversed : ', reversed(name))
print('list : ', list(reversed(name)))
print('list : ', tuple(reversed(name)))
print('list : ', set(reversed(name)))  # 순서X
