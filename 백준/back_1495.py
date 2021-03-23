N, S, M = map(int, input().split())
V = list(map(int, input().split()))

D = [[0]*(M+1) for _ in range(N+1)]
D[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):
        if D[i-1][j] == 0:
            continue
        if j - V[i-1] >= 0:
            D[i][j - V[i-1]] = 1
        if j + V[i-1] <= M:
            D[i][j + V[i-1]] = 1

result = -1

for i in range(M,-1,-1):
    if D[N][i] == 1:
        result = i
        break

print(result)

        

