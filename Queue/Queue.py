class ListNode :
    data = 0
    next = None
    def __init__(self,data:int) -> None:
        self.data = data
        self.next = None
    head = None
    counter = 0

    def push(self,val:int) -> None :
        temp = ListNode(val)
        if not self.head :
            self.head = temp
        else :
            current = self.head
            while current.next :
                current = current.next
            current.next = temp
        self.counter+=1

    def popLeft(self) -> int :
        if not self.head :
            return 
        else :
            popped = self.head.data
            self.head = self.head.next
        self.counter-=1
        return popped
    
    def peek(self):
        if not self.head :
            return None
        else :
            current = self.head
            while current.next :
                current = current.next
            return current
        
    def isEmpty(self) -> bool :
        if self.counter == 0 :
            return True
        else :
            return False

    def Print(self) -> None :
        if not self.head :
            return 
        else:
            current = self.head
            print("[",end=" ")
            while current :
                print(current.data,",",end=" ")
                current = current.next
            print("]")

Q = ListNode(None)