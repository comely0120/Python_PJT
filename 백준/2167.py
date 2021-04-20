# 2차원 배열의 합
N, M = map(int, input().split())
data =[[] for _ in range(N)]

for i in range(N):
    data[i].extend(list(map(int,input().split())))

K = int(input())

for _ in range(K):
    answer = 0
    i, j, x, y = map(int, input().split())
    if i != x :
        while i <= x :
            if j == y:
                answer += data[i-1][j-1]
                i += 1

            else:
                answer += sum(data[i-1][j-1:y])
                i+=1
    else:
        answer += sum(data[i-1][j-1:y])

    print(answer)
