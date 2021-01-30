# 리스트

#리스트 : 순서,중보,수정,삭제 모두 가능
#선언 
a=[]
b =list()
c = [1,2,3,4]
d = [10,100,'A','B']
e = [10,100,['A','B']]

# 인덱싱
print(d[3])
print(e[0])
print(e[2][0])

#슬라이싱
print(d[0:3])
print(e[2][:])

#연산
print(c+d)
print(c*3)

# 리스트 수정,삭제
c[0] = 77
print(c)
c[1]=['a','b','c']
print(c)

del(c[1])
print(c)

# 리스트 함수
y = [5,2,3,1,4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
 # insert와 append의 차이!!
 # insert(원하는 index,넣을 값)=> 원하는 위치에 값을 추가
 # append(넣을 값) => 끝에다가 값 추가
y.insert(2,7)
print(y)
 # remove와 del의 차이!!
 # remove(삭제할 값) => 값을 찾아서 삭제
 # del(리스트[인데스]) => 인덱스를 찾아서 삭제
y.remove(7)
print(y)
 #pop 맨 마지막을 지움
y.pop()
print(y)
 # append와 extend 차이!!
ex =[88,77]
y.extend(ex)
print(y)
y.append(ex)
print(y)


temp = [1,2,3,6,4,5,6,6,6]

print(temp.pop())
print(temp)
