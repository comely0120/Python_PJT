# 가장 큰 정사각형
N, M = map(int, input().split())
table = [list(map(int, list(input().rstrip()))) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        if i>0 and j>0 and table[i][j] == 1:
            table[i][j] += min(table[i-1][j], table[i][j-1], table[i-1][j-1])
        ans = max(ans, table[i][j])
print(ans*ans)
