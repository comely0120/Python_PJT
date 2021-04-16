N, L, K = map(int, input().split())

total_sum = 0 
cnt = 0

for _ in range(N):
    easy, hard = map(int, input().split())
    if L >= hard:
        total_sum += 140
        cnt += 1
    elif L >= easy:
        total_sum += 100
        cnt += 1
    elif L < easy:
        continue
    if cnt == K:
        break

print(total_sum)

'''
다른 풀이
'''

easy, hard = 0,0 
for _ in range(M):
    sub1, sub2 = map(int, input().splilt())

    if sub2 <= L :
        hard += 1
    elif sub1 <= L:
        easy += 1

ans = min(hard, K) * 140

if hard < K:
    ans += min(K-hard, easy)*100

print(ans)

