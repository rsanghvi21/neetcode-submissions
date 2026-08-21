class Solution {
    public int removeDuplicates(int[] nums) {
        int right = 1;
        int left = 1;

        while (right < nums.length){
            // Not unique 
            if (nums[right] != nums[right - 1]){
                nums[left] = nums[right];
                left++;
            }
            right++;
        }

        return left;
    }
}