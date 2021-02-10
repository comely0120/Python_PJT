# 예외처리

# 1. 예외의 종류 
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외처리 중요

# SyntaxError : 잘못된 문법
# NameEroor : 참조변수 없음
# ZeroDivisionError :  0 나누기 에러
# IndexError : 인덱스 범위 오버

# keyError
dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}
# print(dic['hobby'])     # 키가 존재하지 않으면 예외
# 안전하게 코딩하기 위해 get을 사용하자!!!
print(dic.get('hobby')) 

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
# print(time.time())
# print(time.month()) # 예외 발생


# ValueError : 참조 값이 없을 때 예외
x = [1, 5, 9]
# x.remove(5)
# print(x)
# x.remove(100)
# print(x) # 예외 발생


# FileNotFoundError
# f = open('test.txt') # 예외 발생


# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
x = [1, 2]
y = (1, 2)
z = 'test'
# print(x + y) # 예외 발생
# print(x + z) # 예외 발생
# print(y + z) # 예외 발생
# print(sum([1,2,3],10,1)) # 예외 발생
# print(x + list(y))
# print(x + list(z)


# 2. 예외 처리 기본
# try               에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1:    여러 개 가능(에러 처리)
# except 에러명2: 
# else:             try 블록의 에러가 없을 경우 실행
# finally:          항상 실행


# 예제1

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('ok! else!')

print()

# 예제2

try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except:  # 모든 에러를 처리(Exception)
    print('Not found it! - Occurred ValueError!')
else:
    print('ok! else!')

print()

# 예제3

try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except Exception as e:
    print(e)  # 에러 내용 출력
    # pass # 임시로 에러 해결 시 예외 처리
else:
    print('ok! else!')
finally:
    print('ok! finally!')  # 무조건 수행 됨

print()

# 예제4
# 예외처리는 하지 않지만, 무조건 수행 되는 코딩 패턴

try:
    print('try')
finally:
    print('finally')

print()

# 예제5
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Kim':
        print('Ok! pass')
    else:
        raise ValueError
except ValueError: