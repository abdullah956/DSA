from collections import deque


class Mystack :
    def __init__(self) -> None:
        self.q=deque()
    def push(self, x:int)->None :
        self.q.append(x)
    def pop(self) :
        for i in range (len(self.q)-1) :
            self.push(self.q.popleft())
        return self.q.popleft()
    def top(self) :
        return self.q[-1]
    def empty(self) :
        return len(self.q)==0
    

    """
    1 2 3
after pop
 3 2 1
 return 3

    """