

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            k +=1
            i +=1
        else:
            array[k] = right[j]
            k +=1
            j +=1
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            k +=1
            j +=1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            k += 1
            i += 1
    return array

n, k = map(int,input().split( ))

lst = list(map(int,input().split( )))
lst = merge_sort(lst)
print(lst)
print(lst[k-1])
