
public class STACK {
    class ListNode {
        int val ;
        ListNode next ;
        ListNode (int val){
            this.val = val;
            this.next = null;
        }
    }
    ListNode head;
    int counter=0;
    void PUSH(int val){
        ListNode temp = new ListNode(val);
        if (head ==null){
            head = temp;
        }
        else {
            ListNode current = head;
            while (current.next!=null){
                current = current.next;
            }
            current.next = temp;
        }
        counter ++;
    }
    ListNode POP(){
        if (head==null ){
            return null;
        }
        ListNode current = head;
        ListNode previous = null;
        while (current.next!=null){
            previous = current ;
            current = current.next;
        }                                 
        ListNode popped = current;
        previous.next = null;
        counter--;
        return popped;
    }
    ListNode PEEK(){
        if (head==null){
            return null;
        }
        ListNode current = head ;
        while (current.next!=null) {
            current = current.next;
        }
        return current;
    }         

    boolean isEMPTY(){
        if (counter == 0) {
            return true;
        }
        else {
            return false;
        }
    }
    void Print(){
        if (head==null){
            return;
        }
        ListNode current = head ;
        System.out.print("[");
        while (current!=null){
            System.out.print(current.val+",");
            current= current.next;
        }
        System.out.println("]");
    }
    public static void main(String[] args) {
        STACK S = new STACK();
        System.out.println("appending values :");
        S.PUSH(12);
        S.PUSH(23);
        S.PUSH(34);
        S.PUSH(45);
        S.Print();
        System.out.println("taking a peek : "+(S.PEEK()).val);
        S.Print();
        System.out.println("popping from stack : "+(S.POP()).val);
        S.Print();
        System.out.println("checking if the stack is empty : "+S.isEMPTY());
        S.Print();
    }
}
