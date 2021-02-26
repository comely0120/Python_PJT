# -*- coding: utf-8 -*-

## 문제1
"""
Min Heap 자료구조를 이용하면 최대값을 `O(logN)`의 시간복잡도로 찾을 수 있다. Min Heap을 이용하면 우선순위 값이 낮은 자료를 먼저 출력하는 Priority Queue를 구현할 수 있다. Min Heap을 이용한 Priority Queue는 아래와 같은 특징을 가진다.

- Min Heap을 이용한 Priority Queue의 특징
  - 자료를 입력하는 동작과 출력하는 동작 모두 `O(logN)`으로 이루어진다.
  - 우선순위 값이 낮은 자료를 먼저 출력하되, 우선순위 값이 같은 자료끼리는 순서를 고려하지 않는다.
  - 다음과 같은 Method들을 구현한다.
    1. `is_empty()`: Queue가 비어있으면 True, 비어있지 않으면 False를 출력한다.
    1. `put()`: Priority Queue에 자료를 입력한다. 자료는 길이가 2인 Tuple로, `(우선순위, 자료)` 형태로 입력받는다.
    1. `get()`: Priority Queue에서 자료를 출력한다. 출력한 데이터는 Priority Queue에서 삭제한다. 더이상 출력할 데이터가 없는 경우 None을 출력한다.
    1. `peek()`: Priority Queue에서 자료를 출력한다. 출력한 데이터는 Priority Queue에 그대로 유지한다. 더이상 출력할 데이터가 없는 경우 None을 출력한다.
"""

## 문제 1 풀이
class PriorityQueue:
    def __init__(self):
        self.priority_array = list()
        self.key = None
        self.value = None
 
    def is_empty(self):
        if len(self.priority_array) == 0:
            return True
        return False
 
    def put(self, data):
        self.key = data[0]
        self.value = data[1]
        if len(self.priority_array) == 0:
            self.priority_array.append(data)
            self.key = data[0]
            self.value = data[1]
            print("처음추가 : ",self.priority_array)
            print("===========================")
            

        else:
            #self.priority_array.append(data)
            self.key = data[0]
            self.value = data[1]
            length = len(self.priority_array)
            print( "추가하기전 배열 길이 : ",length)
            for index in range(length-1,-1,-1):
                print("인덱스 번호:",index)
                print("비교할 데이터 :  ",self.priority_array[index])
                print("방금 들어온 key값",self.key)
                if  self.key > self.priority_array[index][0]:
                    self.priority_array.insert( index+1,(self.key,self.value))
                    print(self.priority_array)
                    print("===========================")
                    break
                else:
                    pass
            

                    
    def get(self):
        if len(self.priority_array) == 0:
            return None
        print("전:", self.priority_array)
        get_data = self.priority_array[len(self.priority_array)-1]
        del self.priority_array[len(self.priority_array)-1]
        print("후:", self.priority_array)
        return get_data
        
 
    def peek(self):
        if len(self.priority_array) == 0:
            return None
        else:
            return self.priority_array[len(self.priority_array)-1]
# 문제 1 -TEST
pq = PriorityQueue()
pq.put((0, 'a'))
pq.put((5, 'b'))
pq.put((2, 'c'))
pq.put((1, 'd'))
pq.put((3, 'e'))
pq.put((4, 'f'))
print("peek1",pq.peek())
print("peek2",pq.peek())
print("peek3",pq.peek())

print("====peek한 이후에 사라졌는지 아닌지 확인====")
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())

## 문제 2
"""
오름차순으로 정렬된 N개의 정수를 가진 List가 주어져있을 때, 해당 List에 존재하는 서로 다른 값이 몇 가지인지 알아내는 알고리즘을 구현하라. 알고리즘의 제약사항은 아래와 같다. (알고리즘은 `1 <= N <= 10000`에서 테스트된다.)

- 추가 메모리 사용은 `O(1)`으로 제한된다. 따라서 set()와 dict() 등의 자료구조를 사용할 수 없다.
- 알고리즘의 시간복잡도는 `O(N)` 이하로 제한된다.

"""

# 문제 2 풀이
def countUniques(a):
    cnt = 1
    a.sort()
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            pass
        else:
            cnt +=1
    return cnt



print(countUniques([-1, 1, 1, 1, 1, 4, 4, 4, 4, 10, 14, 14]))
print(countUniques([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))

## 문제 3
"""
----
N개의 문자열로 이루어진 List에서 전체 문자열이 앞 n개 문자열이 같다고 할때, 가장 큰 n을 출력하는 알고리즘을 구현하라. (즉, 주어진 모든 문자열의 앞의 몇개의 문자가 일치하는지 출력하라)

```python
def solution(a):
    return 0

# Test code
print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg'])) # 3
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg'])) # 0
```
----
"""

# 문제 3 풀이:

def solution(a):
    result = 0
    for index in range(len(a[0])):
        cnt=0
        for i in range(len(a)-1):
            #print("***",a[i][index],a[i+1][index])
            if a[i][index] == a[i+1][index]:
                cnt +=1 
        #print(cnt)     
        if cnt == (len(a)-1):
            result += 1
            #print(result)
        else:
            break
    return result

print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg']))
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg']))
print(solution(['jkpomh','jkpouslod','jkpowevr','jkpomhd','jkpomho','jkpomhy']))


# 문제 4.
"""

----
자연수 중, **각 자리수를 제곱한 것을 더하는 과정을 반복했을 때 1으로 끝나는 수**를 '행복한 수'라고 한다. '행복한 수'가 아닌 경우 이 과정이 1에 도달하지 못하고 같은 **수열이 반복되는 무한 루프**에 빠지게 된다. 자연수를 입력받았을 때 '행복한 수'인지 판별하는 알고리즘을 작성하라.

'행복한 수'를 찾는 과정의 예
  ```
  19이 행복한 수인지 확인하는 과정
  1^2 + 9^2 = 82
  8^2 + 2^2 = 68
  6^2 + 8^2 = 100
  1^2 + 0^2 + 0^2 = 1 --> True
  ```

```python
def solution(n):
    return True

# Test code
print(solution(19)) # True
print(solution(61)) # False
```

----
"""

# 문제 4 풀이
# 1-> true , 89-> false
def solution(n):
    if n>1:
        sum = 0
        for i in range(len(str(n))):
                sum += int(str(n)[i])**2
        if sum == 89:
            return False
        return solution(sum)
 
    return True

print(solution(19)) # True
print(solution(61)) # False
print(solution(120)) # Fasle

