class Solution :
    def checkRecord(self, s:str) -> bool :
        absent = 0
        late = 0
        for x in s :
            if x=="A" :
                absent+=1
                late=0
            elif x=="L" :
                late+=1
            else :
                late=0
            if absent>1 or late>2 :
                return False
        return True