public class ReversedLinkedList {
    
    public static void main(String [] args) {
        
    }
}
class Solution{
    Node head;
    class Node{
        int data;
        Node next;
        Node(int x){
            this.data=x;
            this.next=null;
        }
        Node(){

        }
    }
    public Node reverseList(Node head) {
        if(head == null || head.next == null) {
            return head;
        }
        Node prev=null,next=null;
        Node current=head;
        while(current != null)
        {
            next=current.next;
            current.next=prev;
            prev=current;
            current=next;
        }
        return prev;
    }
}