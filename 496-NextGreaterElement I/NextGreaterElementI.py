from typing import List
class Solution :
    def nextGreaterElement(self,nums1:List[int],nums2:List[int])->List[int]:
        def greaterTowardsRight(nums2 : List[int]) :
            stack =[]
            result = []
            for i in range(len(nums2)-1,-1,-1) :
                while len(stack)>0 and nums2[i]>=stack[-1] :
                    stack.pop()
                if len(stack)==0 :
                    result.append(-1)
                    stack.append(nums2[i])
                else:
                    result.append(stack[-1])
                    stack.append(nums2[i])
            return result[::-1]
        result = greaterTowardsRight(nums2)
        index_Map = {nums2[i]:i for i in range(len(nums2))}
        output=[]
        for i in nums1 :
            index = index_Map[i]
            output.append(result[index])
        return output
        