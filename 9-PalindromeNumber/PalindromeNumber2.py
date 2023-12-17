class Solution:
    def isPalindrome (self , x):
        if x < 0 :
            return False
        original = x
        reversed = 0
        while x != 0 :
            remainder = x % 10
            reversed = reversed * 10 + remainder;
            x = x //10;
        return original == reversed


s = Solution()
print(s.isPalindrome(1259521))

