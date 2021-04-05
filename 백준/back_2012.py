n = int(input())
grade = []
for _ in range(n):
    grade.append(int(input()))

grade = sorted(grade)
result = 0

for i in range(0,len(grade)):
    if i+1 != grade[i]:
        result += abs((i+1 - grade[i]))

print(result)
