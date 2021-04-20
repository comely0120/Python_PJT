import copy
size = int(input())
A = list(map(int, input().split()))

dp = copy.deepcopy(A)
print(dp)

for i in range(1,size):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(A[i] + dp[j], dp[i])


print(max(dp))

     
