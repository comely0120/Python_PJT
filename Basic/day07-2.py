# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

#클래스 선언 : class 클래스명 : 함수

# 예제1
class UserInfo:
    def __init__(self, name): #__init__ : 초기화
        self.name = name

    def print_info(self):
        print("Name: " + self.name)

    def __del__(self):
        print("Instance removed!")


user1 = UserInfo("Kim")
user2 = UserInfo("Park")

print(id(user1))
print(id(user2))

user1.print_info()
user2.print_info()

print('user1 : ', user1.__dict__)  # 클래스 네임스페이스 확인
print('user2 : ', user2.__dict__)

print(user1.name)


# 예제2
# self의 이해

class SelfTest:
    # 클래스 매소드
    def function1():
        print("function1 called!")

    # 인스턴스 매소드
    def function2(self):
        print(id(self))
        print("function2 called!")


f = SelfTest() # 인스턴스 생성
print(id(f))

# f.function1() #예외 발생
print(SelfTest.function1()) # 클래스 매소드는 => 클래스명.클래스 매소드로 호출

f.function2() # 인스턴스 매소드는 인스턴스명.클래스안의 매소드명
# print(SelfTest.function2()) #예외 발생
print(SelfTest.function2(SelfTest)) 


# 예제3
# 클래스 변수 , 인스턴스 변수

class Warehouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1 #클래스 명.클래스변수 => 클래스 변수는 직접 접근

    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('Kim') # 인스턴스 명 user1, 인스턴스 변수 name = 'kim'
user2 = Warehouse('Park') # 인스턴스 명 user2

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)

print(Warehouse.__dict__)  # 클래스 네임스페이스 , 클래스 변수 (공유)
# 위에 결과
#{'__module__': '__main__', 'stock_num': 2, '__init__': <function Warehouse.__init__ at 0x032DA190>, '__del__': <function Warehouse.__del__ at 0x032DA148>, '__dict__': <attribute '__dict__' of 'Warehouse' objects>, '__weakref__': <attribute '__weakref__' of 'Warehouse' objects>, '__doc__': None}
# 'stock_num': 2라고  되어있음!!!!!!!!!
# 'stock_num'는 클래스 변수이므로 user1,user2가 공유하기 때문에 user1에서 1증가=>stock_num =1이되고 다시 user2로 인해 stockd_num=2가 되는 것
# Warehouse.stock_num = 50 # 직접 접근 가능
print("\n\n===클래스 변수 stock_num은 클래스Warehouse와 인스턴스 user1,user2가 공유===")
print(" \t\t 즉, 3개의 stock_num값이 동일")
print(user1.stock_num)
print(user2.stock_num)
print(Warehouse.stock_num)


del user1

print(user2.stock_num)