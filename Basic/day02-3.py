# 문자열, 문자열 연산, 슬라이싱

# 1. 이스케이프 문자 사용

escape_str1 = "Do you have a \"big collection\"?"
escape_str2 = 'What\'s on TV?'
escape_str3 = "What's on TV?"
escape_str4 = 'This is a "book".'

# 출력1
print(escape_str1)
print(escape_str2)
print(escape_str3)
print(escape_str4)

# 2. 탭, 줄바꿈
t_s1 = "Tab\tClick!"
t_s2 = "New Line\n Start!!"

# 출력2
print(t_s1)
print(t_s2)

# 3. Raw String ❤❤❤ 
# Escape에 영향받지 않음!!! 
# r'파일 경로' => 파일 경로 그대로 출력
raw_s1 = r'C:\Programs\python3\ '  #C:\Programs\python3\
raw_s2 = r"\\a\b\c\d"
raw_s3 = r'\'"'
raw_s4 = r"\"'"

# 출력3
print(raw_s1)
print(raw_s2)
print(raw_s3)
print(raw_s4)

# 4. MULTI 라인 ❤❤❤
multi_str1 = \
    """
    문자열
    멀티라인
    테스트
    """
# 멀티라인 출력
print(multi_str1)

multi_str2 = \
    '''
    문자열 멀티라인 
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)

# 5. 문자열 함수 ❤❤❤
# 참고 : https://www.w3schools.com/python/python_ref_string.asp
str_00 = "COMELY"
str_01 = "comely"
str_02 = "I'm sad"
str_03 = "this is string example....wow!!! this is really string"

print("ISLOWER 소문자야?: ",str_00.islower())
print("Endswith 이문자로 끝나? : ",str_00.endswith('Y'))
print("Capitalize 첫글자 대문자로 변환: ", str_01.capitalize())
print("join str: ", str_01.join(["I'm ", "!"]))
print("replace1: ", str_02.replace('sad', 'HAPPY!'))
print("replace2: (찾을문자,바꿀문자, 몇개 바꿀건지) ", str_03.replace("is", "was", 2))
print("split: ", str_03.split(' '))  # Type 확인
print("sorted: ", sorted(str_01))  # reverse=True
print("reversed1: ", reversed(str_02)) #list 형 변환 꼭 해줘야한다
print("reversed2 글자의 순서를 역순으로!: ", list(reversed(str_02))) 
print(str_02[::-1]) # -이니까 역순으로 출력 reverse와 같음

# 6. immutable 설명 : 변경 불가능!!!! 숫자, 문자열, 튜플
# mutable은 변경 가능!! 리스트, 딕셔너리, NumPy의 배열(ndarray)
x=3
print("숫자 3의 id : ",id(3))
print("x의 id : ",id(x))
y=x
print("y의 id : ",id(y))
#여기까지는 3,x,y가 모두 같은 주소
y +=3
print("y의 id : ",id(y))
#여기서 y값이 달라지기 때문에 y의 주소만 변경(x는 변하지 않음)
print(x,y) 

# 반대로 mutable은 y를 변경하면 x도 자동으로 변경된다.
x = [1,2,3]
y = x
print("x :", x, "Y : ",y)
y += [4,]
print("x :", x, "Y : ",y)


im_str = "LET\'s STUDY!"

for i in im_str:
    print(i)


# im_str[0] = "T"  # 수정 불가(immutable)
im_str2 = im_str.replace(im_str[0],"G") 
print(im_str2)


# 7. 슬라이싱(인덱싱)
# 일부분 추출(정말 중요) ❤❤❤❤❤❤❤❤❤
str_sl = 'Comely\'s STUDY Notes'

# 슬라이싱 연습
print(str_sl[0:3])
print(str_sl[:len(str_sl)])
print(str_sl[:len(str_sl) - 1])
print(str_sl[:])
print(str_sl[1:4:2])
print(str_sl[-3:6])
print(str_sl[1:-2])
print(str_sl[::-1])
print(str_sl[::2])