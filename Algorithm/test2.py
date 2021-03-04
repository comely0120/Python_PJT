# 문제 
'''
이진 탐색법은 정렬된 자료를 탐색하는 데에 사용할 수 있다. 
인덱스가 낮을 수록 더 작은 값으로 정렬된 2차원 리스트에서 target을 찾으면 True를 반환하고, 
target을 찾을 수 없으면 False를 반환하는 프로그램을 작성하시오.
'''

# 문제 풀이
def searchMatrix(matrix,target):
    def searchRow(sub_martix):
        m = len(sub_martix)
        print('m',m)

        if m == 1 :
            return sub_martix[0]

        mid = m//2
        left = sub_martix[:mid]
        right = sub_martix[mid+1:]

        if sub_martix[mid][0] <= target <= sub_martix[mid][-1]:
            return sub_martix[mid]
        elif sub_martix[mid][0] > target:
            print('R-left',left)
            return searchRow(left)
        else:
            print('R-right',right)
            return searchRow(right)


    def searchCol(array):
        n = len(array)
        print('n',n)

        if n==0:
            return False
        if n ==1:
            if array[0] == target:
                return True
            else:
                return False
        mid = n //2
        left = array[:mid]
        right = array[mid+1:]

        if array[mid] == target:
            return True
        elif array[mid] > target:
            print('C-left',left)
            return searchCol(left)

        else:
            print('C-right',right)
            return searchCol(rgiht)

        
    array = searchRow(matrix)
    print('COL',array)
    return searchCol(array)
        

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
print(searchMatrix(matrix, target))