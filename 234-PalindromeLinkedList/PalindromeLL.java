import java.util.Scanner;
public class PalindromeLL{
    class Node{
        int data;
        Node next;
        Node(int data){
            this.data=data;
            this.next=null;
        }
    } 
    Node head;
    int count = 0;
    void addFirst(int x){
        ++count;
        Node temp = new Node(x);
        temp.data=x;
        temp.next=head;
        head=temp;
    }
    void reverseList() {
        if(head == null || head.next == null) {
            return;
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
        head = prev;
    }
    void addLast(int x){
        ++count;
        if(head==null){
            head = new Node(x);
        }
        else {
            Node node = head;
            while(node.next!=null){
                node=node.next;
            }
            Node temp = new Node(x);
            node.next = temp;
        }
    }
    void PrintList(){
        if(head==null){
            System.out.println("empty lists");
            return;
        }
        Node currNode = head;
        while(currNode!=null){
            System.out.print(currNode.data+" -> ");
            currNode = currNode.next;
        }
        System.out.println("NULL");
    }
    boolean isPalindromeArrayVersion(Node head){
        int [] nums = new int[count];
        int i = 0;
        count = count -1;
        while(i<=count){
            nums[i] = head.data;
            head = head.next;
            i++;
        }
        int l=0;
        int r=count;
        while (l<=r){
            if (nums[l]!=nums[r]){
                return false;
            } 
            l++;
            r--;    
        }
        return true;
    }
    boolean isPalindromePointerVersion(Node head){
        Node fast = head;
        Node slow = head;
        //find middle
        while (fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        //reverse second half
        Node prev = null;
        while (slow != null){
            Node temp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = temp;
        }
        //check palindrome
        Node left = head;
        Node right = prev;
        while (right != null){
            if (left.data != right.data){
                return false;
            }
            left = left.next;
            right = right.next;
        }
        return  true;
    }
        
    public static void main(String[] args) {
        PalindromeLL LL = new PalindromeLL ();
        Scanner sc = new Scanner(System.in);
        System.out.print("how many numbers : ");
        int limit = sc.nextInt();
        for(int i=0; i<limit; i++){
            System.out.println("\nenter number");
            int x = sc.nextInt();
            LL.addLast(x); //LL.addLast(x);
            LL.PrintList();
        }
        sc.close();
        LL.reverseList();
        LL.PrintList();
        System.out.println(LL.isPalindromeArrayVersion(LL.head));
        System.out.println(LL.isPalindromePointerVersion(LL.head));
    }
}