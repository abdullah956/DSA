class ListNode :
    data = 0
    next = None
    prev = None
    def __init__(self,data:int) -> None:
        self.data = data
        self.next = None
        self.prev = None
    head = None
    tail = None
    counter = 0
    def insertAtHead(self,val:int) -> None :
        temp = ListNode(val)
        if not self.head  :
            self.head = temp
            self.tail = temp
        else :
            self.head.prev = temp
            temp.next = self.head
            self.head = temp
            self.head.prev = None
        self.counter +=1

    def insertAtEnd(self,val:int) -> None :
        temp = ListNode(val)
        if not self.head  :
            temp.next = None
            temp.prev = None
            self.head = temp
            self.tail = temp
        else :
            current = self.head
            while current.next:
                current = current.next
            self.tail = current
            self.tail.next = temp 
            temp.prev = self.tail
            self.tail = temp 
            self.tail.next = None
        self.counter +=1

    def insertAtPosition(self,position:int,val:int) -> None:
        if position > self.counter or position < 1 :
            return
        if position == 1 :
            self.insertAtHead(val)
        elif position == self.counter :
            self.insertAtEnd(val)
        else :
            i = 1
            previous = None
            temp = ListNode(val)
            current = self.head
            while i < position :
                previous = current
                current = current.next
                i+=1
            temp.prev = previous
            temp.next = previous.next 
            previous.next = temp 
            current.prev = temp
            self.counter+=1

    def deleteHead(self) -> None :
        if not self.head :
            return
        self.head = self.head.next 
        self.head.prev = None
        self.counter-=1

    def deleteTail(self) -> None :
        if not self.head :
            return
        current = self.head
        while current.next :
            current = current.next
        self.tail = current 
        self.tail = self.tail.prev
        self.tail.next = None
        self.counter-=1

    def deleteAtPosition(self,position:int) -> None :
        if position > self.counter or position < 1 :
            return
        if position == 1 :
            self.deleteHead()
        elif position == self.counter :
            self.deleteTail()
        else :
            i = 1
            current = self.head
            previous = None
            while i < position :
                previous = current
                current  = current.next
                i+=1
            previous.next = current.next
            current.next.prev = previous
            self.counter-=1

    def Print(self) -> None :
        if not self.head :
            return 
        else:
            current = self.head
            while current :
                print(current.data," -> ",end=" ")
                current = current.next
        print("NULL")

    def PrintReverse(self) -> None :
        if not self.head :
           return 
        else :
            current = self.head
            while current.next :
                current = current.next
            self.tail = current 
            while current :
                print(current.data," -> ",end=" ")
                current = current.prev
        print("NULL")

DLL = ListNode(None)
