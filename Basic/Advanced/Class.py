# 객체 지향 프로그래밍 OOP -> 코드의 재사용, 코드 중복 방지..등등


# 1. 일반적 코딩 => 하나씩 입력...힘들엉...
# 학생 1
student_name1 = "kim"
student_num1 = 1
student_grade_1 = 1
student_detail_1 = [
    {'gender': 'Male'},
    {'score1' : 95},
    {'score2' : 85}
]
# 학생 2
student_name2 = "OH"
student_num2 = 2
student_grade_2 = 2
student_detail_2 = [
    {'gender': 'Female'},
    {'score1' : 100},
    {'score2' : 75}
]
# 학생 3
student_name3 = "LEE"
student_num3 = 3
student_grade_3 = 3
student_detail_3 = [
    {'gender': 'Male'},
    {'score1' : 50},
    {'score2' : 65}
]

# 2. 리스트 구조로 바꿔보기 => 한번에 입력가능 but 단점있음
student_names_list = ['Kim','Oh','Lee']
student_numbers_list = [1,2,3]
student_grades_list = [1,2,3]
student_detailS_list = [ 
    {'gender': 'Male','score1' : 95,'score2' : 85},
    {'gender': 'Female', 'score1' : 100, 'score2' : 75},
    {'gender': 'Male','score1' : 50,'score2' : 65}   
]

# 단점 : 관리하기 힘들다..! 지워줄때 다 같이 맞춰서 지워줘야함
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_detailS_list[1]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_detailS_list)

# 3. 딕셔너리구조 => 좀더 편하지만, 단점 존재
# 단점 : 코드 반복, 중첩 문제
students_dicts =[
    {'student_name':'Kim', 'student_num':1, 'student_grad':1,'student_detail':{'gender':'Male','score1':95,'score2':85}},
    {'student_name':'Oh', 'student_num':2, 'student_grad':2,'student_detail':{'gender':'Female','score1':100,'score2':75}},
    {'student_name':'Lee', 'student_num':3, 'student_grad':3,'student_detail':{'gender':'Male','score1':50,'score2':65}}
    
]

del students_dicts[1]
print(students_dicts)

# 클래스 구조

class Student():
    def __init__(self,name,num,grade,details):
        self._name = name
        self._num = num
        self._grade = grade
        self._details = details

    def __str__(self):
        return 'str : {}-{}'.format(self._name, self._num)
    
    # str이 없다면 repr을 호출
    def __repr__(self):
        return 'str : {}-{}'.format(self._name, self._num)

print()
print('======================================')
student1 = Student('Kim',1,1,{'gender':'Male','score1':95,'score2':85})
student2 = Student('Oh',2,2,{'gender':'Male','score1':100,'score2':75})
student3 = Student('Lee',3,3,{'gender':'Male','score1':65,'score2':55})

print(student1.__dict__)

s_lst = []
s_lst.append(student1)
s_lst.append(student2)
s_lst.append(student3)


print()
for x in s_lst:
    print(x)



