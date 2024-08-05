class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s)-1, -1, -1): # start stop step
            if s[i] != ' ':
                length += 1
            elif length > 0:
                break
        return length
st = "hello my name is abdullah "
s = Solution()
print(s.lengthOfLastWord(st))