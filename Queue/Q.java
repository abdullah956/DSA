public class Q {
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

    int POPLEFT(){
        if (head==null ){
            return -1;
        }
        int popped = head.val ;
        head = head.next ;
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
        Q que = new Q();
    }
}
