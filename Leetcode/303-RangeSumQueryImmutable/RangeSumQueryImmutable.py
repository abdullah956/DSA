from typing import List
from itertools import accumulate
import operator
class NumArray:

    def __init__(self, nums: List[int]):
        self.acumu = [0] + list(accumulate(nums,operator.add))
        print(self.acumu)
    def sumRange(self, left: int, right: int) -> int:
        return self.acumu[right+1] - self.acumu[left]
        

x =[-2, 0, 3, -5, 2, -1]
s = NumArray (x)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

class NumArray:

    def __init__(self, nums: List[int]):
        self.acumu = [0]
        for num in nums :
            self.acumu = self.acumu + [self.acumu[-1] + num]
        print(self.acumu)
    def sumRange(self, left: int, right: int) -> int:
        return self.acumu[right+1] - self.acumu[left]


q = [0, -2, -2, 1, -4, -2, -3]
w =[0, 2], [2, 5], [0, 5]

print(q[2+1]-q[0])
print(q[5+1]-q[2])
print(q[6]-q[0])