class Solution:
    def getIntersectionNode(self, headA, headB):
        list1 , list2 = headA , headB
        while list1 != list2 :
            if list1 :
                list1 = list1.next
            else :
                list1 = headB
            if list2 :
                list2 = list2.next
            else :
                list2 = headA
        return list1