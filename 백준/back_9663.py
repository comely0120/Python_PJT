# x행의 i열에 Queen을 두어도 되는가 확인
def check(x):
    for i in range(x): # 이전 행에 놓았던 Queen을 모두 확인
        if row[x] == row[i]:
            return False # 위쪽에 이미 있는 경우
        if abs(row[x]-row[i]) == x - i:
            return False # 대각선에 이미 있는 경우
    return True


def dfs(x):
    global result
    if x == n :
        result += 1
    else:
        # x번째 행의 각각의 모든 열(0~n-1)에 Quuen을 둔다고 할때
        for i in range(n):
            row[x] = i
            # x 행의 해당 열(i)에 Queen을 둬도 괜찮은 지 확인
            if check(x):
                # 괜찮다면, 다음 행으로 넘어가기
                dfs(x+1)
            
n = int(input())
row = [0]*n
result = 0
dfs(0) # 첫번째 행부터 시작
print(result)