N = int(input())
array = []


for _ in range(N):
    array.append(int(input()))

#print(array)

left = [array[0]]
right = [array[-1]]


for i in range(0,len(array)):
    if left[-1] < array[i]:
        left.append(array[i])
    if right[-1] < array[len(array)-i-1]:
        right.append(array[len(array)-i-1])

print(len(left))
print(len(right))

