from typing import List
def InsertionSort(array : List[int]) -> List[int]:
    for i in range(1,len(array)) :
        j = i
        while array[j-1] > array[j] and j > 0 :
            array[j-1] , array[j] = array[j] , array[j-1]
            j-=1
    return array
array = [9,5,4,3,8,7,6,2,1,0]
print(InsertionSort(array))
