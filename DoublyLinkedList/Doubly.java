public class Doubly {
    class ListNode {
        int val ;
        ListNode next ;
        ListNode prev ;
        ListNode(int val){
            this.val= val;
            this.next= null;
            this.prev= null;
        }
    }

    ListNode head; 
    ListNode tail;
    int counter;
    void insertAtHead(int val){
        ListNode temp = new ListNode(val);
        if (head==null) {
            head = temp;
            tail = temp;
        }
        else {
            head.prev = temp;    
            temp.next = head;     
            head = temp;
            head.prev = null;
        }
        counter ++;
    }     
    void insertAtTail(int val){
        ListNode temp = new ListNode(val);
        if (head ==null){
            head = temp;
            tail = temp;
        }
        else {
            ListNode current = head;
            while (current.next!=null){
                current = current.next;
            }
            tail = current;        
            tail.next = temp;
            temp.prev = tail;
            tail = temp ;
           // tail.next = null;
        }
        counter ++;
    }
    void insertAtPosition(int position, int val){
        if (position>counter || position<1){
            return;
        }
        if (position==1){
            insertAtHead(val);
            return;
        }
        int i = 1;
        ListNode previous = null;
        ListNode temp = new ListNode(val);
        ListNode current = head;
        while (i < position ){
            previous = current;
            current = current.next;
            i++;
        }
        temp.prev = previous;        
        temp.next = previous.next ;
        previous.next = temp ;
        current.prev = temp;
        counter++;
    }
    void deleteHead(){
        if (head==null){
            return;
        }
        head = head.next;
        head.prev = null;
        counter--;
    }
    void deleteTail(){
        if (head==null ){
            return;
        }
        ListNode current = head;
        while (current.next!=null){
            current = current.next;
        }
        tail = current;
        tail = tail.prev;     
        tail.next = null;
        counter-=1;
    }
    void deleteAtPosition(int position){
        if (position > counter || position <1){
            return;
        }
        if (position==1){
            deleteHead();
            return;
        }
        int i = 1;
        ListNode current = head;
        ListNode previous = null;
        while (i < position ){
            previous = current;
            current  = current.next;
            i++;
        }
        previous.next = current.next;
        current.next.prev = previous;
        counter--;
    }
    void Print(){
        if (head==null){
            return;
        }
        ListNode current = head ;
        while (current!=null){
            System.out.print(current.val+"->");
            current= current.next;
        }
        System.out.println("NULL");
    }
    void PrintReverse(){
        if (head==null){
            return;
        }
        else {
            ListNode current = head ;
            while (current.next!=null){
                current = current.next;
            }
            tail = current;
            while (current!=null){
                System.out.print(current.val+"->");
                current= current.prev;
            }
        }
        System.out.println("NULL");
    }
    public static void main(String[] args) {
        Doubly DLL = new Doubly();
    }
}