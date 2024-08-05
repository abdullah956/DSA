from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n, numBits = 0, len(bits), 0
        while i < n:
            bit = bits[i]
            if bit == 1:
                i += 2
                numBits = 2
            else:
                i += 1
                numBits = 1
        return numBits == 1