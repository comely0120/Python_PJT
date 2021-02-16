# 객체 참조 다양한 특징들

# 1.  id vs __eq__(==) 증명
x = {'01':'1','002':'22','03':333}
y = x       # 얕은 복사! -> id가 같음

print('EX1 : ', id(x),id(y))    # id 확인
print('EX2 : ', x == y)         # 값이 동일한지
print('Ex3 : ', x is y)         # id가 같은지(같은 객체를 보고있는지)

x['04'] = 4444
print('Ex4 : ', x is y)        # 얕은 복사 특징!! -> x를 변화시키면 같은 id를 가진 y도 똑같이 변한다

z = {'01':'1','002':'22','03':333,'04':4444}
print('Ex5 : ', x is z)        # FALSE!! 딕셔너리 값이 동일하다해도 x와 z는 id 값이 다르다!
print('Ex6 : ', x == z)        # 값은 동일하기 때문에 TRUE


# 2. 튜플은 immutable! 불변!!! => 튜틀은 특이하게도 값이 같으면 id가 같다!
tuple1=(1,3,5,('IS','ODD'))
tuple2=(2,4,6,('IS','EVEN'))
tuple3=(1,3,5,('IS','ODD'))

print('EX2-1',id(tuple1),id(tuple2))
print('EX2-2',id(tuple1),id(tuple3))
print('EX2-3',tuple1 is tuple3)
print('EX2-4',tuple1==tuple3)
print('EX2-5',tuple1.__eq__(tuple3))

# 3. Copy, Deep copy
# Copy
tl1= [10,[100,200],(5,10,15)]
tl2 = tl1
tl3 =  list(tl1)
tl4 = [10,[100,200],(5,10,15)]
print(tl3)
print('EX3-1', tl1==tl2)    #  T
print('EX3-2', tl1 is tl2)  #  T
print('EX3-3', tl1 == tl3)  #  T
print('EX3-4', tl1 is tl3)  #  F
print('EX3-5', tl1 is tl4)  #  F

print('전',id(tl1[1]))
tl1[1] += [100,120]
print('후',id(tl1[1]))
print("❤❤ 리스트는 mutable => 값이 변할 수 있음 => 값을 변화시켜도 id유지 ❤❤\n") 

print('전',id(tl1[2]))
tl1[2] += (110,120)
print('후',id(tl1[2]))
print("❤❤ 튜플은  immutable => 값이 변할 수 없음=> id를 재할당 한다 ❤❤ \n") 


print('EX3-6', tl1)
print('EX3-7', tl2) 
print('EX3-8', tl3)

# Deep Copy
# 장바구니
class Basket:
    def __init__(self,products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self,prod_name):
        self._products.append(prod_name)

    def del_prod(self,prod_name):
        self._products.remove(prod_name)

import copy

basket1 = Basket(['Apple','Banana','Milk','Chocolate','Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('EX4-1 : ', id(basket1),id(basket2),id(basket3))
print('EX4-2 : ', id(basket1._products),id(basket2._products),id(basket3._products))
# 인스턴스 basket1,basket2,basket3 모두 다른 id 값을 가짐
# BUT!!! 일반 copy한 basket1의 ._products 와 basket2의 ._products 는 같은 id값을 가짐
# 즉, 얕은(일반)복사를 하게되면 뜻하지 않게 다른 인스턴스들이 각각 가진 인스턴스 변수를 모두 바꾸게될 수 가 있음
# 경우에 따라 얕은 복사, 깊은 복사 잘 사용하기!

basket1.put_prod('Snack')
basket2.del_prod('Chocolate')

print('EX4-3 : ',basket1._products)
print('EX4-4 : ',basket2._products)
print(' #### 이렇게 basket1과 basket2에게 모두 적용되는 오류 발생 ####')
print('EX4-5 : ',basket3._products)

        


# 4. 매개 변수 전달 주의할 점들!
def mul(x,y):
    x += y
    return x

x = 10
y = 5
print('EX5-1 : ',mul(x,y),x,y) # x 값이 변하지 않고 10을 유지

a = [10,100]
b = [20,200] 
print('EX5-2 : ',mul(a,b),a,b)  # a 값이 mul(a,b)의 결과와 같은 값으로 변함 -> mutable 원본이 수정된다...!


A = (10,100)
B = (20,200) 
print('EX5-3 : ',mul(A,B),A,B) 


# 5. 파이썬(+자바) 불변형 예외
# str, bytes, frozenset, tuple : 사본 생성 -> 참조 반환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('EX7-1 -', tt1 is tt2, id(tt1), id(tt2))
print('EX7-2 -', tt3 is tt1, id(tt3), id(tt1))

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('EX7-3 -', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('EX7-4 -', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))