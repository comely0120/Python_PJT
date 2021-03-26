from collections import deque

def dfs(V):
    print(V, end='')
    visited[V] = True
    for e in array[V]:
        if not(visited[e]):
            dfs(e)

def bfs(V):
    q = deque([V])
    while q:
        V = q.popleft()
        if not(visited[V]):
            visited[V] = True
            print(V, end='')
            for e in array[V]:
                if not visited[e]:
                    q.append(e)

N, M , V = map(int,input().split())

array = [[] for _ in range(N+1)]

for _ in range(M):
    a , b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)


for e in array :
    e.sort()


visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)