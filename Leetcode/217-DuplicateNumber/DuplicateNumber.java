import java.util.HashSet;

public class DuplicateNumber{
    public static void main(String [] args) {
        int [] nums = {1,2,3,4,5,3};
        Solution s = new Solution();
        boolean b = s.containsDuplicate(nums);
        System.out.println(b);
    }
}
class Solution {
    public boolean containsDuplicate( int [] nums ){
        HashSet<Integer> HI = new HashSet<>();
        for(int i =0; i<nums.length; i++){
            if(HI.contains(nums[i])){
                return true;
            }
            HI.add(nums[i]);
        }
        return false;
    }
}