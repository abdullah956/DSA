class Solution {
    public int removeDuplicates(int[] nums) {
        int left = 1;
        if (nums.length<1){
            return 0;
        }
        for(int right=left; right<nums.length; right++){
            if (nums[right]!=nums[right-1]){
                nums[left]=nums[right];
                left++;
            }
        }
        return left;
    }
}

public class RemoveDuplicatesFromSortedArray {
    public static void main(String[] args) {
        Solution s = new Solution();
        int [] nums = {0,0,1,1,1,2,2,3,3,4};
        int uniquenumbers = s.removeDuplicates(nums);
        System.out.println(uniquenumbers);
    }
}
