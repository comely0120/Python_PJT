N, M = map(int, input().split())

team_mem , mem_team  = {} , {}

for _ in range(N):
    team_name , member = input(), int(input())
    team_mem[team_name] = []
    
    for _ in range(member):
        name =  input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name


for _ in range(M):
    name, quiz = input(), int(input())

    if quiz:
        print(mem_team[name])

    else:
        for i in sorted(team_mem[name]):
            print(i)
