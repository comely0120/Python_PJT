# 2_1. 다중 상속 형식
class X:
    def x(self):
        print("X")

class Y:
    def y(self):
        print("y")

class Z:
    def z(self):
        print("z")

class A(X,Y):
    def a(self):
        print("A")

class B(Y,Z):
    def b(self):
        print("B")

class M(B,A):
    pass

model1 = A()
model1.x()
model1.y()
model1.a()

model2 = M()
model2.a()
model2.x()
model2.z()
print(M.mro()) 

# 2_2. 다중 상속 문제점
class X1:
    def x(self):
        print("X")
    def xy(self):
        print("xy_x")

class Y1:
    def y(self):
        print("y")
    def xy(self):
        print("xy_y")

class A1(X1,Y1):
    pass

# 만약, 상속받는 2개의 super클래스에 같은 이름의 메소드가 있으면
# 호출할때 우선수위가 높은 메소드 1개만 실행
# class A1(X1,Y1)에서는 X1을 먼저 호출했기 때문에 xy()메소드를 실행하면
# x1의 xy()만 실행된다
model1 = A1()
model1.xy() 

# 2_3. 다중 상속 활용
class CalMultiply():
    def multiply(self):
        return self.v1*self.v2

class CalDivide():
    def divide(self):
        return self.v1/self.v2

class Cal(CalMultiply, CalDivide):
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1

c = Cal(100, 10)
print(c.add())
print(c.multiply())
print(c.divide())