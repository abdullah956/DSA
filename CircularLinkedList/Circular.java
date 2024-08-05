public class Circular {
    class ListNode{
        int val; 
        ListNode next;
        ListNode(int val){
            this.val=val;
            this.next=null;
        } 
    } 
    ListNode head; 
    ListNode tail;
    int counter;
    void insertAtHead(int val){ 
        ListNode temp = new ListNode(val);
        if (head == null){
            head = temp ;             
            head.next = head;
            tail = head;
        }
        else{
            tail.next = temp ;
            temp.next = head ;
            head = temp ;
        }
        counter ++;
    }
    void insertAtTail(int val){
        ListNode temp = new ListNode(val) ;
        if (head == null) {
            head = temp ;
            head.next = head;
            tail = head;
        }              
        else {
            temp.next = tail.next ;
            tail.next = temp ;
            tail = temp ;
        }
        counter++ ;
    }
    void insertAtPosition(int val, int position){
        if (position > counter || position<1){
            return;
        }
        if (position == 1){
            insertAtHead(val) ;
            return;
        }
        int i = 1;
        ListNode current = head;
        ListNode previous = null;
        ListNode temp = new ListNode(val) ;
        while (i < position) {
            previous = current;
            current = current.next ;
            i++ ;
        }
        temp.next = previous.next ;
        previous.next = temp ;
        counter++;
    }
    void deleteHead(){
        if (head==null){
            return ;
        }
        else{
            tail.next = head.next ;
            head = head.next ;               
        }
        counter--;
    }
    void deleteTail(){
        if (head ==null){
            return ;
        }
        else {
            ListNode current = head ;
            while (current!=tail ){
                current = current.next ;
            }                                  
            tail = current ;                        
            tail.next = head ;
        }
        counter--;
    }
    void deleteAtPosition(int position){
        if (position>counter || position<1){
            return;
        }
        if (position == 1 ){
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
        counter--;
        
    }
    void Print(){
        if (head==null){
            return;
        }
        else{
            int i = 1;
            ListNode current = head;
            while (i <= counter ){
                System.out.print(current.val+"->"+" ");
                current = current.next;
                i+=1;
            }
        }
        System.out.println("NULL");
    }
    public static void main(String[] args) {
        Circular CLL = new Circular();
}
}