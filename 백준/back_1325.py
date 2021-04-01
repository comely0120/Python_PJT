from collections import deque

N, M = map(int, input().split())
array = [[] for _ in range(N+1)]

for _ in range(M):
    A,B = map(int, input().split())
    array[B].append(A)
 

def bfs(V):
    q = deque([V])
    visited = [False] * (N+1)
    visited[V] = True
    count = 1
    while q:
        V = q.popleft()
        for e in array[V]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count += 1

    return count

result = []
max_value = -1

for i in range(1,N+1):
    cnt = bfs(i)

    if cnt > max_value :
        result=[i]
        max_value = cnt
    elif cnt == max_value:
        result.append(i)
        max_value = cnt

for e in result:
    print(e,end=' ')
