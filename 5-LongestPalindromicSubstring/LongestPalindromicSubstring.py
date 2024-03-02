class Solution:
    def longestPalindrome(self, s: str) -> str:
        print("word is ddfkak")
        def check(i, j):
            left = i
            right = j - 1
            print("value of left at check : ", left)
            print("value of right at check : ", right)
            
            while left < right:
                print("alphabet at s left :", s[left])
                print("alphabet at s right : ", s[right])
                if s[left] != s[right]:
                    print("returning false because it left right alphabets didnt match")
                    return False
                
                left += 1
                right -= 1
            print("value of left after check increment : ",left)
            print("value of left after check increment : ",right)
            return True
        #range(start, stop, step)
        for length in range(len(s), 0, -1):
            print("length : ", len(s))
            print("length itself : ", length)
            for start in range(len(s) - length + 1): # 1 2
                print("start : ", start)
                print("stop : ", len(s) - length + 1 )
                if check(start, start + length):
                    return s[start:start + length]

        return ""
s = Solution()
print(s.longestPalindrome("ddfkak"))
"""                 
                    0            1              2              3              4            5         
                   #d            d              f              k              a            k          
                                                               start                         
                                                                                           length   
  
"""
               