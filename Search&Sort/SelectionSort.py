from typing import List
def SelectionSort(array : List[int]) -> List[int]:
    for i in range(len(array)) :
        for j in range(i+1,len(array)) :
            if array[i] > array[j] :
                array[i] , array[j] = array[j] , array[i]
    return array
array = [9,5,4,3,8,7,6,2,1,0]
print(SelectionSort(array))
