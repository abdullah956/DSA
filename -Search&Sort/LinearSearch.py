from typing import List
def linearSearch(array : List[int] , val : int) -> int:
    for i in range(len(array)):
        if (array[i] == val):
            return i
    return -1
array = [9,5,4,3,8,7,6,2,1,0]
print(linearSearch(array,1))