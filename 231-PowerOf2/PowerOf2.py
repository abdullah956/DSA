class Solution :
    def isPowerOfTwo(self,n : int )-> bool :
        check , i = 1 , 1
        while check <= n :
            if check == n :
                return True
            check = 2 ** i 
            i += 1
        return False

class Solution :
    def isPowerOfTwo(self,n : int )-> bool :
        if n<1 :
            return False
        if n == 1 :
            return True
        if n%2 == 1 :
            return False
        return self.isPowerOfTwo(n/2)