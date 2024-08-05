import java.util.*;   
public class Singly {
    class ListNode {
        int val ;
        ListNode next ;
        ListNode (int val){
            this.val = val;
            this.next = null;
        }
    }
    ListNode head;
    int counter;
    void insertAtHead(int val){
        ListNode temp = new ListNode(val);
        if (head==null) {
            head = temp;
        }
        else {
            temp.next = head;
            head = temp;
        }
        counter ++;
    }     
    void insertAtTail(int val){
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
        temp.next = previous.next ;
        previous.next = temp ;
        counter++;
    }
    void deleteHead(){
        if (head==null){
            return;
        }
        head = head.next;
        counter--;
    }
    void deleteTail(){
        if (head==null ){
            return;
        }
        ListNode current = head;
        ListNode previous = null;
        while (current.next!=null){
            previous = current ;
            current = current.next;
        }
        previous.next = null;
        counter--;
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
    ListNode thirdlastNode(){
        if (head==null || head.next==null || head.next.next==null){
            return null;
        }
        ListNode slow = head;
        ListNode fast = head;
        int i = 0 ;
        while (i<2){
            fast = fast.next;
            i++;
        }
        while (fast.next!=null){
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }
    ListNode Search(int val){
        if (head==null){
            return null;
        }
        ListNode current = head ;
        while (current!=null){
            if (current.val == val){
                return current;
            }
            current=current.next;
        }
        return null;
    }
    void insertionSortList(){
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = head;
        ListNode current = head.next;
        while (current!=null){
            if (current.val>=prev.val){
                prev = current;
                current = current.next;
                continue;
            }
            ListNode insert = dummy;
            while (current.val > insert.next.val){
                insert = insert.next;
            }
            prev.next = current.next;
            current.next = insert.next;
            insert.next = current;
            current = prev.next;
        }
        head = dummy.next;
    }
    void removeDupsFromSortedList(){
        if (head==null){
            return;
        }
        ListNode current = head;
        while (current!=null && current.next!=null){
            if (current.val == current.next.val){
                current.next = current.next.next;
            }
            else {
                current = current.next;
            }
        }
    }
    void removeDupsBySet(){
        if (head==null){
            return;
        }
        HashSet<Integer> SET = new HashSet<Integer>();
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode current = dummy;
        while (current!=null && current.next!=null){
            if (SET.contains(current.next.val)){
                current.next = current.next.next;
            }
            else {
                SET.add(current.next.val);
                current = current.next;
            }
        }
    }
    public static void main(String[] args) {
        Singly SLL = new Singly();
    }
}
