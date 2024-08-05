from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self):#, head: ListNode) -> List[int]:
        nodeValues = [2,7,4,3,5]
        #current = head
        #while current:
        #    nodeValues.append(current.val)
        #    current = current.next
        output = [0] * len(nodeValues)
        stack = []
        for index, value in enumerate(nodeValues):
            print("nodevalues :", nodeValues)
            print("in for index and value :",index , value)
            while stack and nodeValues[stack[-1]] < value:
                print("in while index and value and peek :",index , value, stack[-1])
                output[stack.pop()] = value
            stack.append(index)
            print("stack after taking index :", stack)
            print("output be like :", output)
            print()
        return output
s = Solution()
s.nextLargerNodes()