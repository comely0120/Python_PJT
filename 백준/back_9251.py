X = input()
Y = input()
D = [[0] * (len(Y)+1) for _ in range(len(X)+1)]

for i in range (1, len(X)+1):
    for j in range(1, len(Y)+1):
        if X[i-1] == Y[j-1]:
            D[i][j] = D[i-1][j-1] + 1
        else:
            D[i][j] = max(D[i][j-1], D[i-1][j])

print(D[len(X)][len(Y)])