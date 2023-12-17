class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True 
        
        if len(s) == 0 and len(t) != 0:
            return True 
        
        if len(s) != 0 and len(t) == 0:
            return False 
        
        s_pointer = t_pointer = 0     
        len_s, len_t = len(s), len(t)
        while s_pointer < len_s and t_pointer < len_t :
            
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1     
            t_pointer += 1 
        return s_pointer == len_s