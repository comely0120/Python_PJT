from collections import deque
import heapq
import sys
input = sys.stdin.readline

def djkstra():
    heap_data = []
    heapq.heappush(heap_data,(0,start))
    distance[start] = 0
    while heap_data:
        dist,now = heapq.heappop(heap_data)
        if distance[now] < dist :
            continue
        for i in array[now]:
            length = dist + array[now][i]
            if distance[i] > length :
                distance[i] = length
                heapq.heappush(heap_data,(length,i))

def bfs():
    q = deque()
    # 도착점 부터 역추적
    q.append(end)
    while q:
        now = q.popleft()
        if now == start: # 시작점 도달
            continue # break하면 다른 최단 경로 확인 불가
        for prev, length in reverse_array[now]:
            if distance[now] == distance[prev] +length:
                if(prev, now) not in dropped:    
                    dropped.append((prev,now))
                    q.append(prev)


while True:
    spot, road = map(int,input().split())
    if spot == 0:
        break
    start , end = map(int, input().split())
    array = [dict() for _ in range(spot)]
    reverse_array = [[] for _ in range(spot)]

    for _ in range(road):
        x, y, length = map(int, input().split())
        # x에서 y로 가는 정보
        array[x][y] = length
        # y로 들어오는 x의 정보
        reverse_array[y].append((x,length))
    
    dropped = list()
    distance = [1e9] *( spot)
    # 최단 경로의 길이 찾기
    djkstra()
    # 최단 경로 역추적
    bfs()

    # 최단 경로 제거
    for x, y in dropped:
        del array[x][y]

    distance = [1e9] * (spot)
    djkstra()
    if distance[end] != 1e9:
        print(distance[end])
    else:
        print(-1)

