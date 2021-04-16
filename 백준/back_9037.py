def check(N,candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy[i] += 1
    return len(set(candy)) == 1

def teacher(N, candy):
    # 오른쪽 친구에게 추가해줄 사탕 개수
    tmp_lst = [0 for i in range(N)]
    for idx in range(N):
        if candy[idx] % 2 :
            candy[idx] += 1
        tmp_lst[(idx+1)%N] = candy[idx] // 2
        candy[idx] //= 2
    
    for idx in range(N):
        candy[idx] += tmp_lst[idx]
    return candy



def process():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0
    while not check(N, candy):
        cnt += 1
        candy = teacher(N,candy)
    print(cnt)


for _ in range(int(input())):
    process()

