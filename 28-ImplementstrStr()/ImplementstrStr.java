class Solution {
    public int strStr(String haystack, String needle) {
    // here if we want then we can take the int as final.
      int m = haystack.length();
      int n = needle.length();
          // m-n+1 means loop will run last that number of the string which is as the length of the needle suppose needle length is 3 then we have to run the loop until lasr 3rd element.
  for (int i = 0; i < m - n + 1; ++i)
  // in if condition it checks , by taking the substring from the number to the needle length with the needle
    if (haystack.substring(i, i + n).equals(needle))
      return i;
  
  return -1;
    }
  }
public class ImplementstrStr {
  public static void main(String[] args) {
    Solution s = new Solution();
    String haystack="hello";
    String needle = "ll";
    int result = s.strStr(haystack,needle);
    System.out.println(result);
  }
}