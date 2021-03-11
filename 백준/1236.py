N, M = map(int,input().split(' '))
array = []
for i in range(N):
    data.append(input())

# 열과 행의 개수 많큼 배열 만들기
row = [0]*N
col = [0]*M

# array에 X가있으면 해당 row,col을 1로 바꿔주기
for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':
            row[i] = 1
            col[i] = 1

# 비어있는 행 개수 구하기
row_cnt = 0
for i in range(n):
    if row[i] == 0:
        row_cnt += 1

# 비어있는 열 개수 구하기
col_cnt = 0
for i in range(n):
    if col[i] == 0:
        col_cnt += 1

print(max(row_cnt,col_cnt))
