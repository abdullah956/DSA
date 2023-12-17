import typing
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0 :
            return ""
        prefix = strs[0]
        for i in range(1,len(strs)) :
            while(strs[i].find(prefix)!=0):
                prefix = prefix[0:len(prefix)-1]
        return prefix;

s = Solution()
arr = ["flower","flow","flight"]
string = s.longestCommonPrefix(arr)
print(string)