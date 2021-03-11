'''
문제 1
리스트 [1,2,3,...,n] 를 섞는 방법은 총 n! 가지이다. n = 3일 때 3! = 6개의 섞은 결과는 아래와 같은 순서를 가진다고 하자.

[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
n과 k가 주어졌을 때, k번째 섞은 결과를 반환하시오. (단, 1 <= n <= 9, 1 <= k <= n!)
'''
from math import factorial

def solution(n,k):
    answer = []
    num_lst = list(range(1,n+1)) 
    while n!= 0:
        fact = factorial(n-1)
        answer.append(num_lst.pop( (k-1)//fact))
        n -=1
        k %= fact
    return answer
# 결과
print('문제 1: ', solution(3,3))

''' 
문제 2
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5
5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다. 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.
'''

def solution2(N,number):
    sets = [{},{N}]

    if N == number: # 같으면 그냥 1출력
        return 1
    
    for i in range(2,9): # N은 1부터9까지니까
        current_set = {int(str(N)*i)}

        for j in range(1, i//2 +1):
            for val_j in sets[j]:
                for val_k in sets[i-j]:
                    # -랑 // 는 주의!!
                    current_set.add(val_j + val_k)
                    current_set.add(val_j - val_k)
                    current_set.add(val_k - val_j)
                    current_set.add(val_j * val_k)
                    if val_k != 0:
                        current_set.add(val_j // val_k)
                    if val_j != 0:
                        current_set.add(val_k // val_j)
                    
                    
                    if number in current_set:
                        return i
                   
        sets.append(current_set)
    return -1
                
print('solution2',solution2(5,12))

'''
문제 3
n개의 정수로 이루어진 리스트 nums와 정수 target이 주어졌을 때, nums에 있는 정수 4개를 합하여 target을 만들 수 있는 모든 조합을 구하시오. 단, 정답에는 동일한 정수 조합이 여러개 포함되어서는 안된다.

예시 입력

nums = [1, 0, -1, 0, -2, 2]
target = 0
출력:

[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
def solution3(nums, target):
    nums = sorted(nums)
    used = [0] *len(nums)
    def generate(chosen):
        if len(chosen) == 4 and sum(chosen)==target :
            print(chosen)
        
        start = nums.index(chosen[-1]) +1 if chosen else 0
        for nxt in range(start, len(nums)):
            if used[nxt] == 0 and (nxt == 0 or nums[nxt-1] != nums[nxt] or used[nxt-1]):
                chosen.append(nums[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])

nums = [1, 0, -1, 0, -2, 2]
target = 0
print('solution3')
solution3(nums,target)


'''
문제 4
정수로 이루어진 수열 x가 주어졌을 때, x[i-1] < x[i], x[i+1] < x[i]인 x[i]를 피크라고 부른다. a에 피크가 단 하나 반드시 존재할 때, 이 피크를 찾아 출력하는 O(logN) 알고리즘을 구현하시오.

예시 입력

                    x	                              return
[-4, -4, -2, 0, 0, 2, 4, 5, 6, 3, 2, -4, -6]	        6
[-1, -1, -1, -1, 0, 1, 20, 19, 17]	                    20
'''
def solution4(x):
    if len(x) == 1:
        return x
    if len(x) ==2:
        return x[1]

    mid = len(x)//2
    
    if x[mid]>x[mid-1] and x[mid]>x[mid+1]:
        return x[mid]
    else:
        if x[mid] < x[mid+1]:
            return solution4(x[mid+1:])
        else:
            return solution4(x[:mid])

a = [-1, -1, -1, -1, 0, 1, 20, 19, 17]
print('solution4',solution4(a))

'''
문제 5
그래프를 DFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력: 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력: V부터 방문된 점을 순서대로 출력한다.

예시 입출력

N	M	V	                   edges	                      출력
4	5	1	    [[1, 2], [1, 3], [1,4], [2, 3], [3, 4]]	    1 2 3 4
'''

def solution5(N,M,V,edges):
    visited = []
    adj_lists = [[]]*(N+1)

    for i in range(1, N+1):
        adj_list = list(map(lambda x:x[1], filter(lambda x: x[0]==i, edges))) + list(map(lambda x:x[0],(filter(lambda x:x[1] == i, edges))))
        adj_list.sort()
        adj_lists[i] = adj_list
    
    def dfs(node):
        visited.append(node)
        print(node,end=' ')
        for n in adj_lists[node]:
            if n not in visited:
                dfs(n)
    dfs(V)

N, M, V = 4, 5, 1
edges = [[1, 2], [1, 3], [1,4], [2, 3], [3, 4]]
solution5(N, M, V, edges)