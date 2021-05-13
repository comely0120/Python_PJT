from copy import deepcopy

N = int(input())
Board = [list(map(int, input().split())) for _ in range(N) ]

# 90도 회전
def rotate90(B,N):
    NBoard = deepcopy(B)
    for i in range(N):
        for j in range(N):
            NBoard[j][N-i-1] = B[i][j]
    return NBoard

# 줄 단위로 왼쪽방향으로 합치기
def convert(lst,N):
    new_list = [ i for i in lst if i ]
    for i in range(1,len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] =0
    new_list = [i for i in new_list if i]
    return new_list + [0] *(N-len(new_list))

def dfs(N, B, cnt):
    ret = max([max(i) for i in B]) # 판에 존재하는 수들 중 최대값

    if cnt == 0: # 5번 다 돌렸으면 종료
        return ret
    
    for _ in range(4): # 4개의 줄에 대해 각각 왼쪽으로 합침
        X = [convert(i,N) for i in B]
        
        if X != B: # 다르다는 건 합쳐졌다는 것! (같다면 더이상 합칠 수 있는 수가 업다는 것)
           ret= max(ret, dfs(N,X,cnt-1) )  #  Board로 다시 dfs
        
        B = rotate90(B,N) # 판 자체 회전
    return ret



print(dfs(N,Board,5))