public class TwoSum {
    public static void main(String[] args) {
        Solution s = new Solution();
        int [] nums = {2,7,11,15};
        int target = 9;
        int [] nums2 = s.twoSum(nums,target);
        for(int i=0; i<nums2.length; i++){
            System.out.println(nums2[i]);
        }
    }
}
class Solution{
    public int[] twoSum(int[] nums, int target){
        int a = 0;
        int b = nums.length-1;
        while(a <= b){
            int sum = nums[a] + nums[b];
            if (sum>target){
                b = b - 1;
            }
            else if(sum<target){
                a = a + 1;
            }
            else{
                return new int[] {a+1,b+1};
            }
        }
        return new int[] {a+1,b+1};
    }
}