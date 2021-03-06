# day01-1
# Print 구문의 이해

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""

# 기본 출력
print('hello Pyhon!')
print("hello Python!")
print("""hello Python!""")
print('''hello Python!''')

# Seperator 옵션 사용 
print('T', 'E', 'S', 'T') # 문자 하나당 공백 하나 T E S T
print('T', 'E', 'S', 'T', sep='') # 각각을 연결해서 출력
print('2020','01','20', sep='-') # 각각을 -로 연결해서 출력 2020-01-20

# end 옵션 사용 => 줄바꿈 없이 문장 연결
print('Welcome to', end=' ')
print('heyon\'s', end=' ')
print('python study notes')

# format 사용
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print('{var1} are {var2}'.format(var1='I am', var2='corinee'))

# %d : 정수,  %f : 실수,  %s : 문자
print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price:{1: 4.3f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))

