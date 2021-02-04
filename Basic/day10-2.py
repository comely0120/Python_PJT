# 파일 쓰기
# 2-1. 없는 파일이라도  open을 써준다
with open('./resource/test1.txt','w') as f:
    f.write("wow~~~\n")


# 2-2
from random import randint
with open('./resource/test2.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(1,50)))
        f.write('\n')


# 2-3
# 리스트를 써보자, wirtelines 메소드 사용!!
list = ['pizza\t','pasta\t']
with open('./resource/test3.txt','w') as f:
    f.writelines(list)


# 2-4 
# print 사용해서 써보자 => file이란 변수를 사용!!
with open('./resource/test4.txt','w') as f:
    print('TEST WIRTE USING print()', file=f)
    print('REMEBER, should use file!',file=f)