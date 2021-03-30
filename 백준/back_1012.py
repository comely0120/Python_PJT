import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    visited[x][y] = True
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in directions:
        nx , ny = x+dx , y+dy
        # 범위를 넘어가는 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        # 상하좌우 좌표에 배추가 있고 아직 방문하지 않았다면
        if array[nx][ny] and not visited[nx][ny]:
            dfs(nx,ny)


test_case = int(input())

for _ in range(test_case):
    M , N , K = map(int,input().split())
    array = [[0]* M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        y, x = map(int, input().split())
        array[x][y] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            # 배추가 있는 곳이고 아직 방문하지 않았다면
            if array[i][j] and not visited[i][j]:
                # result는 dfs가 수행된 횟수
                dfs(i,j)
                result += 1
    print(result)

