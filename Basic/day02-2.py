""" 파이썬 데이터 타입 종류
1.Boolean : 1 TRUE, 0 FALSE
2.Numbers
3.String : 문자열(시퀀스)
4.Bytes
5.Lists : 리스트(시퀀스) ❤❤
6.Tuples : 
7.Sets : 집합
8.Dictionaries : 사전 ❤❤
9.Tuple : 튜플(시퀀스)
"""

dict1 = {
    "name" : "Comely",
    "age" : 23
} 
list1 = [1,2,3,4]
set1 = {5,6,7}
print(type(dict1))


i1= 5
f1=31.123456789
result1 = i1 + f1
result2 = i1 * f1
result3 = i1 ** f1
print(result1,type(result1)) # float
print(result2,type(result2)) # float
print(result3,type(result3)) # float

# 형변환 int, float, complex(복소수)
print(int(result1))
print(complex(3)) # (3+0j)
print(complex(0)) # 0j
print(int('3')) # 3

# divmod : 몫은 n, 나머지는 m
n,m = divmod(100,8)
print(n,m)

# math.ceil : 현재 숫자보다 크면서 가장 작은 정수
# math.ceil : 현재 숫자보다 작으면서 가장 큰 정수
import math
print(math.ceil(5.1)) #6
print(math.floor(5.1)) #5


# 그 밖에 함수는 아래 URL 보고 계속 공부하자!!
# https://docs.python.org/3/library/math.html
