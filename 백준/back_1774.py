import math
import sys
input = sys.stdin.readline

# 두 노드 사이의 길이
def get_distance(p1,p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return math.sqrt((a*a)+(b*b))

# 노드의 정점(제일 꼭대기 부모 노드) 구하기
def get_parent(parent,n):
    if parent[n] == n:
        return n 
    return get_parent(parent,parent[n])

# 정점 연결
def union_parent(parent,a,b):
    a = get_parent(parent,a)
    b = get_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드 a와 b가 연결되어있는지 확인
def find_parent(parent,a,b):
    a = get_parent(parent,a)
    b = get_parent(parent,b)
    if a == b:
        return True
    else:
        return False


edges = []
parent = {}
locations = []
N , M = map(int,input().split())

for _ in range(N):
    x,y = map(int,input().split())
    locations.append((x,y))

length = len(locations)

# 모든 노드들에 대해 길이 구하기
for i in range(length - 1):
    for j in range(i+1, length):
        edges.append((i+1, j+1, get_distance(locations[i],locations[j])))

# 입력으로 주어진 노드들은 연결, 나머지는 정점이 자기 자신
for i in range(1,N+1):
    parent[i] = i

for i in range(M):
    a,b = map(int, input().split())
    union_parent(parent, a,b)

# 길이를 key로 정렬 (최단 거리 찾기 위해서)
edges.sort(key=lambda data: data[2])

result = 0
for a, b, cost in edges:
    # 최단 거리로 노드들 연결
    if not find_parent(parent,a,b):
        union_parent(parent, a,b)
        result += cost
print('%0.2f' %result)
