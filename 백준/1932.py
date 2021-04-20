# 정수 삼각형
N = int(input())
dp = [[] for _ in range(N)]
for i in range(N):
    dp[i].extend(list(map(int,input().split())))


for i in range(1,N):
    for j in range(0,len(dp[i])):
        if j == 0:
            dp[i][j] += dp[i-1][0]
        elif j == i :
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[-1]))
