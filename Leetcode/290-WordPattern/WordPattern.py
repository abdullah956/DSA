class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern) :
            return False
        charToWord = {}
        wordToChar = {}
        
        for i in range(len(words)) :
            a , b = pattern[i] , words[i]
            if a in charToWord and charToWord[a] != b :
                return False
            if b in wordToChar and wordToChar[b] != a :
                return False
            charToWord[a] = b
            wordToChar[b] = a
        return True