public class CircularDoubly {
    class ListNode {
        int val;
        ListNode next;
        ListNode prev;
        ListNode(int val){
            this.val = val;
            this.next = null;
            this.prev = null;
        }
    }
    ListNode head;
    ListNode tail;
    int counter;
    void addAtFirst(int val){
        ListNode temp = new ListNode(val);
        if (head==null){
            head = temp;
            tail = temp;
            tail.next = head;
        }
        else {
            temp.next = head;
            head.prev = temp;
            head = temp;
            tail.next = head;
        }
        counter++;
    }
    void addAtLast(int val){
        ListNode temp = new ListNode(val);
        if (head==null){
            head = temp;
            tail = temp;
            tail.next = head;
        }
        else {
            tail.next = temp;
            temp.prev = tail;
            tail = temp;
            tail.next = head;
        }
        counter++;
    }
    void addAtPosition(int val, int pos){
        if (head==null || pos>counter){
            return;
        }
        if (pos==1){
            addAtFirst(val);
            return;
        }
        ListNode current = head;
        ListNode previous = null;
        ListNode temp = new ListNode(val);
        int i = 1;
        while (i<pos){
            previous = current;
            current = current.next;
            i++;
        }
        previous.next = temp;
        temp.prev = previous;
        temp.next = current;
        current.prev = temp;
        counter++;
    }
    void deleteAtFirst(){
        if (head==null){
            return;
        }
        head = head.next;
        head.prev = null;
        tail.next = head;
        counter--;
    }
    void deleteAtLast(){
        if (head==null){
            return;
        }
        tail = tail.prev;
        tail.next = head;
        counter--;
    }
    void deleteAtPosition(int pos){
        if (head==null || pos>counter){
            return;
        }
        if (pos==1){
            deleteAtFirst();
            return;
        }
        ListNode current = head;
        ListNode previous = null;
        int i = 1;
        while (i<pos){
            previous = current;
            current = current.next;
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
        ListNode current = head;
        int i = 1;
        while (i<=counter){
            System.out.print(current.val+" -> ");
            current = current.next;
            i++;
        }
        System.out.println("null");
    }
    void PrintReverse(){
        if (head==null){
            return;
        }
        ListNode current = tail;
        int i = 1;
        while (i<=counter){
            System.out.print(current.val+" -> ");
            current = current.prev;
            i++;
        }
        System.out.println("null");
    }
    public static void main(String[] args) {
        CircularDoubly CD = new CircularDoubly();
    }
}