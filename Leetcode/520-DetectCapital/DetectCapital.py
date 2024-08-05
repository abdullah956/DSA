class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word==word.upper():
            return True
        elif word==word.lower():
            return True
        else:
            firstwordCheck=word[0]
            if word[0]==firstwordCheck.upper():
                restwordCheck=word[1:]
                if restwordCheck==restwordCheck.lower():
                    return True
        return False