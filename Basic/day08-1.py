# 파이썬 클래스 상세 이해
# 클래스 상속, 다중 상속

# 1. 상속 기본
# 슈퍼 클래스(부모) 및 서브클래스(자식) => 모든 속성, 메소드 사용가능
# 장점 : 코드 재사용, 중복되는 코드 최소화, 복잡한 코드를 -> 간단하게
# 서브클래스가 슈퍼클래스 사용하는 방법 => class 서브클래스명(슈퍼클래스명)

class Car :
    '''Parent Class'''
    # 초기화 함수
    def __init__(self,tp,color):
        self.type = tp
        self.color = color

    # 출력 함수
    def show(self):
        return 'Car Class "Show Method!"'


class BmwCar(Car) :
    '''Sub Calss'''
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color) #super() => 슈퍼클래스, inint을 호출하여 부모에게 tp,color를 넘겨준다
        self.car_name = car_name

    def show_model(self) -> None : # 저번 시간에 공부한 힌트!!! return값이 없음을 알려주자!
        return "Your Car Name : %s" % self.car_name



class Benz(Car) :
    '''Sub Calss'''
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)
        self.car_name = car_name

    def show_model(self) -> None : # 저번 시간에 공부한 힌트!!! return값이 없음을 알려주자!
        return "Your Car Name : %s" % self.car_name
            
    # show이름을 가진 함수는 super클래스에 이미 있음
    def show(self):
        return '(Overridng!)Car Info: %s %s %s' %(self.car_name,self.type, self.color) 


# Sub클래스 BmwCar 사용
model1 =  BmwCar('520d','sedan','red')
# super,sub 변수 모두 사용 가능
print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # Sub
# super,sub 메소드 모두 사용 가능
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__)


# Method Overriding(오버라이딩) :  super에 이미 정의된 메소드를 sub가 이름은 같고 기능은 다르게 재정의 하는 것!
# Sub클래스 Benz 사용
model2 = Benz('220d','suv','black')
print(model2.show()) # super, sub 둘다 show()메소드를 가지고있음 => 실행은 sub의 show가 실행됨

    
# ❤❤ Super Method Call, 오버라이딩하고 부모것도 호출하고 싶은뎅??? ❤❤ 
class Benz_2(Car) : 
    '''Sub Calss'''
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)
        self.car_name = car_name

    def show_model(self) -> None : 
        return "Your Car Name : %s" % self.car_name
            
    def show(self):
        print(super().show()) # ❤❤ 오바리이딩 한 함수에 부모거 호출하면 됨!!!!!!!!!
        return '(Overridng!)Car Info: %s %s %s' %(self.car_name,self.type, self.color) 


model3 = Benz_2('350s','sedan','silver')
print(model3.show())

# Interitance Info, 상속 관계를 보여준다, 오른쪽으로 갈수록 super 클래스
print(Benz_2.mro())