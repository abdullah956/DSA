class ListNode :
    data = 0
    next = None
    def __init__(self,data:int) -> None:
        self.data = data
        self.next = None
    head = None
    tail = None
    counter = 0

    def insertAtHead(self,val:int) -> None :
        temp = ListNode(val)
        if not self.head :
            self.head = temp
            self.head.next = self.head
            self.tail = self.head
        else:
            self.tail.next = temp
            temp.next = self.head
            self.head = temp
        self.counter+=1

    def insertAtEnd(self,val:int) -> None :
        temp = ListNode(val)
        if not self.head :
            self.head = temp
            self.head.next = self.head
            self.tail = self.head
        else :
            temp.next = self.tail.next
            self.tail.next = temp
            self.tail = temp
        self.counter+=1

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
            #temp.prev = previous
            temp.next = previous.next 
            previous.next = temp 
            #current.prev = temp
            self.counter+=1

    def deleteHead(self) -> None :
        if not self.head :
            return 
        else :
            self.tail.next = self.head.next
            self.head = self.head.next
        self.counter-=1

    def deleteTail(self) -> None :
        if not self.head :
            return
        else :
            current = self.head
            while current!=self.tail :
                current = current.next
            self.tail.next = current
            self.tail = current
            self.tail.next = self.head
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
                current = current.next
                i+=1
            previous.next = current.next
            self.counter-=1

    def Print(self) -> None :
        if not self.head :
            print("list is empty")
            return 
        else:
            i = 1
            current = self.head
            while i <= self.counter  :
                print(current.data," -> ",end=" ")
                current = current.next
                i+=1
        print("NULL")

CLL = ListNode(None)
