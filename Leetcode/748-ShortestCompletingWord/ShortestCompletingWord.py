from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        Map={}
        LS=""
        output=[]
        for c in licensePlate :
            if c.isalpha() :
                c = c.lower()
                LS+=c
                if c in Map :
                    Map[c] +=1
                else:
                    Map[c] =1
        for i in range(len(words)) :
            count=0
            for j in LS :
                if j in Map :
                    if words[i].count(j) >= Map[j] :
                        count+=1
            if count == len(LS) :
                if output :
                    if len(words[i]) < len(output[0]) :
                        output[0] = words[i]
                else:
                    output.append(words[i])
        return output[0]