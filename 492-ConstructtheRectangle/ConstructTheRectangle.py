from cmath import inf
from typing import List
class Solution :
    def contructRectangle (self, area :int) -> List[int] :
        minimumdifference =  float (inf) 
        a = [ area , 1 ]
        for width in range (1, int(area**0.5) +1) :
            length = area / width
            if length==int(length) and length>=width and length-width<minimumdifference :
                a[0] = int(length)
                a[1] = width
                minimumdifference = length - width
        return a
