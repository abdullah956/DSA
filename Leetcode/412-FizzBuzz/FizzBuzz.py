class Solution(object):
    def fizzBuzz(self, n):
        output=[]
        for i in range(1,n+1) :
            result=""
            if i%3==0:
                result +="Fizz"
            if i%5==0:
                result +="Buzz"
            if result=="":
                result += str(i)
            output.append(result)
        return output