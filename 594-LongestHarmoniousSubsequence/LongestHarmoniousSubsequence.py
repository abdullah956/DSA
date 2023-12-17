from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap={}
        count = 0
        for i in range(len(nums)):
            print("number in array :", nums[i])
            if nums[i] not in hashmap:
                print("number not present in map :",nums[i])
                hashmap[nums[i]] = 1
            else:
                print("present in hashmap :",nums[i])
                hashmap[nums[i]] += 1
                print("their count in map :",hashmap[nums[i]])
        if len(hashmap) <= 1:
            return 0
        for key in hashmap:
            print("key before increment :",key)
            if key + 1 in hashmap:
                print("key checking to next :",key+1)
                print("hash value at key :",hashmap[key])
                print("hash value at next key :",hashmap[key+1])
                print("count so far :",count)
                count = max(count, hashmap[key] + hashmap[key + 1])
                print("key counts",hashmap[key] + hashmap[key + 1])
        return count
arr= [1,3,2,2,5,2,3,7]
s = Solution()
print(s.findLHS(arr))