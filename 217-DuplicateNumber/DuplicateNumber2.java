import java.util.Arrays;

public class DuplicateNumber2 {
    public static void main ( String [] args){
        int [] nums = {1,2,3,4,5,6,3};
        Solution s = new Solution();
        System.out.println(s.containsDuplicate(nums));
    }
}
class Solution {
    public boolean containsDuplicate( int [] nums ){
        Arrays.sort(nums);
        for( int i=0; i<nums.length-1; i++){
            if( nums[i] == nums[i+1]){
                return true;
            }
        }
        return false;
    }
}