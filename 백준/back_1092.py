import sys

N = int(input())
cranes = list(map(int,input().split( )))
M = int(input())
box = list(map(int, input().split()))


if max(cranes) < max(box):
    print(-1)
    sys.exit()

# 각 크레인이 현제 옮길 박스 번호
positions = [0] * N
# 박스가 옮겨졌는지 확인
checked = [False] *M

cranes.sort(reverse=True)
box.sort(reverse=True)

result = 0
count = 0

while True:
    if count == len(box): # 박스 다 옮겼다면 종료
        break
    for i in range(N):
        while positions[i] < len(box):
            if not checked[positions[i]] and cranes[i] >= box[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result += 1

print(result)