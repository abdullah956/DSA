class Solution :
    def isIsomorphic(self, s : str , t : str) -> bool :
        mapST , mapTS = {},{}
        for a,b in zip(s,t) :
            if (a in mapST and mapST[a]!=b or b in mapTS and mapTS[b]!=a) :
                return False
            mapST[a] = b
            mapTS[b] = a

        return True
    
"""
egg
add
MAp1 {e:a  g:d  }
MAp2 {a:e  d:g  }
"""