from typing import List
def linearSearch(array : List[int] , val : int) -> int:
    start , end = 0 , len(array)-1
    while start <= end:
        mid = start + (end - start)//2
        if array[mid] == val:
            return mid
        elif array[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return -1
array = [1,2,3,4,5,6,7,8,9]
print(linearSearch(array,5))