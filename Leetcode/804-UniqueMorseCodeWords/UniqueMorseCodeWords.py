from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morsecode=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res=[]
        for word in words :
            morse=""
            for char in word :
                morse+=morsecode[ord(char)-ord('a')]
            if morse not in res :
                res.append(morse)
        return len(res)