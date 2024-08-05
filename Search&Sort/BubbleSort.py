from typing import List
def BubbleSort(array : List[int]) -> List[int]:
    for i in range(len(array)-1,0,-1) :
        for j in range(i) :
            if array[j] > array[j+1] :
                array[j] , array[j+1] = array[j+1] , array[j]
    return array
array = [9,5,4,3,8,7,6,2,1,0]
print(BubbleSort(array))
