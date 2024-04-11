from typing import List
class Soluion :
    def containsNearbyDuplicate(self,nums : List[int], k: int) -> bool :
        Map = {}
        for i in range(len(nums)) :
            current = nums[i]
            if current in Map and i-Map[current]<=k :
                return True
            else:
                Map[current]=i
        return False
    
    """
1,2,3,1
    i 3
    current = 1
    Map {
 1:0
 2:0
 3:0
    }
    3-0<=k

    """