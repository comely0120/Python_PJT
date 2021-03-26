def dfs(V):
    visited[V] = True
    for e in array[V]:
        if not(visited[e]):
            dfs(e)

N = int(input())
L = int(input())
array = [[] for _ in range(N+1)]

for _ in range(L):
    x, y = map(int, input().split())
    array[x].append(y)
    array[y].append(x)

for e in array:
    e.sort()

visited = [False] * (N+1)
dfs(1)

cnt = 0
for i in range(2,N+1):
    if visited[i] == True:
        cnt +=1

print(cnt)