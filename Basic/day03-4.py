# 집합 (sets) 순서x, 중복 x
a = set()
b = set([1,2,3,4])
c = set([1,3,4,5,6,3])

print(c)

t = tuple(c)
print(t)
l = list(c)
print(c)

# 집합 함수
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합 intersection, &
print(s1.intersection(s2))
print(s1 & s2)

# 합집합 union, |
print(s1 | s2)
print(s1.union(s2) )

# 차집합 difference, -
print(s1 - s2)
print(s1.difference(s2) )

# 추가add, 제거remove
s3 = set([7,8,9,10])
s3.add('A')
print(s3)

s3.remove(8)
print(s3)
