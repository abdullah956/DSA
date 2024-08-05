class Solution :
    def canConstruct(self, ransomNote :str , magazine :str) -> bool :
        Map = dict()
        for c in magazine :
            if c not in Map :
                Map[c] = 1
            else:
                Map[c] +=1
        for c in ransomNote :
            if not c in Map or Map[c]==0 :
                return False
            else:
                Map[c] -= 1
        return True