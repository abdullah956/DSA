class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l < r :
            print("string :",s)
            print("chars :",s[l],s[r])
            if s[l] != s[r] :
                print(l,r)
                print("skiping :",s[l+1:r+1],s[l:r])
                skipL,skipR=s[l+1:r+1],s[l:r]
                print(skipL,skipL[::-1])
                print(skipR,skipR[::-1])
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l,r=l+1,r-1
        return True
s=Solution()
print(s.validPalindrome("aabca"))
a="aabca"
print (a[2:4])
print(a[1:3])