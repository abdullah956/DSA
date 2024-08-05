import typing
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits   = digits[::-1]
        limit  =1
        index =0
        while limit :
            if index < len(digits) :
                if digits[index]==9 :
                    digits[index] =0
                else:
                    digits[index] = digits[index] +1
                    limit = 0
            else :
                digits.append(1)
                limit = 0
            index = index + 1
        return digits[::-1]
s = Solution()
print(s.plusOne([9,9,9]))