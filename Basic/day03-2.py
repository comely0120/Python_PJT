# 튜플
# 순서, 중복 가능/ 수정,삭제 불가능

#선언
a = ()
b = (1,)
c = (1,2,3,4)
d = (10,100,('a','b','c','d','e'))

# 인덱싱, 슬라이싱
print(c[2])
print(c[3])
print(d[2][0])
print(d[2][1:4])
print(d[2:])

# 튜플 함수
z = (5,2,1,3,4)
print(z)
print(3 in z)
print('a' in z)
    # 튜플.index
print(z.index(2))
    # 튜플.count
print(z.count(7))

del z
print(z)