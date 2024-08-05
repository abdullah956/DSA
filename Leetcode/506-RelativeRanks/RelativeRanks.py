from typing import List
class Solution :
    def findRelativeRanks(self,score : List[int]) -> List[str] :
        sorted_score = sorted(score, reverse=True)
        count={}
        for i in range(len(sorted_score)) :
            if i==0 :
                count[sorted_score[i]] = "Gold Medal"
            elif i==1 :
                count[sorted_score[i]] = "Silver Medal"
            elif i==2 :
                count[sorted_score[i]] = "Bronze Medal"
            else:
                count[sorted_score[i]] = str(i+1)
        result = []
        for i in score :
            result.append(count[i])
        return result