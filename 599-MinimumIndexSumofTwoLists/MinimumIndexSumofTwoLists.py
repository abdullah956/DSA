from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = {}
        for i in range(len(list1)):   #step 1
            print("index",i)
            print(list1[i])
            print(hashmap)
            hashmap[list1[i]] = i
        
        res = []

        minsum = float("inf")   #step 2
        
        for j in range(len(list2)):    #step 3
            print("index of scnd lsit",j)
            print("seocnd lsit :",list2[j])
            if list2[j] in hashmap:
                print("list2[",j,"]preent in map :",list2[j])
                Sum = j + hashmap[list2[j]]    #step 3a
                print("sum ",Sum)
                print()
                print("min sum",minsum)
                if Sum < minsum:   #step 3b
                    minsum = Sum
                    print("after swapping min ",minsum)
                    res = []
                    res.append(list2[j])
                    print(list2[j])
                elif Sum == minsum:     #step 3c
                    res.append(list2[j])
        return res
s=Solution()
l1=["Shogun","Tapioca Express","Burger King","KFC"]
l2= ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(s.findRestaurant(l1,l2))
