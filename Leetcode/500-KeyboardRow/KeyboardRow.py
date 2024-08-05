import re
from typing import List
class Solution :
    def findWords(self, words : List[str])  -> List[str] :
        output=[]
        for i in words :
            if re.match("^[qwertyui]+$", i.lower()) or re.match("^[asdfghjkl]+$",i.lower()) or re.match("^[zxcvbnm]+$", i.lower()) :
                output.append(i)
        return output