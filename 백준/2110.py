N, C = map(int, input().split())
home = []

for _ in range(N):
    home.append(int(input()))

home = sorted(home)
max_gap = home[-1] - home[0]

diff = [a-b for a, b in zip(home[l:],home[:-1])]
diff = sorted(diff)
min_gap = diff[0]

result = 0

while( min_gap <= max_gap):
    mid = (max_gap + min_gap) // 2
    value = home[0]
    count = 1 # 공유기를 설치할 수 있는 집의 수
    
    # 현재 mid 이상만큼 떨어져 있는 집들을 구한다
    for i in range(1,len(home)):
        if home[i] >= value + mid: 
            value = home[i]
            count += 1

    # for문이 끝났을 때 count가 C이상이라면, mid_gap을 증가
    if count >= C:
        min_gap = mid + 1
        result = mid

    # C보다 작다면(즉, 문제 조건을 만족하지 못한다면)
    # max_gap을 mid-1로 감소시킨다
    else:
        max_gap = mid -1

print(result)



