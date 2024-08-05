class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        SET = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in SET :
                SET.remove(s[l])
                l+=1
            SET.add(s[r])
            res = max(res,r-l+1)
        return res


        """"
        pwwkew
        l=0
        r=0
        setadd-p
        res = 0-0+1

        r=1
        setadd-w
        res = 1-0+1

        r=2
        while set s[2](w) in set :
            set remove (s[0](p))
            l+1
        l=2
        set is empty
        setadd-w
        res = 2-2+1

        r=3
        setadd-k
        res = 3-2+1

        r=4
        setadd-e
        res = 4-2+1

        r=5
        while set s[5](w) in set :
            set rempve s[2](w)
            l+1
        l=3
        setempty 
        setadd-w
        res = 5-3+1

        res max was 3 return 3
        """