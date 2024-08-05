class MyQueue  :
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []
    def push(self,x :int) ->None :
        while self.stack1 :
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2 :
            self.stack1.append(self.stack2.pop())
    def pop(self) -> int :
        self.stack1.pop()
    def peek(self) -> int :
        return self.stack1[-1]
    def empty(self) -> bool :
        return not self.stack1
    

"""
stack1 = [2,1]
stack2 = []

"""