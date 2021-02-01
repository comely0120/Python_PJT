# 모듈, 패키지

# 패키지 => 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)
print(Fibonacci.fib_2(300))

from pkg.calculations import * 
# import *은 권장하지 않음!!! => 너무 많은 메로리 차지, 필요한 함수만 불러오자!!!

# from pkg.calculations import add,substract  => , 를 통해 여러개 한번에 가져올 수도 있음
print(add(10,20))
print(substract(10,20))
print(multiply(5,10))
print(divide(5,10))

import pkg.prints as p
p.print1()
p.print2()
