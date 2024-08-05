class Solution {
    public int removeElement(int[] nums, int val) {
        int actualsize=0;
        for(int i =0; i<nums.length; i++){
            if(nums[i]!=val){
                nums[actualsize]=nums[i];
                actualsize++;
            }
        }
        return actualsize;
    }
}
public class RemoveElement{
    public static void main(String[] args) {
        Solution s = new Solution();
        int [] nums = {3,2,2,3};
        int val = 3;
        System.out.println((s.removeElement(nums, val)));
    }
}