class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        checkJ=set(jewels)
        total=0
        for stone in stones :
            if stone in checkJ :
                total +=1
        return total