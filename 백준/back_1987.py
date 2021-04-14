dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    global result
    # 동일한 경우 한번만 계산 하기 위해서 set사용
    q = set()
    q.add((x,y,board[x][y]))
    
    while q:
        x,y,step = q.pop()
        # 가장 긴 거리를 저장
        result = max(result, len(step))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ( 0 <= nx and nx < R and 0 <= ny and ny < C and board[nx][ny] not in step):
                q.add((nx,ny, step + board[nx][ny]))



R, C = map(int,input().split(' '))
board = []

for _ in range(R):
    board.append(input())

result = 0
bfs(0,0)
print(result)
