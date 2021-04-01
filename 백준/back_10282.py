import heapq
import sys
input= sys.stdin.readline


def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0,start))
    distance[start] = 0
    
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist :
            continue
        for i in array[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data,(cost,i[0]))
               




for _ in range(int(input())):
    n, d, start = map(int,input().split())
    array = [[]for _ in range(n+1)]
    distance = [1e9] *(n+1)
    for i in range(d):
        a, b, cost = map(int, input().split())
        array[b].append((a,cost))

    dijkstra(start)
    count = 0
    max_distance = 0 
    for i in distance:
        if i != 1e9:
            count += 1
            if i > max_distance:
                max_distance = i
    print(count, max_distance)

