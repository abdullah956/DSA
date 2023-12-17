class ListNode :
    val = 0
    next = None
    def __init__(self,val:int) -> None:
        self.val = val
        self.next = None
    head = None
    counter = 0
    
    def takeHead (self) :
        return self.head

    def returnHead(self,head) :
        self.head = head

    def insertAtHead(self,val:int) -> None :
        temp = ListNode(val)
        if not self.head :
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp
        self.counter+=1

    def insertAtEnd(self,val:int) -> None :
        temp = ListNode(val)
        if not self.head :
            self.head = temp
        else :
            current = self.head
            while current.next :
                current = current.next
            current.next = temp
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
            self.head = self.head.next
        self.counter-=1

    def deleteTail(self) -> None :
        if not self.head :
            return
        else :
            previous = None
            current = self.head
            while current.next :
                previous = current
                current = current.next
            previous.next = None
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
            previous = None
            current = self.head
            while i < position :
                previous = current
                current = current.next
                i+=1
            previous.next = current.next
            self.counter-=1

    def Print(self) -> None :
        if not self.head :
            return 
        else:
            current = self.head
            while current :
                print(current.val," -> ",end=" ")
                current = current.next
        print("NULL")
        
    def removeDupsBySet(self) -> None :
        if not self.head :
            return
        SET = set()
        dummy = ListNode(0)
        dummy.next = self.head
        current = dummy
        while current and current.next :
            if current.next.val in SET :
                current.next = current.next.next
            else :
                SET.add(current.next.val)
                current = current.next

    def insertionSort(self):
        dummy = ListNode(0) 
        dummy.next = self.head
        prev , current = self.head , self.head.next 
        while current :
            if current.val >= prev.val : 
                prev , current = current , current.next 
                continue 
            insert = dummy 
            while current.val > insert.next.val : 
                insert = insert.next
            prev.next = current.next 
            current.next = insert.next 
            insert.next = current
            current = prev.next 
        self.head = dummy.next

    def removeDupsSortedList(self) -> None:
        if not self.head :
            return
        current = self.head
        while current and current.next :
            if current.val == current.next.val :
                current.next = current.next.next
            else :
                current = current.next

    def mergeSort(self,head):
        if not head or not head.next :
            return head
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp 
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        return self.mergeLists(left,right)

    def getMid(self,head) :
        slow , fast = head , head.next
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeLists(self,left,right) :
        dummy = ListNode(0)
        current = dummy
        while left and right :
            if left.val < right.val :
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current=current.next
        if left :
            current.next = left
        else:
            current.next = right
        return dummy.next
    
    def thirdlastNode(self) :
        if not self.head or not self.head.next or not self.head.next.next:
            return None
        slow = fast = self.head
        i = 0
        while i<2 :
            fast = fast.next
            i+=1
        while fast.next:
            slow = slow.next
            fast = fast.next
        return slow
SLL = ListNode(None)
SLL.insertAtHead(89)
SLL.insertAtEnd(23)
SLL.insertAtEnd(34)
SLL.insertAtEnd(34)
SLL.insertAtEnd(34)
SLL.insertAtEnd(23)
SLL.insertAtEnd(34)
SLL.insertAtEnd(34)
SLL.insertAtEnd(89)
SLL.insertAtEnd(7)
SLL.insertAtEnd(34)
SLL.insertAtEnd(8)
SLL.insertAtEnd(34)
SLL.insertAtEnd(7)
SLL.insertAtEnd(8)
SLL.Print()
SLL.removeDupsBySet()
SLL.Print()
#SLL.Print()
#SLL.insertionSort()
#SLL.removeDupsSortedList()
#SLL.Print()
#print("removing dups in unnsorted list")
#SLL.removeDupsBySet()
#SLL.Print()
#print("list before sorting",end=" ")
#SLL.Print()
#SLL.returnHead(SLL.mergeSort(SLL.takeHead()))
#print("list after performing merge sort",end=" ")
#SLL.Print()
#SLL.removeDupsSortedList()
#print("list after removing duplicates",end=" ")
#SLL.Print()
