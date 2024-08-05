class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #empty array
        chace =[[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]

        #filling row column 3,2,1 
        for j in range(len(word2)+1) :
            chace[len(word1)][j] = len(word2) - j
        for i in range(len(word1)+1) :
            chace[i][len(word2)] = len(word1) - i
            
        #starting form the last box
        for i in range(len(word1)-1,-1,-1) :
            for j in range(len(word2)-1,-1,-1) :
                if word1[i] == word2[j] :
                    chace[i][j] = chace[i+1][j+1]
                else :
                    chace[i][j] = 1 + min(chace[i+1][j], chace[i][j+1],chace[i+1][j+1])

        #return 0 index that will have all cost because we started from the begininng
        return chace[0][0]