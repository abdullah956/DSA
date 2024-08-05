import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
public class Tree {
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
    class TreeNode {
        int val ;
        TreeNode left ;
        TreeNode right ;
        TreeNode (int val){
            this.val = val;
            this.left = null;
            this.right = null;
        }
    }
    TreeNode root;
    ListNode takeHead(){
        return head;
    }
    TreeNode takeRoot(){
        return root;
    }
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
        root = sortedListToBST(takeHead());
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
        root = sortedListToBST(takeHead());
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
        root = sortedListToBST(takeHead());
    }
    void deleteHead(){
        if (head==null){
            return;
        }
        head = head.next;
        counter--;
        root = sortedListToBST(takeHead());
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
        root = sortedListToBST(takeHead());
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
        root = sortedListToBST(takeHead());
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
    List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode cur = root;
        while(cur!=null || !stack.empty()){
            while(cur!=null){
                stack.add(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            list.add(cur.val);
            cur = cur.right;
        }
        return list;
    }
    TreeNode sortedListToBST(ListNode head) {
        if(head==null) return null;
        return toBST(head,null);
    }
    TreeNode toBST(ListNode head, ListNode tail){
        ListNode slow = head;
        ListNode fast = head;
        if(head==tail) return null;
        while(fast!=tail&&fast.next!=tail){
            fast = fast.next.next;
            slow = slow.next;
        }
        TreeNode thead = new TreeNode(slow.val);
        thead.left = toBST(head,slow);
        thead.right = toBST(slow.next,tail);
        return thead;
    }
    public static void main(String[] args) {
        Tree t = new Tree();
        t.insertAtHead(13);
        t.insertAtTail(23);
        t.insertAtTail(33);
        t.insertAtTail(43);
        t.insertAtTail(53);
        t.insertAtTail(63);
        t.insertAtTail(73);
        t.insertAtTail(83);
        t.insertAtTail(93);
        t.Print();
        List<Integer> LI = t.inorderTraversal(t.takeRoot());
        System.out.println(LI);
        //TreeNode rooted = t.sortedListToBST(t.takehead());
        //List<Integer> LI = t.inorderTraversal(rooted);
        //System.out.println(LI);
    }
}