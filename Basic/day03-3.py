# 딕셔너리 : 순서,중복 x, 수정,삭제 O
# 딕셔너리에는 다양한 자료형이 들어갈수있음
# key,value(json) -> MongoDB


# 선언
a = {'name':'Kim','Phone':'010-**23-****','birth':'791230'}
b = {0:'hello python',1:'hello coding'}
c = {'arr':[1,2,3,4,5]}

# 출력
print(a['name'])
    # get을 사용하면 안전하게 가져올수있다.
    # get('딕셔너리에 없는 KEY값') => 출력을 NONE으로 함으로써
    # 해당 값이 없음을 알려줌. ERROR X
print(a.get('name'))
print(a.get('address')) # 출력
print(c['arr'][:])
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1,2,3] #리스트 
a['rank2'] = (1,2,3) #튜플
print(a)

# key, value, items(=key+value)
print(a.keys())
#print(a.keys(1)) 이렇게 가져올 수 없음. 리스트로 형변환 필요
print(list(a.keys()))
temp = list(a.keys())
print(temp[1:3])

print(a.values())
temp2 = list(a.values())
print(temp2)
print("======items======")
print(a.items())
# 결과 
#dict_items([('name', 'Kim'), ('Phone', '010-**23-****'), ('birth', '791230'), ('address', 'Seoul'), ('rank', [1, 2, 3]), ('rank2', (1, 2, 3))])
print("=====list(딕셔너리.items())는 리스트 안에 튜플로====")
print(list(a.items()))
#결과
#'name', 'Kim'), ('Phone', '010-**23-****'), ('birth', '791230'), ('address', 'Seoul'), ('rank', [1, 2, 3]), ('rank2', (1, 2, 3))]


