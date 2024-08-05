import java.util.Scanner;
import java.util.Stack;
class Solution {
    public boolean isValid(String s) {
        if(s.length()%2 !=0){
            return false;
        }
        Stack<Character> stack = new Stack<>(); // stack is last in first out 
        for(char c : s.toCharArray()){ //toCharArray converts this string into character array
            if(c=='(' || c=='{' || c=='['){
                stack.push(c);
            }
            else if(c==')' && !stack.isEmpty()  && stack.peek() == '('){
                stack.pop(); // removes an element from the top of stack
            }
            else if(c=='}' && !stack.isEmpty()  && stack.peek() == '{'){
                stack.pop(); // stack.peek() is used to get reference of element at stack's top
            }
            else if(c==']' && !stack.isEmpty()  && stack.peek() == '['){
                stack.pop();
            }
            else{
                return false;
            }
        }
        return stack.isEmpty();
    }
}

public class ValidParentheses {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter paratheses");
        String str = sc.nextLine();
        Solution s = new Solution();
        System.out.println(s.isValid(str));
        sc.close();
    }
}
