import copy
size = int(input())
A = list(map(int, input().split()))

dp = copy.deepcopy(A)
rev = [0 for _ in range(size)]
idx = 0

for i in range(1,size):
    for j in range(i):
        if A[i] > A[j] and dp[i] < A[i] + dp[j]:
            dp[i] = max(A[i] + dp[j], dp[i])
            rev[i] = j
    
    if dp[idx] < dp[i] :
        idx = i

print(dp[idx])
while rev[idx] != idx :
    print(A[idx], sep='')
    idx = rev[idx]
print(A[idx])