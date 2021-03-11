from collections import deque

N, M = map(int, input().split( ))
adj = [[] for _ in range(N+1)]

def bfs(C): # 경로가 있는지
    queue = deque([start_node])
    visited = [False] * (N+1)
    visited[start_node] = True
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= C:
                visited[y] = True
                queue.append(y)
    return visited[end_node]


start = 1000000000
end = 1

for _ in range(M):
    x, y, weight = map(int,input().split())
    adj[x].append((y,weight))
    adj[y].append((x,weight))
    start  = min(start,weight) # 최소 중량
    end = max(end,weight) # 최대 중량


start_node, end_node = map(int, input().split())
result = start # 결과의 초기값은 제일 작은 중량으로 초기화!

while( start <= end ):
    mid = (start + end)//2
    if bfs(mid): # 이동이 가능하다면 결과값(result)를 mid로 바꿔주고 start증가
        result = mid
        start = mid+1
    else: # 이동이 불가능 하다면 end값 감소
        end = mid -1

print(result)
    