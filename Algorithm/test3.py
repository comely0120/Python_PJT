''' 문제
두 문자열 A와 B가 있을 때, 두 문자열의 '최대공약문자열' C를 아래와 같이 정의하자.

1. 문자열 C를 반복하여 문자열 A와 B를 생성할 수 있다.
1. 가능한 C 중에 가장 긴 문자열을 C로 한다.
1. 위 조건을 만족하는 C가 없으면 빈 문자열을 C로 한다.

이 때, 문자열 A와 B를 입력받아 C를 출력하는 프로그램을 작성하시오.

예시입력1
A = 'ababcde'
B = 'ababcde'
출력: 'ababcde'

예시입력2
A = 'ababababab'
B = 'abab'
출력: 'ab'

예시입력3
A = 'abababab'
B = 'abab'
출력: 'abab'

예시입력4

A = 'fast'
B = 'campus'
출력: ''
'''

# 풀이

def gcdString(A,B):
    def isDivisor(string,isDivisor):
        n = len(divisor)
        if len(string)% n !=0:
            return False

        while string != '':
            # A문자열에서 처음부터 B문자열 길이까지의 문자가 일치 하지 않다면
            # 처음부터 A와 B는 일치하지 않기에 False
            # A : abcabc B:abd
            if string[:n] != divisor:
                return False

            string = string[n:]
        return True

    if len(A) > len(B):
        str1,str2 = A,B
    else:
        str1,str2 = B,A
    divisor =str2
    m =1
    while divisor != '':
        if isDivisor(str2,divisor) and isDivisor(str1,divisor):
            return divisor
        m +=1
        divisor = str2[:len(str2)//m]
    return ''

A = 'ababcde'
B = 'ababcde'
print(gcdString(A, B))
 
A = 'ababababab'
B = 'abab'
print(gcdString(A, B))
 
A = 'abababab'
B = 'abab'
print(gcdString(A, B))
 
A = 'fast'
B = 'campus'
print(gcdString(A, B))  


        