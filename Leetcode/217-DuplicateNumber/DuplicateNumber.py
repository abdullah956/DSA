class Solution:
    def dups (nums) :
        Map ={}
        for i in range(len(nums) ) :
            if nums[i] not in Map :
                Map[nums[i]] =1 
            else :
                nums[i] +=1
        for i in range(len(nums)):
                if Map[nums[i]] > 1 :
                    return True
        return False