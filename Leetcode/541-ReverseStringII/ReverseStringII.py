class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k>=len(s):
            return s[::-1]
        s=list(s)
        for i in range(0,len(s),2*k):
            print(i)
            s[i:i+k]=reversed(s[i:i+k])
            print(s[i:i+k])
        return "".join(s)

s=Solution()
sr="abcdefg"
print(s.reverseStr(sr,2))
