# day02
# 기초부터 시작!

#import this  #파이썬에 대한 설명글이 좌라락
import sys 

# 파이썬 기본 인코딩, 파이썬 3.X버전부터는 utf-8이 기본 인코딩
print(sys.stdin.encoding) #utf-8
print(sys.stdout.encoding) #utf-8

# 반복문_구구단
for i in range(1,10):
    print('=== %d단===' %(i))
    for j in range(1,10):
        print('%d * %d = ' %(i,j), i*j)

# 함수 선언
def HI():
    print("(❁´◡`❁) 안녀엉~ (❁´◡`❁)")

HI()

# 클래스
class CODING:
    pass

#객체 생성
code = CODING()

print(code)
print(id(code))
print(dir(code))


# 가상환경 activate, deactivate.bat
# pip show, install, uninstall, --upgrade

#외부 페키지 simplejson 테스트
import simplejson as json
test_dict = {'1':100, '5':50, '3':70,'4':40,'2':80}
#키 값으로 정렬하고 4개의 공백출력(indent=4*' ')후  "키값":값 출력
print(json.dumps(test_dict, sort_keys=True,indent=4*' '))
