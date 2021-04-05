N = int(input())

coin_list = [500,100,50,10,5,1]
money = 1000-N
total_coin = 0

for coin in coin_list:
    if coin > money:
        pass
    else:
        coin_num = money // coin
        total_coin += coin_num
        money -= (coin *coin_num)

print(total_coin )


# 풀이 2
changes = 1000 - int(input())
count = 0

for i in [500, 100, 50, 10 , 5, 1]:
    count += changes//i
    changes %= i

print(count)
