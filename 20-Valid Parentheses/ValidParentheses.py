class Solution :
    def isValid(self,s : str)-> bool :
        stack = []
        closeToOpen = dict
        closeToOpen = { ")": "(", "}" : "{", "]" : "[" }
        for c in s :
            if c in closeToOpen :
                if stack and stack[-1] == closeToOpen[c] :
                    stack.pop()
                else :
                    return False
            else:
                stack.append(c)
        if not stack: #simple stack will mean stack has someting in it but not means if it does not
            return True
        else:
           return False

s = Solution()
paren = input("enter parentheses")
print(s.isValid(paren))