class Solution :
    def guessNumber (self,n :int)-> bool :
        l = 1
        r = n
        while True:
            m=(l+r)//2
            result = guess(m)
            if result > 0 :
                l = m +1
            elif result < 0 :
                r = m-1
            else:
                return m