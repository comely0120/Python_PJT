import heapq

N, M = map(int, input().split())
array = [[] for i in range(N+1)]
indegree = [0] * (N+1)

heap = []
result = []

# 정점, 진입 차수 리스트 만들기
for _ in range(M):
    x, y = map(int, input().split())
    array[x].append(y)
    indegree[y] += 1

# 제일 처음 시작점 찾기
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap,i)
        

while heap:
    data = heapq.heappop(heap)
    result.append(data)

    for y in array[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap,y)

for i in result:
    print(i)



