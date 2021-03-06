
N = int(input())
num = 1
cnt =0

while N >= num:
    N = N - num
    num +=1
    cnt +=1
    if num > N:
        num = 1

print( cnt)



